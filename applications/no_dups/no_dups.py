

def no_dups(s):
    # Your code here
    cache = {}
    if s == "":
        return ""
    str = s.split()
    for i in str:
        if i not in cache:
            cache[i] = 1
        else:
            cache[i] += 1
    
    newlist = []
    for i in cache.keys():
        if i is not None:
            newlist.append(i)
    str1 = " ".join(newlist)
    return str1



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))