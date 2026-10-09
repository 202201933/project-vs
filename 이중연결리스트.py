class DListNode:
    def __init__(self, data):
        self.data = data
        self.llink = None
        self.rlink = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data):
        newnode = DListNode(data) #새로운 노드 생성
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.rlink = self.head
            self.head.llink = newnode #새 노드의 오른쪽 링크가 헤드 가리킴
            self.head = newnode #헤드를 뉴 노드로 변경
        return newnode
        
    def insert_last(self, data):
        newnode = DListNode(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.rlink = newnode
            newnode.llink = self.tail
            self.tail = newnode
        return newnode
        
    def insert_after(self,target_value,data):
        target = self.search(target_value) #서치함수로 타겟찾음
        if target is None: #타겟이 없으면 None
            print("타겟 없음")
            return None
        
        newnode = DListNode(data) #뉴노드 생성
        newnode.llink = target #타겟노드 다음 삽입 -> 뉴노드의 왼쪽링크에 타겟 주소가 있음
        newnode.rlink = target.rlink #타겟의 오른쪽링크 = 기존 타겟 다음에 있던 노드의 주소 -> 뉴노드의 오른쪽링크

        if target.rlink is not None: #기존 타겟 다음에 있던 노드가 있으면
            target.rlink.llink = newnode #그 노드의 왼쪽 링크를 뉴노드와 연결(중간에 삽입하라는 뜻)
        else: #꼬리라면 마지막 삽입
            self.tail = newnode
        target.rlink = newnode #뉴노드의 주소는 타겟의 오른쪽링크에
        return newnode

    def delete_first(self):
        if self.head is None:
            print("리스트 비어있음")
            return None

        remove = self.head.data
        if self.head == self.tail: #노드가 1개뿐
            self.head = None
            self.tail = None
        else:
            self.head = self.head.rlink
            self.head.llink = None
        return remove

    def delete_last(self):
        if self.tail is None:
            print("리스트 비어있음")
            return None

        remove = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.llink
            self.tail.rlink = None
        return remove

    def delete(self,target_value):
        target = self.search(target_value)
        if target is None: #없을떄
            return None
        
        if target == self.head: #헤드일때
            return self.delete_first()
        if target == self.tail: #테일일때
            return self.delete_last()
        #중간일때
        target.llink.rlink = target.rlink
        target.rlink.llink = target.llink
        return target.data

    def search(self,target):
        curr = self.head
        while curr is not None: #헤드가 None일때 멈춤
            if curr.data == target:
                return curr
            curr = curr.rlink
        return None

    def print_forward(self):
        curr = self.head
        result = []
        while curr is not None:
            result.append(str(curr.data))
            curr = curr.rlink
        print(" <-> ".join(result))

    def print_backward(self):
        curr = self.tail
        result = []
        while curr is not None:
            result.append(str(curr.data))
            curr = curr.llink
        print(" <-> ".join(result))


L = DoublyLinkedList()

L.insert_first(20)
L.insert_first(10)
L.insert_last(30)
L.insert_last(40)

print("Forward:")
L.print_forward()

print("Backward:")
L.print_backward()

L.insert_after(20,25) # 20값을 가진 노드 뒤에 삽입

print("After insert:")
L.print_forward()

L.delete_first()
L.delete_last()
L.delete(25)

print("After delete:")
L.print_forward()

node = L.search(30)

if node is not None:
    print("Found:",node.data)
else:
    print("Not found")
    
        
