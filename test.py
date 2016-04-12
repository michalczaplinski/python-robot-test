from pprint import pprint as pp

range1 = []
range2 = []

def choose_angle(l)
for index, item in enumerate(l):
    if item == 100:
        range2.append((index, item))
    elif l[index-1] == 100:
        range2.append((index, item))
    else:
        if len(range2) > len(range1):
            range1 = range2
        range2 = []

d = dict(range1)

print d.keys()
print d
print sum(d.keys()) / len(d.keys())
