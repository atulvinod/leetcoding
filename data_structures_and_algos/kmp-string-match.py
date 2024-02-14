'''
 LPS: Longest Proper Prefix Length
 here LPS[i] defines the maximum K, where string of length K from start and end is the same
'''
def prepareLPS(pattern:str):
    lps = [0]*len(pattern)
    for i in range(1, len(pattern)):
        '''
            index of the longest value matched upto now
        '''
        j = lps[i-1]

        '''
            go to the first matched value until we hit 0th index, which implicitly has no matched value
        '''
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]

        '''
            if we are at the matched value , the increment the value at j, as we are assuming that
            the array is one-indexed, this will also refer to the matched index as well
        '''
        if pattern[i] == pattern[j]:
            j+=1
        lps[i] = j

    return lps


print(prepareLPS("abcdabc"))

def searchPattern(string:str, pattern:str):
    i,j=0,0
    lps = prepareLPS(pattern)
    while i < len(string):
        '''
            if the pattern has matched, the increment both j and i
        '''
        if string[i] == pattern[j]:
            j += 1
        else:
            '''
                if the pattern has not matched, then we check if j is at a non zero location,
                if it is, we go to the last matched position of j
            '''
            if j != 0:
                j = lps[j-1]
        if j == len(pattern):
            return i-len(pattern)
        i += 1
    return -1


# print(searchPattern("atulvivnod","viv"))

