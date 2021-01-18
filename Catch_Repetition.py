t=int(input())
for i in range(t):
    s=input()
    ptr_dbba=-1
    start_ptr=0
    for j in range(1,len(s)):
        if(ptr_dbba>0):
            if(s[j]==s[(start_ptr)%ptr_dbba]):
                start_ptr+=1
            else:
                ptr_dbba = -1
                start_ptr = 0
        elif(s[j]==s[start_ptr]):
            ptr_dbba = j
            start_ptr+=1
    if(ptr_dbba>0):
        print(s[0:ptr_dbba])
    else:
        print("No repetitive pattern")
        
       
'''#Input
3
abab
abcabccabcabcc
a

#Output
ab
abcabcc
No repetitive pattern'''
