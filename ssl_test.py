# 테스트 코드
from ssl import *

if __name__ == '__main__':
    ll = LinkedList()

    # append() 함수 테스트
    ll.append(100)
    ll.append(72)
    ll.append(325)
    ll.traverse_all() 
# 예상 출력: head -> (100) -> (72) -> (325) -> null 
# 실제 출력: head ->
# ssl.py가 아닌 Python 내장 모듈 중 하나인 'ssl' 모듈을 임포트한 것 같음