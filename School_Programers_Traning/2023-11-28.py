a = '!@#$%^&*('
b = '\'"<>?:;'
print(a+"\\"+b)

# 문자 개수 세기

# 문자열 모듈 임포트
import string

def solution(my_string):
    
    # 솔루션 정의
    # 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때
    # my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수
    # my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를
    # 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
    
    # 알파벳 순서가 배열의 순서가 되도록 맞춰야하고
    # 문자열의 순번에 따라 해당 배열의 순번 0값 증가
    
    # 알파벳 대문자, 소문자 가져오기
    all_letters = string.ascii_uppercase + string.ascii_lowercase
    
    # 알파벳 순번 값으로 매핑하기
    alphabet_mapping = {letter: index for index, letter in enumerate(all_letters)}
    
    # 배열 값 0으로 초기화
    answer = [0] * 52
    
    for char in my_string :
        if char in alphabet_mapping :
            answer[alphabet_mapping[char]] += 1
    
    return answer