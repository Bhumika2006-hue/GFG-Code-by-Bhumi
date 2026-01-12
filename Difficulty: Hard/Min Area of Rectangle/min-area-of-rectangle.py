class Solution:
    def minArea(self, path: str, fr: int, fc: int) -> int:
        
        def get_final_pos(moves, limit, target):
            # limit is n or m. Grid indices are 0 to limit-1
            curr = 0
            for move in moves:
                if move == 'pos': # 'D' or 'R'
                    if curr + 1 < limit:
                        curr += 1
                else: # 'U' or 'L'
                    if curr - 1 >= 0:
                        curr -= 1
            return curr

        def find_min_dim(moves, target):
            # Binary search for the smallest dimension (limit)
            # The maximum possible dimension needed is path length + 1
            low = target + 1
            high = len(path) + 1
            res = -1
            
            while low <= high:
                mid = (low + high) // 2
                final = get_final_pos(moves, mid, target)
                
                if final == target:
                    res = mid
                    high = mid - 1 # Try to find a smaller dimension
                elif final < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return res

        # Separate the path into vertical and horizontal components
        v_moves = []
        h_moves = []
        for char in path:
            if char == 'D': v_moves.append('pos')
            elif char == 'U': v_moves.append('neg')
            elif char == 'R': h_moves.append('pos')
            elif char == 'L': h_moves.append('neg')

        # Find min n (rows) and min m (cols)
        min_n = find_min_dim(v_moves, fr)
        min_m = find_min_dim(h_moves, fc)

        if min_n != -1 and min_m != -1:
            return min_n * min_m
        else:
            return -1