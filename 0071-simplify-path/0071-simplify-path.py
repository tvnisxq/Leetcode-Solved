class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        canPath = path.split("/")

        for c in canPath:
            if c == "..":
                if stack: stack.pop()
            elif c != "" and c != ".":
                stack.append(c)
                c = ""
            else:
                c += c
        return "/" + "/".join(stack)

