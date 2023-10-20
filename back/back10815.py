import sys

num=int(input())
card=list(map(int,sys.stdin.readline().split()))

num2=int(input())
check=list(map(int,sys.stdin.readline().split()))

res=[]

card.sort()

def bs(x):
    low=0
    high=num-1

    while low<=high:        
        mid=(low+high)//2
        if(card[mid]==x):
            return 1
        elif(x<card[mid]):
            high=mid-1
        elif(x>card[mid]):
            low=mid+1
        
    return 0

for i in check:
    print(bs(i),end=' ')
    
    #이분탐색 알고리즘
    #1~50중에 숫자를 맞추는 게임을 했다고 했을때 업다운게임과 같이 중앙값에서 확인한후 찾아가는 방식