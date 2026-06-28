from functools import cmp_to_key

class Job:
    def __init__(self,start,finish,profit):
        self.start = start
        self.finish = finish
        self.profit = profit


def JobComparator(s1,s2):
        return s1.finish < s2.finish
    
def latestNonConflict(arr,i):
        for j in range(i-1,-1,-1):
            if arr[j].finish <= arr[i-1].start:
                return j
        return -1
    

def findMaxProfit(arr,n):
        arr = sorted(arr,key=cmp_to_key(lambda s1,s2: s1.finish < s2.finish))
        table = [None] * n
        table[0] = arr[0].profit

        for i in range(1,n):
            incProf= arr[i].profit
            l = latestNonConflict(arr,i)
            if l != -1:
                incProf += table[l]

            table[i] = max(incProf, table[i-1])
        result = table[n-1]
        return result
    
values = [(3,10,20), (1,2,50),
          (6,19,100), (2,100,200)]
arr = []
for i in values:
    arr.append(Job(i[0],i[1],i[2]))
    
n = len(arr)
print("The optimal profit is", findMaxProfit(arr,n))