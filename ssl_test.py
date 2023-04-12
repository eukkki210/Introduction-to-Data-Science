# 테스트 코드
import ssl

ll = ssl.LinkedList()

# append() 함수 테스트
ll.append(100)
ll.append(72)
ll.append(325)
ll.traverse_all() # 예상 출력: head -> (100) -> (72) -> (325) -> null 

