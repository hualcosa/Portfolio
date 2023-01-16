class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key= lambda x: (x[0],x[1])):
            users[user].append(site)
            
        patterns = Counter()
        
        for user, sites in users.items():
            # we create a set because doesn't matter how many times the user repeated the pattern
            # only the count of users is important
            patterns.update(Counter(set(combinations(sites, 3))))
        
        # get most frequent 3-sequence sorted lexicographically
        return max(sorted(patterns), key=patterns.get)