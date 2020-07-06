def aroundCenter(s, L, R):
    right= R
    left = L
    while((left>=0 and right<len(s))):
        if(s[right]==s[left]):
            right+=1
            left-=1
        else:
            break
    return right-left-1

def longestPalindrome(s):
    if(s == None or len(s)==0):
        return ""
    n = len(s)
    finalStart=0
    finalEnd=0
    for i in range(n):
        len1 = aroundCenter(s,i,i)
        len2 = aroundCenter(s,i,i+1)
        length = max(len1,len2)
        if(length>finalEnd-finalStart):
            finalStart = i-(length-1)//2
            finalEnd = i+(length//2)
    return s[finalStart:finalEnd+1]

s = input()
print(longestPalindrome(s))
