# 201701257 브라질학과/Software&AI 류승기

# Node 클래스 정의
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


# LinkedList 클래스 정의
class LinkedList:

	# 초기화 메소드
	def __init__(self):
		dummy = Node("dummy")
		self.head = dummy
		self.tail = dummy

		self.current = None
		self.before = None

		self.num_of_data = 0

	# append 메소드 (insert1 - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
	def append(self, data):
		new_node = Node(data)
		self.tail.next = new_node
		self.tail = new_node

		self.num_of_data += 1

	# delete 메소드 (delete1 - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
	def delete(self):
		pop_data = self.current.data

		if self.current is self.tail:
			self.tail = self.before

			# 중요 : current가 next가 아닌 before로 변경된다.
			self.before.next = self.current.next
			self.current = self.before 

			self.num_of_data -= 1

			return pop_data

	# first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
	def first(self):
		# 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
		if self.num_of_data == 0: 
			return None

		self.before = self.head
		self.current = self.head.next

		return self.current.data

	# next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
	def next(self):
		if self.current.next == None:
			return None

		self.before = self.current
		self.current = self.current.next

		return self.current.data

	# size 메소드
	def size(self):
		return self.num_of_data 
	
	# traverse_all 메소드 (search3 - 순차적으로 모든 원소 탐색, 각 노드의 data print, 이전에 first 메소드가 한번은 실행되어야 함)
	def traverse_all(self):
		if self.num_of_data == 0:
			return None
		
		print("head -> ", end="")
		# 현재 노드를 가리키는 변수 초기화 (변수 사용하지 않으면 while문이 무한 루프에 빠짐)
		cur_node = self.current
		# 현재 노드 (헤드 노드의 다음 노드)가 None이 아닐 때까지 반복하여 현재 노드의 데이터 출력
		while cur_node is not None:
			print(f"({cur_node.data})", end="")
			if cur_node.next is not None:
				print(" -> ", end="")
			# 다음 노드가 없을 때(null), 즉 연결리스트의 마지막 노드일 때 "-> null"출력
			else:
				print(" -> null")
			cur_node = cur_node.next
		
	# insert_at 메소드 (insert2 - 주어진 position에 노드 추가, before과 node의 next, 데이터 개수 변경)
	def insert_at(self, position, new_data):
		# position이 1보다 작은 경우 메소드 종료 (error)
		if position < 1:
			print("오류: 위치가 1보다 크거나 같아야 합니다.")
			return None
		# position이 num_of_data보다 큰 경우, append 메소드를 호출하여 맨 마지막에 new_data 삽입
		elif position > self.num_of_data:
			self.append(new_data)
			return None
		# 유효한 position의 경우
		new_node = Node(new_data)
		# 현재 node 탐색 (현재 위치 1로 초기화)
		cur_pos = 1
		cur_node = self.current
		# 현재 위치가 position보다 작은 동안 반복 (반복문 내부에서 before, current 갱신)
		while cur_pos < position:
			self.before = cur_node
			self.current = cur_node.next
			cur_pos += 1
		self.before.next = new_node
		new_node.next = self.current

		self.num_of_data += 1

	# remove 메소드 (delete2 - key와 일치하는 node 삭제, 인접 node의 current, next 변경, 데이터 개수 변경)
	def remove(self, key):
		# 처리 결과 출력을 위해 삭제된 원소 개수 카운트
		del_cnt = 0
		# 몇 번째 원소인지 알기 위해 idx 변수 선언
		idx = 0
		# 빈 리스트일 경우 메소드 종료
		if self.num_of_data == 0:
			return None
		cur_node = self.current
		# 리스트 전체 탐색 (cur_node가 None이 되면 끝까지 탐색한 것)
		while cur_node is not None:
			# 삭제할 node 발견
			if cur_node.data == key:
				# 삭제할 node가 첫 번째 node일 경우
				if cur_node is self.current:
					self.current = cur_node.next
					cur_node = self.current
				# 삭제할 node가 중간에 위치하는 경우
				else:
					self.before.next = cur_node.next
					cur_node = cur_node.next
					
				self.num_of_data -= 1
				del_cnt += 1
			# 현재 node의 값이 key와 같지 않다면, 다믐 node로 이동
			else:
				self.before = cur_node
				cur_node = cur_node.next
			idx += 1
		if del_cnt == 0:
			print("해당하는 원소가 없습니다.")
		else:
			print(f"{idx-1}번째 원소(key)를 삭제합니다.")