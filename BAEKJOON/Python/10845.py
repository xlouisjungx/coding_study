# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

stack = []
result = []

def push(list):
    stack.append(list[-1])

def pop(list):
    if len(list) == 0:
        result.append(-1)
    else:
        n = list[0]
        stack.remove(n)
        result.append(n)

def size(list):
    result.append(len(list))

def empty(list):

    if len(list) == 0:
        result.append(1)
    else:
        result.append(0)

def front(list):
    if len(list) == 0:
        result.append(-1)
    else:
        result.append(list[0])

def back(list):
    if len(list) == 0:
        result.append(-1)
    else:
        result.append(list[-1])
        

N = int(input())

for i in range(N):
    num = list(map(str, input().split()))

    if 'push' in num:
        push(num)
        
    elif 'pop' in num:
        pop(stack)

    elif 'size' in num:
        size(stack)

    elif 'empty' in num:
        empty(stack)

    elif 'front' in num:
        front(stack)

    elif 'back' in num:
        back(stack)

for i in range(len(result)):
    print(result[i])  
