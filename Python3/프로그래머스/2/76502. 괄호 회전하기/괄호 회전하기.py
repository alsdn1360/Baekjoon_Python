# 입력된 괄호를 왼쪽으로 x 만큼 회전하는 함수
def rotate(s, x):
    return s[x:] + s[:x]

# 괄호의 짝이 맞는지 확인하는 함수
def check(s):
    stack = []
    
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c) # 여는 괄호이면 스택에 푸시
        elif c == ')':
            if not stack: # 만약 스택이 비어있으면 False 리턴
                return False
            elif stack[-1] == '(': # 스택의 가장 위 항목이 ( 이면 팝
                stack.pop()
        elif c == '}':
            if not stack:
                return False
            elif stack[-1] == '{':
                stack.pop()
        elif c == ']':
            if not stack:
                return False
            elif stack[-1] == '[':
                stack.pop()
    
    if stack: # 스택이 비어있지 않으면 False 리턴
        return False
    else:
        return True

def solution(s):
    answer = 0
    rotate_s = []
    
    for i in range(len(s)):
        rotate_s = rotate(s, i)
        
        if check(rotate_s):
            answer += 1
            
    return answer
            
    