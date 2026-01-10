class Solution:
    def maximumToys(self, N, A, Q, Queries):
        # Store (cost, original_index) and sort by cost
        sorted_toys = []
        for i in range(N):
            sorted_toys.append((A[i], i + 1))
        sorted_toys.sort()

        # Map original 1-based index to its position in the sorted array
        pos_in_sorted = [0] * (N + 1)
        for i in range(N):
            pos_in_sorted[sorted_toys[i][1]] = i + 1

        # BITs for sum and count
        bit_sum = [0] * (N + 1)
        bit_count = [0] * (N + 1)

        def update(bit, idx, val):
            while idx <= N:
                bit[idx] += val
                idx += idx & (-idx)

        def query_bit(bit, idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        # Initialize BITs with all toys
        for i in range(N):
            update(bit_sum, i + 1, sorted_toys[i][0])
            update(bit_count, i + 1, 1)

        results = []
        for q in Queries:
            C = q[0]
            K = q[1]
            broken_indices = q[2:]

            # Temporarily remove broken toys
            removed = []
            for idx in broken_indices:
                p = pos_in_sorted[idx]
                cost = A[idx-1]
                update(bit_sum, p, -cost)
                update(bit_count, p, -1)
                removed.append(p)

            # Binary lifting on BIT to find max toys within budget C
            pos = 0
            current_sum = 0
            current_count = 0
            
            # log2 of N is roughly 17-18 for 10^5
            for i in range(17, -1, -1):
                next_pos = pos + (1 << i)
                if next_pos <= N and current_sum + bit_sum[next_pos] <= C:
                    pos = next_pos
                    current_sum += bit_sum[pos]
                    current_count += bit_count[pos]

            results.append(current_count)

            # Backtrack: Add broken toys back for the next independent query
            for p in removed:
                cost = sorted_toys[p-1][0]
                update(bit_sum, p, cost)
                update(bit_count, p, 1)

        return results