## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre
    # Case 1 : 헤드 앞에 삽입 (다현, 화사)
    if (head.data == findData) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # Case 2 : 중간 노드에 삽입 (사나, 솔라)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # Case 3 : 없는 노드 앞에 삽입==마지막 노드에 추가(재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(delData) :
    global memory, head, current, pre
    # Case 1 : 헤드를 삭제할 때 (다현)
    if (head.data == delData) :
        current = head
        head = head.link
        del(current)
        return
    # Case 2 : 중간 노드를 삭제할 때 (쯔위)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == delData) :
            pre.link = current.link
            del(current)
            return
    # Case 3 : 없는 노드 삭제 (재남)
    return

def  findNode(findData) :
    global memory, head, current, pre
    current = head
    if (current.data == findData) :
        return current
    while (current.link != None) :
        current = current.link
        if (current.data == findData) :
            return current
    return Node()

## 변수
memory=[]
head, current, pre = None, None, None
dataAry = ['다현', '정연', '쯔위', '사나', '지효'] # 여러분의 데이터

## 메인

node = Node()  # 첫 노드
node.data = dataAry[0]
head = node
memory.append(node)

for data in dataAry[1:] : # ['정연', '쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

# insertNode('다현', '화사')
# printNodes(head)
# insertNode('사나', '솔라')
# printNodes(head)
# insertNode('재남', '문별')
# printNodes(head)

# deleteNode('다현')
# printNodes(head)
# deleteNode('쯔위')
# printNodes(head)
# deleteNode('재남')
# printNodes(head)

retData = findNode('쯔위')
print(retData.data, ' 뮤비가 나옵니다.. 쿵짝쿵짝')