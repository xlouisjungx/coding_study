lst=list(map(str,input()))

stack=[]
stack_num=0
i=0
ans=0
while i<len(lst):
    if lst[i]=='(' and lst[i+1]==')': # 레이저 발사하는 경우
        ans+=stack_num # 레이저로 막대가 분할되어, 막대 수 만큼 더 해줌
        i+=1
        
    elif lst[i]=='(': # 막대 시작부분 처리
        stack.append(lst[i])
        stack_num+=1

    elif lst[i]==')': # 막대 끝부분 처리
        stack.pop()
        stack_num-=1
        ans+=1 # 원래 막대도 하나 더해줌
    i+=1

print(ans)