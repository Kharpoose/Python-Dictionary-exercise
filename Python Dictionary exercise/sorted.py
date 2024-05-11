import operator

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print('Original dictionary : ', x)

sorted_x = sorted(x.items(), key=operator.itemgetter(1))

print('Dictionary in ascending order by value : ', sorted_x)

print('Dictionary in ascending order by value : ',sorted_x)

sorted_y = dict( sorted(x.items(), key=operator.itemgetter(1), reverse=True))

print('Dictionary in descending order by value : ',sorted_y)