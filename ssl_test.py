# 테스트 코드
from myssl import *

if __name__ == '__main__':
    ll = LinkedList()

    # append() 함수 테스트
    ll.append(100)
    ll.append(72)
    ll.append(325)
    ll.first()
    ll.traverse_all() 
    # 예상 출력: head -> (100) -> (72) -> (325) -> null 
    # 실제 출력: head ->
    # ssl.py가 아닌 Python 내장 모듈 중 하나인 'ssl' 모듈을 임포트한 것 같음 -> 파일 명 myssl.py로 변경
    # traverse_all 함수 실행 전에 first 함수를 호출해야됨.
    # 실제 출력: head ->(100) -> (72) -> (325) -> null

    # insert_at() 함수 테스트
    ll.insert_at(2, 500)
    ll.first()
    ll.traverse_all() 
    # 예상 출력: head -> (100) -> (500) -> (72) -> (325) -> null
    # 실제 출력: head ->(100) -> (500) -> (72) -> (325) -> null

    # remove() 함수 테스트
    ll.remove(72)
    ll.first()
    ll.traverse_all()
    # 예상 출력: (100) -> (500) -> (325) -> null