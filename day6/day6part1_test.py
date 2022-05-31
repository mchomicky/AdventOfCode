data = '3,4,3,1,2'

fish = [int(x) for x in data.strip().split(',')]

for i in range(80):
    for j in range(len(fish)):
        if fish[j] > 0:
            fish[j] -= 1
        else:
            fish[j] = 6
            fish.append(8)

print(len(fish))
