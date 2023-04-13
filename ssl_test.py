# 201701257 브라질학과/Software&AI 류승기

# 테스트 코드
from myssl import *

if __name__ == '__main__':
    ll = LinkedList()

    # append() 메소드 테스트
    ll.append(100)
    ll.append(72)
    ll.append(325)
    ll.traverse_all() 
    # 예상 출력: head -> (100) -> (72) -> (325) -> null 
    # 실제 출력: head ->
    # ssl.py가 아닌 Python 내장 모듈 중 하나인 'ssl' 모듈을 임포트한 것 같음 -> 파일 명 myssl.py로 변경
    # traverse_all 메소드 실행 전에 first 메소드를 호출해야됨.
    # 실제 출력: head ->(100) -> (72) -> (325) -> null

    # insert_at() 메소드 테스트
    ll.insert_at(2, 500)
    ll.traverse_all() 
    # 예상 출력: head -> (100) -> (500) -> (72) -> (325) -> null
    # 실제 출력: head ->(100) -> (500) -> (72) -> (325) -> null

    # remove() 메소드 테스트
    ll.remove(72)
    ll.traverse_all()
    # 예상 출력: 3번째 원소(key)를 삭제합니다.\nhead -> (100) -> (500) -> (325) -> null
    # 실제 출력: �ش��ϴ� ���Ұ� �����ϴ�.\nhead ->(100) -> (500) -> (72) -> (325) -> null 
    # remove 메소드에서 line 126의 cur_node 자체(node 객체)가 아닌 cur_node의 data 값을 key와 비교해야 함.
    # 추가적인 문제: 메시지가 �ش��ϴ� ���Ұ� �����ϴ�.라고 뜸 -> jpn 환경에서는 제대로 인코딩 됨
    # 생각해보니 삭제되는 node의 data 값이 아니라 node의 위치 (몇 번째)가 나와야됨. -> idx라는 변수를 지정하기로 함.
    # 4번째 원소(key)를 삭제합니다.라고 뜸: head를 첫 번째 원소라고 계산한 것으로 보임. 
    # -> head node의 위치가 0번째 원소인 것으로 취급하여 출력 시 idx-1로 수정.
    # 실제 출력: 3��° ����(key)�� �����մϴ�.\nhead ->(100) -> (500) -> (325) -> null
    
    ll.remove(999)
    ll.traverse_all()
    # 예상 출력: 해당하는 원소가 없습니다.\nhead ->(100) -> (500) -> (325) -> null
    # 실제 출력: �ش��ϴ� ���Ұ� �����ϴ�.\nhead ->(100) -> (500) -> (325) -> null

# pdf에 있는 테스트 코드
if __name__ == '__main__':
    ll = LinkedList()
    ll.append(5)
    ll.append(2)
    ll.append(1)
    ll.append(2)
    ll.append(7)
    ll.append(2)
    ll.append(11)
    ll.traverse_all()

print('first :', ll.first()) # first : 5
print('next :', ll.next()) # next : 2
print('size :', ll.size()) # size : 7
print('delete :', ll.delete()) # delete : 2
# 실제 출력 결과: delete : None -> delete() 메소드의 return 값 인덴트를 바꾸면서 해결 
print('size :', ll.size()) # size : 6
# 실제 출력 결과: size : 7 -> 위와 같은 방법으로 해결
print('current:', ll.current.data)# current: 5
# 실제 출력 결과: current : 2 -> 초기화가 되지 않은 듯 -> delete() 메소드의 마지막에 self.first() 호출
print('tail:', ll.tail.data) # tail: 11
print('first :', ll.first()) # first : 5
print('next :', ll.next()) # next : 1
# next : 2
print('next :', ll.next()) # next : 2
# next : 1
print('next :', ll.next()) # next : 7
# next : 2
# ==> self.current = self.before 코드를 수행하면서 가리키는 node가 변경된 문제 line 61에서 모두 해결

# 전체 노드 data 표시하기
data = ll.first()

if data:
    print(data, end=' ')
while True:
    data = ll.next()
    if data:
        print(data, end=' ')
    else:
        break
# 예상 출력 결과: 5 1 2 7 2 11
# 실제 출력 결과: 5 2 1 2 7 2 11
# 뭐가 문제지..? -> 위에서 delete할 때 삭제가 안된듯?
# -> delete 메소드에 else문 추가: 삭제하려는 node가 tail일 때
# next 메소드에서도 현재 node가 None일 경우 다음 node를 찾지 않고 None을 반환하도록 수정
# 구글링을 통해 solution을 찾긴 했지만 100% 완벽히 이해X => review 필요