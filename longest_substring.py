from itertools import count


def len_of_longest_substring(s):
    front = 0
    back = 0
    counter = 0
    while front != len(s):
        c = s[front]
        if c not in s[back:front]:
            front += 1
            counter = front - back if front - back > counter else counter
        else:
            while c in s[back:front]:
                back += 1
    
    return counter
        
        
            






print(len_of_longest_substring("ohvhjdml"))