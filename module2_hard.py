import random
Rebus = random.randint(3, 20)
print('ISHODNOYE=', Rebus)


Arraykey = []
k = 1
while k<Rebus/2 :
    for i in range(k, Rebus):
        if (Rebus%(k+i) == 0) and (k!=i):
            Arraykey.append(str(k))
            Arraykey.append(str(i))
    k=k+1
print(Arraykey)

string = ''
for j in Arraykey:
    string += j
print(string)