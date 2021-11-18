head = int(input("Enter the head value: "))
sequence = [10, 90, 80, 40, 50, 20, 70, 89, 92, 11, 231]

#FCFS does everything in order
def FCFS(seq):
    seq.insert(0, head)
    print(sequence)
    seq.remove(head)

#SSTF does everything in an optimal way, where the nearest element is served first
def calculateDifference(queue, head, diff): 
    for i in range(len(diff)): 
        diff[i][0] = abs(queue[i] - head)

def findMin(diff):  
    index = -1
    minimum = 999999999
    for i in range(len(diff)): 
        if(not diff[i][1] and minimum > diff[i][0]): 
            minimum = diff[i][0] 
            index = i
    return index

def SSTF(request, head):
    if (len(request) == 0):  
            return
    l = len(request)  
    diff = [0] * l   
    for i in range(l):
        diff[i] = [0, 0]
    seek_sequence = [0] * (l + 1)  
    for i in range(l):  
        seek_sequence[i] = head  
        calculateDifference(request, head, diff)  
        index = findMin(diff)
        diff[index][1] = True 
        head = request[index]  
    seek_sequence[len(seek_sequence) - 1] = head
    for i in range(l + 1): 
        print(seek_sequence[i])

SSTF(sequence, head)
