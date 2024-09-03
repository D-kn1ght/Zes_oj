
def check(s):
    for i in range(1,len(s)):
        if 2<=abs(s[i]-s[i-1])<=4:
            pass
        else:
            return False
    return True