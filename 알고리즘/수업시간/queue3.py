## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear == SIZE-1) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인

enQueue('화사')
enQueue('솔라')
# enQueue('문별')
# enQueue('휘인')
# enQueue('선미') # 원더걸스 원년 멤버
print('출구<--', queue, '<--입구')

# enQueue('재남')
# print('출구<--', queue, '<--입구')

retData = deQueue()
print('식사손님 : ', retData)
retData = deQueue()
print('식사손님 : ', retData)
print('출구<--', queue, '<--입구')

retData = deQueue()
print('식사손님 : ', retData)