word = "pineapple"

# Inverting list

def inv_list(list):
    new_list = []
    size = len(list)
    print(len(list))
    for i in range(size):
        new_list.append(list[size-i-1])
    return new_list

print(inv_list(word))

"""
list = pineapple
new_list = []
size = size of 'pineapple' -> 9
for i in range (9):
    i = 0
    pineapple[9-0-1] => new_list[8]
    [1, 2, 3, 4, 5, 6, 8, 9] => positions = > [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return ['', '', '', '', '', '', '', '', p]
    i = 1
    pineapple[9-1-1] => new_list[7]
    return ['', '', '', '', '', '', '', i, p]
    .
    .
    .
['e', 'l', 'p', 'p', 'a', 'e', 'n', 'i', 'p']
"""

#====================================================================================#

# Checking for duplicates

def duplicate(list):
    for i in range(len(list)-1):
        for j in range(1+i, len(list)):
            if list[i] == list[j]:
                return True
    return False

print(duplicate(word))

"""
list = pineapple
for i in range of 9 - 1:                        [0, 1, 2, 3, 4, 5, 6, 7]
    for j in range of (0 + 1 until 9):          [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if list[0] equals to list[0 + 1]        [p] <=> [i]
            return True and end
            else continue
    if there's no duplicates, returns False

[p, i, n, e, a, p, p, l, e] <=> [i, n, e, a, p, p, l, e]
i = 0
j = 1, 2, 3, 4, 5, 6, 7, 8, 9
[p] <=> [i]
[p] <=> [n]
[p] <=> [e]
[p] <=> [a]
[p] <=> [p] => True         
[p] <=> [p]
[p] <=> [l]
[p] <=> [e]

ends
"""
#====================================================================================#

def duplicate2(list):
    dp = 0
    seen = []
    for i in range(len(list)-1):
        for j in range(1+i, len(list)):
            if list[i] == list[j] and list[i] not in seen:
                seen.append(list[j])
                dp += 1
    print(f"There are {dp} duplicate(s) letter(s) in {list}. The letters are {seen}")

print(duplicate2(word))

"""
list = pineapple
dp = 0
seen = []
for i in range of 9 - 1:                        
    for j in range of (0 + 1 until 9):          
        if list[0] equals to list[0 + 1] and list[0] isn't in [seen] 
            seen = [list[1]]
            dp = 1 + 1
        else dp = 0
    continue

[p, i, n, e, a, p, p, l, e] <=> [i, n, e, a, p, p, l, e]
i = 0
j = 1, 2, 3, 4, 5, 6, 7, 8, 9
[p] <=> [i]
[p] <=> [n]
[p] <=> [e]
[p] <=> [a]
[p] <=> [p] => True         
[p] <=> [p]
[p] <=> [l]
[p] <=> [e]
seen = [p]
dp = 0 + 1

i = 1
j = 2, 3, 4, 5, 6, 7, 8, 9
[i] <=> [n]
[i] <=> [e]
[i] <=> [a]
[i] <=> [p] => True         
[i] <=> [p]
[i] <=> [l]
[i] <=> [e]
seen = [p]
dp = 1
.
.
.
i = 3
j = 4, 5, 6, 7, 8, 9
[e] <=> [e] => True 
[e] <=> [a]
[e] <=> [p]         
[e] <=> [p]
[e] <=> [l]
[e] <=> [e]
seen = [p, e]
dp = 1 + 1
.
.
.
i = 8
j = 9
[e] <=> [e] => True
but [e] is in seen = [p, e]
dp = 2 + 0
end
"""
