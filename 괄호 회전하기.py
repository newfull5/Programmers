def solution(s):
    def check(s):
        stack = []

        while s:
            stack.append(s.pop(0))

            while True:
                if len(stack) >= 2:
                    if stack[-1] == ']' and stack[-2] == '[':
                        stack.pop()
                        stack.pop()
                        continue

                    if stack[-1] == ')' and stack[-2] == '(':
                        stack.pop()
                        stack.pop()
                        continue

                    if stack[-1] == '}' and stack[-2] == '{':
                        stack.pop()
                        stack.pop()
                        continue

                break

        if not stack:
            return True
        return False
    
    s = list(s)
    answer = 0
    
    for _ in range(len(s)):
        s.append(s.pop(0))
        if check(s[:]):
            answer += 1
            
    return answer
