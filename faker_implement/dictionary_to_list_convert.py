"""
x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
output:  [ 'a', 1, 'b',  2, 'c', 3, 'd', 4]
"""

x = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
l = []


def create_list(new_list):
    for (key, val) in new_list.items():
        l.append(key)
        l.append(val)
    return l


# final_list = create_list(x)
final_list = create_list(d)
print(final_list)

