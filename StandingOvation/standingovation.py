def numFriends(s):
    lst = s.split()
    num = int(lst[0])
    audience = [int(x) for x in lst[1]]
    add = total = 0
    for s in range(num+1):
        if s > total and audience[s] > 0:
            add += s - total
            total += s - total
        total += audience[s]
    return add

i = int(raw_input())
for _i in range(1,i+1):
    print "Case #%d:" % _i, numFriends(raw_input())
