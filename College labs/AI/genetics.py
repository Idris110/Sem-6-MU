import random

# y = random.randint(0,25)
# print(y)
chromo = [
    ['c1', 'c2', 'c3', 'c4', 'c5', 'c6'],
    [2,4,6,16,18,11],
    [12,21,8,7,4,19]
]

def genetic_gen(chromo):
    # fitness calci for f = x1^2 + x2
    fitness = []
    for i in range(len(chromo[0])):
        x1 = chromo[1][i]
        x2 = chromo[2][i]
        f = (x1**2) + x2
        print('f',i+1,'=',f)
        fitness.append(f)

    chromo.append(fitness)
    print(chromo)

    totalfitness = sum(fitness)
    avgfitness = totalfitness/len(fitness)

    prob = []
    for i in range(len(chromo[0])):
        prob.append((chromo[3][i]/totalfitness)*100)
    chromo.append(prob)


    print(chromo)
    totalprob = sum(prob)
    print('Chromosome\tX1\tX2\tFitness\tProbability')
    for i in range(len(chromo[0])):
        print(chromo[0][i],'\t\t',chromo[1][i],'\t',chromo[2][i],'\t',chromo[3][i],'\t',chromo[4][i])

    print('Total Fitness = ',totalfitness)
    print('Average Fitness = ',avgfitness)
    print('Total Probability = ',totalprob,'%',sep='')

    # find the max prob
    # maxprob = max(prob)
    # indexprob = prob.index(maxprob)
    # print('Max Probability = ',maxprob,'%',sep='')
    # print('Max Probability Chromosome = ',chromo[0][indexprob])

    # find top 2 max prob
    maxprob = max(prob)
    indexprob = prob.index(maxprob)
    print('Max Probability = ',maxprob,'%',sep='')
    print('Max Probability Chromosome = ',chromo[0][indexprob])

    tp = prob.copy()
    tp.remove(maxprob)
    maxprob2 = max(tp)

    indexprob2 = prob.index(maxprob2)
    print('2nd Max Probability = ',maxprob2,'%',sep='')
    print('2nd Max Probability Chromosome = ',chromo[0][indexprob2])

    cumprob = []
    sums = 0
    for i in range(len(chromo[0])):
        sums = sums + prob[i]
        cumprob.append(sums)

    print(cumprob)

    ranges = [[cumprob[indexprob2-1],cumprob[indexprob]], [chromo[0][indexprob2],chromo[0][indexprob]]]

    print('\n\nRANDOM NUMBERS')
    x= len(chromo[0])

    rand = []
    for i in range(x):
        rand.append(random.uniform(ranges[0][0],ranges[0][1]))


    print(rand)
    print(ranges)
    cnt=0
    for i in rand:
        if i>=ranges[0][0] and i <= cumprob[indexprob2]:
            chromo[0][cnt] = ranges[1][0]
            chromo[1][cnt] = chromo[1][indexprob2]
            chromo[2][cnt] = chromo[2][indexprob2]
        else:
            chromo[0][cnt] = ranges[1][1]
            chromo[1][cnt] = chromo[1][indexprob]
            chromo[2][cnt] = chromo[2][indexprob]

        cnt+=1

    # print chromo again
    print('Chromosome\tX1\tX2')
    for i in range(len(chromo[0])):
        print(chromo[0][i],'\t\t',chromo[1][i],'\t',chromo[2][i])


    crossprob = .3
    swapvalue = [[chromo[1][indexprob2], chromo[2][indexprob2]], [chromo[1][indexprob], chromo[2][indexprob]]]


    print(swapvalue)

    # generate 6 random using 

    for i in range(len(chromo[0])):
        rand = random.uniform(0,1)
        if rand <= crossprob:
            print('crosss' , i+1)
            if chromo[1][i] == swapvalue[0][0]:
                chromo[2][i] = swapvalue[0][1]
            else:
                chromo[2][i] = swapvalue[1][1]


    print("after crossover")
    print('Chromosome\tX1\tX2')
    for i in range(len(chromo[0])):
        print(chromo[0][i],'\t\t',chromo[1][i],'\t',chromo[2][i])


    # mutation

    mutationprob = .25

    totalmutation = int(mutationprob*len(chromo[0])*2)
    print('total mutation = ',totalmutation)

    mutate = []
    for i in range(totalmutation):
        rand = random.randint(0,len(chromo[0])*2-1)
        mutate.append(rand)

    print('mutations = ',mutate)

    maxx1 = 21
    maxx2 = 26

    for i in mutate:
        if i < len(chromo[0]):
            chromo[1][i] = maxx1-1-chromo[1][i]
        else:
            chromo[2][i-len(chromo[0])] = maxx2-1-chromo[2][i-len(chromo[0])]

    print("after mutation")
    print('Chromosome\tX1\tX2')
    for i in range(len(chromo[0])):
        print(chromo[0][i],'\t\t',chromo[1][i],'\t',chromo[2][i])
    

    print('=====================================================\n\n')
    return chromo



x = genetic_gen(chromo)
chname= 1
for i in range(len(x[0])):
    print(i)
    x12 = chname -1
    x[0][x12]= 'c'+str(chname)
    chname+=1

print(x)
    
u=genetic_gen(x)