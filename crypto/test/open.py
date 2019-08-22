import collections
f=open('tit.txt','r')
print(collections.Counter(f.read()))