# largest common subsequence
# Input: s1 = “ABC”, s2 = “ACD”
# Output: 2

# Input: s1 = “AGGTAB”, s2 = “GXTXAYB”
# Output: 4

# Input: s1 = “ABC”, s2 = “CBA”
# Output: 1


# with rec (not optimimized)

def rec_common_subs(string1, string2, i1, i2, common_subs):
    if i1 == len(string1) or i2 == len(string2) :
        return 0
    if string1[i1] == string2[i2]:
        common_subs[0] +=1
        print(string1[i1])
        n_strings = rec_common_subs(string1, string2, i1+1, i2 +1, common_subs)
        n_strings +=1
    else:
        n_strings = max(rec_common_subs(string1, string2, i1+1, i2, common_subs),
            rec_common_subs(string1, string2, i1, i2+1, common_subs))
    return n_strings
import copy 
def _get_list_from_max(string1, string2, i1, i2, common_subs):
    subs1, subs2 = copy.deepcopy(common_subs), copy.deepcopy(common_subs)
    val1 = rec_common_subs(string1, string2, i1+1, i2, subs1)
    val2 = rec_common_subs(string1, string2, i1, i2+1, subs2)
    if val1> val2:
        del subs2
        return val1
    else:
        del subs1
        return val2
    
all_s1 = ["ABC", "ACD", "AGGTAB"]

all_s2 = ["ACD", "ABC", "GXTXAYB"]

print("largest common subsequence")
for s1, s2 in zip(all_s1, all_s2):
    common_subs = [0]
    print(rec_common_subs(s1, s2,0 ,0, common_subs), set(common_subs))



# with dyn prog
def _dyn_common_subs(string1, string2, i1, i2, memo, common_subs):
    if i1 == len(string1) or i2 == len(string2) :
        return 0

    if memo[i2+1][i1+1] is not None:
        return memo[i2+1][i1+1]
    if string1[i1] == string2[i2]:
        common_subs[0] += 1

        memo[i2+1][ i1+1] = _dyn_common_subs(string1, string2, i1+1, i2 +1, memo, common_subs)
        memo[i2+1][ i1+1] += 1
        
        n_strings = memo[i2+1][ i1+1]

    else:
        memo[i2][i1+1]  = max(_dyn_common_subs(string1, string2, i1+1, i2, memo, common_subs),
            _dyn_common_subs(string1, string2, i1, i2+1, memo, common_subs))
        memo[i2+1] [i1] = memo[i2][i1+1]
        n_strings = memo[i2+1][i1]
        
    return n_strings

def dyn_common_subs(string1, string2, common_subs):
    memo = [[None for _ in range(len(string1)+1)] for _ in range(len(string2)+1)]
    return _dyn_common_subs(string1, string2, 0,0, memo, common_subs)

print("with dyn prog")
for s1, s2 in zip(all_s1, all_s2):
    common_subs = [0]
    print(dyn_common_subs(s1, s2,common_subs), set(common_subs))


