# https://cp-algorithms.com/dynamic_programming/intro-to-dp.html


# fibonaci

# f(n) = f(n-1) + f(n-2), f(1)=1 and f(0)=0
# cruntime O(2**n)

def fibonaci(n, fc_call=0):
    fc_call[0] += 1
    if n >1:
        return fibonaci(n-1, fc_call) + fibonaci(n-2, fc_call)
    elif n == 1:
        return 1
    else:
        return 0
    
fc_call = [0]  # nb of time we are going to call the function
print(fibonaci(29, fc_call), fc_call)

# speed up fibonaci with memoizing (try to decrease te number of call)
# runtime complexity O(n)


fc_call = [0]
val = 29

def fibonaci_memoizing(n, fc_call=0):
    memo = [None] * (n+1)
    return _fibonaci_memoizing(n, memo, fc_call), memo

def _fibonaci_memoizing(n, memo, fc_call=0):
    fc_call[0] += 1

    if memo[n]:
        return memo[n]
    if n  == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = _fibonaci_memoizing(n-1, memo, fc_call) + _fibonaci_memoizing(n-2, memo, fc_call)
        return memo[n]
    
print(fibonaci_memoizing(29, fc_call), fc_call)

fc_call = [0]
# bottom up dynamic programming
def fibonaci_bottom_up(n, fc_call):
    max_save = 3  # we only need to store 3 values
    memo = [None] * (max_save+1)
    memo[0] = 0
    memo[1] = 1
    print(memo)
    fc_call[0] +=1
    for i in range(2, n+1):
        memo[i%3] = memo[(i -1) %3] + memo[(i -2)%3]
    return memo[n%3]


print(fibonaci_bottom_up(29, fc_call), fc_call)




# memoization with binary search

class Job:
    def __init__(self, start, finish, profit):
        self.start = start 
        self.finish = finish 
        self.profit = profit 

def schedule(jobs):
    jobs = sorted(jobs, key=lambda j: j.start)

    n = len(jobs)
    table = [0 for _ in range(n)]
    table[0] = jobs[0].profit
    for i in range(1, n):
        inc_proof = jobs[i].profit
        l = binary_search(jobs, i)
        if (l !=-1):
            inc_proof+=table[l]
        table[i] = max(inc_proof, table[i-1])
    return table[n-1]

def binary_search(job, start_index):
    # O(logn)
    lo = 0
    hi = start_index - 1

    # Perform binary Search iteratively 
    while lo <= hi: 
        mid = (lo + hi) // 2
        if job[mid].finish <= job[start_index].start: 
            if job[mid + 1].finish <= job[start_index].start: 
                lo = mid + 1
            else: 
                return mid 
        else: 
            hi = mid - 1
    return -1

job = [Job(1, 2, 50), Job(3, 5, 20), Job(6, 19, 100), Job(2, 100, 200)] 
print("Optimal profit is")
print(schedule(job))


