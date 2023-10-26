#프로그래머스 가장 큰수 문제

def solution(numbers):
    numbers = list(map(str, numbers))   # map 함수를 이용해 list안의 모든 값을 문자열로 변환
    numbers.sort(key=lambda x: x * 3, reverse=True) # lambda : x:x*3 : 모든 리스트값을 3번 반복하고 그값을 기준으로 정렬 ex) 6=>666 , reverse를 통해 내림차순 정렬
    #문자열에서의 대소비교는 문자열 첫 번째 인덱스를 아스키 숫자로 바꿔 비교하고, 같으면 다음 인덱스를 비교하는 형식 ex) a=66 b=67 이면 앞자리는 같으니까 다음인덱스가 더큰 b가 더크다
    # x*3을 하는 이유는 입력되는 숫자 최대 크기조건이 1000미만이라 세자리수까지만 비교하면됨
    return str(int(''.join(numbers)))  # [0,0,0,0]일때 실행한값이 "0000" 이 나오지 않도록 수정