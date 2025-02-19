# knapsack problem

def non_dyn_prog_knapstack(capacity, wt, profit, n, nb_calls):
    # time complexity  O(2**n)
    nb_calls[0] +=1
    if n == 0 or capacity==0:
        return 0
    curr_w = wt[n -1]
    if  curr_w> capacity:
        # not included in the optimal solution
        return non_dyn_prog_knapstack(capacity, wt, profit, n-1, nb_calls)

    else:
        return max(profit[n-1] + non_dyn_prog_knapstack(capacity - curr_w, wt, profit, n-1, nb_calls),
                    non_dyn_prog_knapstack(capacity, wt, profit, n-1, nb_calls))

profit = [60, 100, 120]
weight = [10, 20, 30]
cap = 60
n = len(profit)
nb_calls = [0]
print(non_dyn_prog_knapstack(cap, weight, profit, n, nb_calls), nb_calls, )


def dyn_rec_knapstack(capacity, wt, profit, n, memo, nb_calls):
    
    if n < 0:
        return 0
    

    if memo[n][capacity] is not None:
        return memo[n][capacity]
    nb_calls[0] += 1
    # store value in table before return
    curr_w = wt[n]
    if curr_w > capacity:
        memo[n][capacity] = dyn_rec_knapstack(capacity, wt, profit, n-1, memo, nb_calls)
    else:
        memo[n][capacity] = max(profit[n] + dyn_rec_knapstack(capacity-curr_w, wt, profit, n-1, memo, nb_calls),
        dyn_rec_knapstack(capacity, wt, profit, n-1, memo, nb_calls))
    return memo[n][capacity]

def dyn_knapstack(capacity, wt, profit, n, nb_calls):
    # time complexity O(n * w)
    memo = [[None for _ in range(capacity+1)] for _ in range(n)]
    return dyn_rec_knapstack(capacity, wt, profit, n-1, memo, nb_calls)

nb_calls = [0]
print(dyn_knapstack(cap, weight, profit, n, nb_calls), nb_calls)
