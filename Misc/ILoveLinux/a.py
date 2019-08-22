import pickle

with open('123321.pickle', 'rb') as f:

    data = pickle.load(f)

#for d in data:

#    print(d)
print(len(data))
new_data = list()

for i in range(len(data)):

    tmp = [ ' ']*100

    new_data.append(tmp)

for i, d in enumerate(data):

    for m in d:

        new_data[i][m[0]] = m[1]
        #print m;

for i in new_data:

    print(''.join(i))