import sys

T = int(input())

result = []

def Solve(VPS_L):

    String = []
    
    for j in VPS_L:
        if j == '(':
            String.append(j)

        elif j == ')':
            if len(String) != 0:
                String.pop()
            else:
                return "NO"

    if len(String) == 0:
        return "YES"
    else:
        return "NO"

for i in range(T):
    VPS_L = sys.stdin.readline().strip() 
    # strip()은 문자열의 앞뒤 공백(띄어쓰기, 개행 문자 \n, 탭 \t)을 제거하는 메서드
    result.append(Solve(VPS_L))
     

for i in range(len(result)):
    print(result[i])