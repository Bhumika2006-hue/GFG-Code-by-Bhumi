class Solution():
    def checkRedundancy(self, s):
        stack = []
        operators = set(['+', '-', '*', '/'])

        for ch in s:
            if ch == ')':
                top = stack.pop()
                has_operator = False

                while top != '(':
                    if top in operators:
                        has_operator = True
                    top = stack.pop()

                # If no operator inside brackets → redundant
                if not has_operator:
                    return True
            else:
                stack.append(ch)

        return False
