class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def accMerge(self, arr):
        n = len(arr)
        dsu = DSU(n)
        email_to_acc = {} # email -> first account index seen

        # Step 1: Union accounts that share emails
        for i in range(n):
            for email in arr[i][1:]:
                if email in email_to_acc:
                    dsu.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i

        # Step 2: Group emails by their root parent index
        merged_emails = {} # root_index -> set of emails
        for email, acc_idx in email_to_acc.items():
            root = dsu.find(acc_idx)
            if root not in merged_emails:
                merged_emails[root] = set()
            merged_emails[root].add(email)

        # Step 3: Format the result
        result = []
        for root_idx, emails in merged_emails.items():
            name = arr[root_idx][0]
            result.append([name] + sorted(list(emails)))

        return result