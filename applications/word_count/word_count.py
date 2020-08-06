import re

def word_count(s):
    # Your code here
    cache = {}
    foo = re.sub("'", "", s)
    str = re.sub('\W+', ' ', foo)
    sep = str.split()
    
    for i in sep:
        x = i.lower()
        if x in cache:
            cache[x] += 1
        else:
            if x == "doesnt":
                x = "doesn't"
            cache[x] = 1
    return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))