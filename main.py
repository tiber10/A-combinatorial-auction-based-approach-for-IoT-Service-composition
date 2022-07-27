import numpy as np
import random
import math
import matplotlib.pyplot as plt
import nsga2


pop = nsga2()
x = input('Enter the number of required generations ')
n = input('Enter the size of population ')

population = np.array([])
population = pop.init_pop(int(n))
print('\n')
print('-------------------------------------')
print('After combinatorial auction selection')
print('-------------------------------------')
for i in range(0, population.size, 18):
    print("============= Service Comp ",end=' ')
    print((i/18)+1,end=' ')
    print('===================')
    for j in range(i, i + 18):
        print(population[j], end=' ')
    print('\n')

for O in range(0,int(x)):
    newpop = pop.crossover1(population)
    print('-------------------------------------')
    print('The Population PT')
    print('-------------------------------------')
    for i in range(18*6, newpop.size, 18):
        print("============= Service Comp ", end=' ')
        print((i / 18) -5, end=' ')
        print('===================')
        for j in range(i, i + 18):
            print(newpop[j], end=' ')
        print('\n')

    print('-------------------------------------')
    print('The Off_Spring Population')
    print('-------------------------------------')
    for i in range(0, newpop.size, 18):
        print("============= Service Comp ", end=' ')
        print((i / 18) +1, end=' ')
        print('===================')
        for j in range(i, i + 18):
            print(newpop[j], end=' ')
        print('\n')
    index, domin = pop.sortNonDominated(newpop)
    newind = pop.crowdingDistance(newpop, index, domin)
    preppop = pop.prepareGen(newind, newpop)
    popafMu = pop.mutation(preppop)
    print('-------------------------------------')
    print('The Population after MUTATION')
    print('-------------------------------------')
    for i in range(0, popafMu.size, 18):
        print("============= Service Comp ", end=' ')
        print((i / 18) + 1, end=' ')
        print('===================')
        for j in range(i, i + 18):
            print(popafMu[j], end=' ')
        print('\n')
    lastgen = pop.crossover2(popafMu)
    pop.fronts(lastgen)
    print('-------------------------------------')
    print('The Population PT')
    print('-------------------------------------')
    for i in range(18 * 6, lastgen.size, 18):
        print("============= Service Comp ", end=' ')
        print((i / 18) - 4, end=' ')
        print('===================')
        for j in range(i, i + 18):
            print(lastgen[j], end=' ')
        print('\n')

    print('-------------------------------------')
    print('The Off_Spring Population')
    print('-------------------------------------')
    for i in range(0, lastgen.size, 18):
        print("============= Service Comp ", end=' ')
        print((i / 18) + 1, end=' ')
        print('===================')
        for j in range(i, i + 18):
            print(lastgen[j], end=' ')
        print('\n')
    lastind, lastdomin = pop.sortNonDominated(lastgen)
    lastnewind = pop.crowdingDistance(lastgen, lastind, lastdomin)
    print('-----------------------------------------------')
    print('The BEST Services Compositions after domination')
    print('-----------------------------------------------')
    for i in lastind:
        print(i, end=' ')
    print('\n')
    print('-----------------------------------------------')
    print('The list of DOMINATIONS')
    print('-----------------------------------------------')
    for i in lastdomin:
        print(i, end=' ')
    print('\n')

    res = pop.prepareGen(lastnewind, lastgen)
    print('-------------------------------------')
    print('best service composition in this generation is ')
    for i in range(0,18):
        print(res[i],end=' ')
    population = res

out = np.array([])
for i in range(8,18):
    out=np.append(out,int(res[i]))

output = np.array([[32,32,32,32,32]])
rng = 0
todo = 0
for i in range(1,11):
    curr = np.array([])
    for j in range(0,5):
        if j%2 == 1 and i%2 == 1:
            if out[rng] == 0:
                curr = np.append(curr, 37)
            else:
                curr = np.append(curr, 10)
            rng += 1
        elif i%2 == 1:
            curr = np.append(curr,0)
        else:
            curr = np.append(curr,32)
    output = np.append(output,[curr],axis = 0)
print(output.size)
plt.imshow(output)
plt.colorbar()
plt.show()

#newind = pop.crowdingDistance(newpop,index,domin)
#print(index)




''' def init_pop(self):
            temperature = np.array([])
            rain = np.array([])
            humidity = np.array([])
            soil = np.array([])
            indicators = np.array([])
            temperature,rain,humidity,soil,indicators = Qos.__input__()
            population = np.array([])
            for i in range(0,25,5):
                curr = np.array([])
                for j in range(i, i + 5):
                    curr = np.append(curr, temperature[j])
                for j in range(i,i+5):
                    curr = np.append(curr,rain[j])
                for j in range(i,i+5):
                    curr = np.append(curr,humidity[j])
                for j in range(i,i+5):
                    curr = np.append(curr,soil[j])
                population = np.append(population,curr)
        return population'''

'''    
    def preprocess(pop):
        srtPop = np.array([])
        serComp = 6
        sizPop = serComp*16
        reputations = np.array([])
        otherfactors = np.array([])
        for i in range(0,sizPop,16):
            curr = np.array([])
            for j in range(i,i+16):
                curr = np.append(curr,pop[i])
            reputations = np.append(reputations,obj_rep(curr))
            otherfactors = np.append(otherfactors,obj_rt(curr))
        return reputations,otherfactors

    def sortNonDominated(population):
        index = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        repu = np.array([])
        factors = np.array([])
        for i in range(0,population.size,26):
            subarr = np.array([])
            for j in range(i,i+26):
                subarr = np.append(subarr,population[j])
            x,y = obj_fun(subarr)
            repu = np.append(repu,x)
            factors = np.append(factors,y)
        for i in range(0,repu.size):
            for j in range(i+1,repu.size):
                if repu[i]==repu[j]:
                    if factors[j]<factors[i]:
                        x = index[i]
                        index[i] = index[j]
                        index[j] = x

                elif repu[j]>repu[i]:
                    x = index[i]
                    index[i] = index[j]
                    index[j] = x
        return index

    def crowdingdistance(repu,factors,x):
        index =  fast_non_dominated_sort(repu,factors)
        choosed = np.array([])
        newrepu = np.array([])
        newfactors = np.array([])
        for i in range(0,x):
            choosed = np.append(choosed,index[i])
        return choosed

    def selection(rep,fac,param):
        index = crowdingdistance(rep,fac)
'''

'''
def obj_electricity(arr):
    x = 0
    for i in range(1,10):
        x += arr[i]
    return min(x)

def obj(obj_rep,obj_rt,obj_energy,obj_distance):
    for i in range (0,25):
     service1= obj_rep+obj_rt+obj_energy+obj_distance
     return service1
    for i in range(0, 25):
        service2 = obj_rep + obj_rt + obj_energy + obj_distance
        return service2
    for i in range(0, 25):
        service3 = obj_rep + obj_rt + obj_energy + obj_distance
        return service3
    for i in range(0, 25):
        service4 = obj_rep + obj_rt + obj_energy + obj_distance
        return service4
'''
''''
 if x >= 10 and x <= 30: #Electricty
     return 1
 return 0
 '''
''''
   def solution_I(self):
       I= []
       x=0
       y=1
       for i in range(0, 30):
           if (i == 0 or i == 5 or i == 10 or i == 15):
               I.append(random.randint(0,1)) #R
           if (i == 1 or i == 6 or i == 11 or i == 16): #RT
               I.append(random.uniform(0.001, 5))
           if (i == 2 or i == 7 or i == 12 or i == 17): #E
               I.append(random.randint(10, 100))
           if (i == 3 or i == 8 or i == 13 or i == 18): #E
               I.append(random.randint(0, 100))
           if (i == 4 or i == 9 or i == 14 or i == 19): #D
               I.append(random.randint(10, 100))
           for i in range (20,30):
               I.append(random.randint(0,1))
               if (i==0):
                   print('the indicator is close');
               else:
                   print('the indicator is open');
       return I
       '''
'''for i in range(0, 24):
            if self.check_range(temperature[i])!=1:
                print('False value of rep')
            if self.check_range(temperature[i+1])!=5:
                print('False value of RT')
            if self.check_range(temperature[i+2])!=50:
                print('False value of energy')
            if self.check_range(temperature[i+3])!=30:
                print('False value of distance')

        for i in range(0,24):
            if self.check_range(rain[i]) != 1:
                print('False value of rep')
            if self.check_range(rain[i + 1]) != 5:
                print('False value of RT')
            if self.check_range(rain[i + 2]) != 50:
                print('False value of energy')
            if self.check_range(rain[i + 3]) != 30:
                print('False value of distance')

        for i in range(0,24):
            if self.check_range(humidity[i]) != 1:
                print('False value of rep')
            if self.check_range(humidity[i + 1]) != 5:
                print('False value of RT')
            if self.check_range(humidity[i + 2]) != 50:
                print('False value of energy')
            if self.check_range(humidity[i + 3]) != 30:
                print('False value of distance')

        for i in range(0,24):
            if self.check_range(soil[i]) != 1:
                print('False value of rep')
            if self.check_range(soil[i + 1]) != 5:
                print('False value of RT')
            if self.check_range(soil[i + 2]) != 50:
                print('False value of energy')
            if self.check_range(soil[i + 3]) != 30:
                print('False value of distance')'''


