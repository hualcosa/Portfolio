class Solution:
    import re
    def simplifyPath(self, path: str) -> str:
        ## preprocessing
        # the path must start with a slash
        if path[0] != '/':
            path = '/' + path
        # removing unecessary slash
        path = re.sub("//+", "/", path)
        # removing trailing slash
        path = path[:-1] if path[-1] == '/' else path
        # edge case - empty string
        path = '/' if len(path) == 0 else path
        dir_list = path.split('/')[1:]
        ans = []
        for i, symbol in enumerate(dir_list):
            if symbol == '.' or (symbol == '..' and len(ans) == 0):
                continue
            if symbol == '..' and len(ans) > 0:
                ans.pop()
                continue
            ans.append(symbol)
                
        return '/' + '/'.join(ans)
            
                
            