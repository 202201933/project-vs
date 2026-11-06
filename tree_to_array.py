class Node:
    def __init__(self, key): #생성자
        self.key = key #노드 생성
        self.left = None
        self.right = None


def tree_to_array(root): 
    if root is None: #루트가 없으면 트리가 none
        return []

    array = [] #값을 넣을 배열 생성
    queue = [((root,0))] #초기값을 큐에 집어넣음

    while queue: #큐에 값이 없어질때까지
        node, index = queue.pop(0) #큐에서 빼서 노드와 인덱스에 각각 넣자

        if index >= len(array): #인덱스가 배열길이보다 크거나 같으면 배열을 확장해야함
            array.extend([None] * (index - len(array) + 1)) #부족한 길이만큼 None을 채워서 배열을 확장

            array[index] = node.key #해당 인덱스 위치에 노드값 저장

            if node.left:
                queue.append((node.left, 2*index + 1))
            if node.right:
                queue.append((node.right, 2*index + 2))

    return array

binary_tree_root = Node(1)
binary_tree_root.left = Node(2)
binary_tree_root.right = Node(3)
binary_tree_root.left.left = Node(4)
binary_tree_root.left.right = Node(5)
binary_tree_root.right.left = Node(6)
binary_tree_root.right.right = Node(7)

array_representation = tree_to_array(binary_tree_root)
print(array_representation)