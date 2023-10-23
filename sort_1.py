def solution(array, commands):  #프로그래머스 K번째 수 정렬문제
    sub=[]  #자르고 정렬해놓을 임시 리스트 생성
    answer=[]
    
    for i in range (0,len(commands)):   #리스트의 길이만큼 반복
   
        for k in range (commands[i][0]-1,commands[i][1]):  # x번째부터 y번째까지의 수를 임시 리스트에 저장후 정렬
            sub.append(array[k])
            sub.sort()
            
        
        answer.append(sub[commands[i][2]-1])    # 정답리스트에 정렬해놓은 임시리스트의 K번째 수 추출
        print(sub)
        sub.clear()   
        
            
         
    print(sub)
  
 
    return answer
    