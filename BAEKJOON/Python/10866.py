# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque

Deque = deque()
result = []

def push_front(list):
    Deque.appendleft(int(list[1]))

def push_back(list):
    Deque.append(int(list[1]))

def pop_front(list):
    if len(Deque) == 0:
        result.append(-1)
    else:
        n = Deque.popleft()
        result.append(n)

def pop_back(list):
    if len(Deque) == 0:
        result.append(-1)
    else:
        n = Deque.pop()
        result.append(n)

def size():
    result.append(len(Deque))

def empty():

    if len(Deque) == 0:
        result.append(1)
    else:
        result.append(0)

def front():
    if len(Deque)==0:
        result.append(-1)
    else:
        result.append(Deque[0])

def back():
    if len(Deque) == 0:
        result.append(-1)
    else:
        result.append(Deque[-1])
        

N = int(input())

for i in range(N):
    num = list(map(str, input().split()))

    if 'push_front' in num:
        push_front(num)

    elif 'push_back' in num:
        push_back(num)
        
    elif 'pop_front' in num:
        pop_front(Deque)

    elif 'pop_back' in num:
        pop_back(Deque)

    elif 'size' in num:
        size()

    elif 'empty' in num:
        empty()

    elif 'front' in num:
        front()

    elif 'back' in num:
        back()

for i in range(len(result)):
    print(result[i])  
