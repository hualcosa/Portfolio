class DSU:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self, x):
        if self.rep[x] != x:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        
        if self.rank[rx] > self.rank[ry]:
            self.rep[ry] = rx
        else:
            self.rep[rx] = ry
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1
                
    def flatten(self):
        self.rep = [self.find(x) for x in range(len(self.rep))]
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # mapping: email -> [account_id]
        # connects emails/
        # what does it mean if
        # a -> [1, 2]
        # b -> [2, 3]
        # it means that [1, 2, 3] belong to the same person.
        # DSU
        
        # Use DSU to merge common accounts under one representant -> one idx
        dsu = DSU(len(accounts))
        email_to_id = {}
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    dsu.union(email_to_id[email], idx)
                else:
                    email_to_id[email] = idx
        dsu.flatten()
        
        # create set of unique emails == merge emails
        # from all accounts that are grouped under one representant
        representant_to_emails = defaultdict(lambda: set())
        for idx, account in enumerate(accounts):
            r = dsu.find(idx)
            representant_to_emails[r].update(account[1:])
        
        # Utility mapping to extract name
        account_to_name = dict([(idx, account[0]) for idx, account in enumerate(accounts)])
        
        merged_accounts = []
        for account_id, emails in representant_to_emails.items():
            name = account_to_name[account_id]
            merged_accounts.append([name] + sorted(emails))
            
        return merged_accounts