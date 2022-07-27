import numpy as np
import random
import math
import matplotlib.pyplot as plt

class nsga2():
    def __init__(self):
        print('Hello , welcome to my program')

    def check_range(self,x):
        if x>=0 and x<=1: #R
            return 1
        return 0
        if x >= 1 and x <= 5: #Rt
            return 1
        return 0
        if x >= 10 and x <= 30: #D
            return 1
        return 0
        if x >= 20 and x <= 50: #E
            return 1
        return 0
    def __input__(self,n):
        temperature = np.array([])
        rain = np.array([])
        humidity = np.array([])
        soil = np.array([])
        for i in range(0, n):
            temperature = np.append(temperature, random.randint(0, 1))
            temperature = np.append(temperature, random.randint(1, 5))
            temperature = np.append(temperature, random.randint(10, 30))
            temperature = np.append(temperature, random.randint(20, 50))
        for i in range(0, n):
            rain = np.append(rain, random.randint(0, 1))
            rain = np.append(rain, random.randint(1, 5))
            rain = np.append(rain, random.randint(10, 30))
            rain = np.append(rain, random.randint(20, 50))
        for i in range(0, n):
            humidity = np.append(humidity, random.randint(0, 1))
            humidity = np.append(humidity, random.randint(1, 5))
            humidity = np.append(humidity, random.randint(10, 30))
            humidity = np.append(humidity, random.randint(20, 50))
        for i in range(0, n):
            soil = np.append(soil, random.randint(0, 1))
            soil = np.append(soil, random.randint(1, 5))
            soil = np.append(soil, random.randint(10, 30))
            soil = np.append(soil, random.randint(20, 50))
        return temperature, rain, humidity, soil

    def norm(self,x,arr):
        return (x-min(arr))/(max(arr)-min(arr))

    def sol(self,arr,population):
        rep = np.array([])
        rt = np.array([])
        e = np.array([])
        dis = np.array([])
        for i in range(0, population.size, 4):
            rep = np.append(rep, population[i])
        for i in range(1, population.size, 4):
            rt = np.append(rt, population[i])
        for i in range(2, population.size, 4):
            e = np.append(e, population[i])
        for i in range(3, population.size, 4):
            dis = np.append(dis, population[i])
        x = (self.norm(arr[0], rep))
        n = x
        y = 0
        y += (self.norm(arr[1], rt))
        y += (self.norm(arr[2], e))
        y += (self.norm(arr[3], dis))
        z = y
        x += (1/y)
        return x,n,z

    def services(self,arr,population):
        outp = np.array([])
        outy = np.array([])
        outz = np.array([])
        for i in range(0,arr.size,4):
            curr = np.array([])
            for j in range(i,i+4):
                curr = np.append(curr,arr[j])
            x,y,z=self.sol(curr,population)
            outp = np.append(outp, x)
            outy = np.append(outy, y)
            outz = np.append(outz, z)
        return outp,outy,outz

    def setPop(self,arr1,arr2,arr3,arr4):
        population = np.array([])
        for i in arr1:
            population = np.append(population, i)
        for i in arr2:
            population = np.append(population,i)
        for i in arr3:
            population = np.append(population,i)
        for i in arr4:
            population = np.append(population,i)
        return population
    def where(self,arr,x):
        for i in range(0,arr.size):
            if x== arr[i]:
                return i
        return -1

    def CA(self,arr1,arr2,arr3,arr4):
        population = self.setPop(arr1, arr2, arr3, arr4)
        arrS,a,b = self.services(arr1,population)
        arrT,n,d = self.services(arr2,population)
        arrH,e,f = self.services(arr3,population)
        arrR,g,h = self.services(arr4,population)
        res= np.array([])
        popo = np.array([])
        for i in range(0,int(arrS.size/4)):
            x3 = max(arrS)
            c = self.where(arrS, x3)
            popo = np.append(popo, a[c])
            popo = np.append(popo, b[c])
            arrS = np.delete(arrS, c)
            a = np.delete(a, c)
            b = np.delete(b, c)

            x4 = max(arrT)
            c = self.where(arrT, x4)
            popo = np.append(popo, n[c])
            popo = np.append(popo, d[c])
            arrT = np.delete(arrT, c)
            n = np.delete(n, c)
            d = np.delete(d, c)

            x2 = max(arrH)
            c = self.where(arrH, x2)
            popo = np.append(popo, e[c])
            popo = np.append(popo, f[c])
            arrH = np.delete(arrH, c)
            e = np.delete(e, c)
            f = np.delete(f, c)

            x1 = max(arrR)
            c = self.where(arrR, x1)
            popo = np.append(popo, g[c])
            popo = np.append(popo, h[c])
            arrR = np.delete(arrR, c)
            g = np.delete(g, c)
            h = np.delete(h, c)

            res = np.append(res, x3)
            res = np.append(res, x4)
            res = np.append(res, x2)
            res = np.append(res, x1)

            for k in range(0,10):
                popo = np.append(popo,random.randint(0,10)%2)
        return popo

    def init_pop(self,n):
        temperature = np.array([])
        rain = np.array([])
        humidity = np.array([])
        soil = np.array([])
        temperature, rain, humidity, soil = self.__input__(n)
        newpop = self.CA(temperature,rain,humidity,soil)
        return newpop



    def crossover1(self,newpop):
        arr = np.array([])
        for i in range(0,newpop.size):
            arr = np.append(arr,newpop[i])
        for i in range(0,int(newpop.size/18),2):
            ccc = random.randint(1, 20)%3
            x1 = ccc * 2
            x2 = ((ccc+1)%3) * 2

            a,b = arr[i*18 + x1],arr[i*18 + x1+1]
            arr[i*18 + x1],arr[i*18 + x1+1]=arr[(i+1)*18 + x1],arr[(i+1)*18 + x1+1]
            arr[(i+1)*18 + x1],arr[(i+1)*18 + x1+1] = a,b

            a,b = arr[i*18 + x2],arr[i*18 + x2+1]
            arr[i*18 + x2],arr[i*18 + x2+1]=arr[(i+1)*18 + x2],arr[(i+1)*18 + x2+1]
            arr[(i+1)*18 + x2],arr[(i+1)*18 + x2+1]= a,b

        for i in range(0,newpop.size):
            newpop = np.append(newpop,arr[i])
        return newpop

    def obj_rep(self,arr):
        x = 0
        for i in range(0, arr.size, 2):
            x += arr[i]
        return x

    def obj_of(self,arr):
        x = 0
        for i in range(1, arr.size, 2):
            x += arr[i]
        return x

    def obj_ind(self, population):
        indc = 0
        for i in range(population.size-10,population.size):
            indc += population[i]
        return indc/10


    def fitness(self,serviceComp):
        x1 = self.obj_of(serviceComp)
        x2 = self.obj_rep(serviceComp)
        x3 = self.obj_ind(serviceComp)
        return (1/(x1+x3))+x2

    def checking(self,rep1,rep2,fac1,fac2):
        if rep1 > rep2 and fac1 > fac2:
            return 1
        if rep1 > rep2 and fac1 >= fac2:
            return 1
        if rep1 >= rep2 and fac1 > fac2:
            return 1
        if rep1 < rep2 and fac1 < fac2:
            return -1
        if rep1 < rep2 and fac1 <= fac2 :
            return -1
        if rep1 <= rep2 and fac1 < fac2:
            return -1
        return 0

    def sortNonDominated(self,population):
        index = np.array([])
        domination = np.array([])
        for i in range(0,int(population.size/18)):
            index = np.append(index,int(i))
            domination = np.append(domination,int(i))
        repu = np.array([])
        factors = np.array([])
        for i in range(0, population.size, 18):
            subarr = np.array([])
            for j in range(i, i + 18):
                subarr = np.append(subarr, population[j])
            x = self.obj_rep(subarr)
            y = self.obj_ind(subarr)+self.obj_of(subarr)
            repu = np.append(repu, x)
            factors = np.append(factors, y)


        for i in range(0,index.size - 1):
            for j in range(i+1,index.size):
                a = self.checking(repu[i],repu[j],factors[i],factors[j])
                if a == -1:
                    index[i],index[j]=index[j],index[i]
                    domination[i],domination[j]=domination[j],domination[i]
                if a == 0:
                    domination[i]=domination[j]
        return index,domination

    def crowdingDistance(self,population,index,dominations):
        distance = np.array([])
        for i in range(0,dominations.size):
            distance = np.append(distance,0)
        maxrep = 0
        minrep = 999999
        maxof= 0
        minof = 999999
        for i in range (0, population.size, 18):
            for j in range(i*18,i*18 + 8,2):
                maxrep = max(maxrep, population[i])
                minrep = min(minrep, population[i])
        for i in range (1, population.size,2):
            for j in range(i * 18 + 1, i * 18 + 8, 2):
                maxof = max(maxof,population[i])
                minof = min(minof,population[i])

        for i in range(0,index.size-1):
            val = 1
            for j in range(i+1,index.size):
                if dominations[i]==dominations[j]:
                    val += 1
                else:
                    break
            if val == 1:
                distance[i] = 99999
            elif val == 2:
                distance[i] = 99999
                distance[i + 1] = 99999
            else:
                distance[i] = 99999
                distance[i + val - 1] = 99999
                for k in range(i+1,val-1):
                    repa=0
                    ofa=0
                    repc=0
                    ofc=0
                    for s in range(index[k-1]*18,index[k-1]*18 + 8,2):
                        repa += population[int(s)]
                    for s in range(index[k-1]*18 + 1,index[k-1]*18 + 8,2):
                        ofa += population[s]
                    for s in range(index[k+1]*18,index[k+1]*18 + 8,2):
                        repc += population[s]
                    for s in range(index[k+1]*18 + 1,index[k+1]*18 + 8,2):
                        ofc += population[s]
                    distance[k] = math.sqrt(math.pow(((repa-repc)/(maxrep-minrep)),2)+ math.pow(((ofa-ofc)/(maxof-minof)),2))
                for k in range(i,i+val-1):
                    for kk in range(i,i+val):
                        if distance[k]<distance[kk]:
                            distance[k],distance[kk] = distance[kk],distance[k]
                            index[k],index[kk] = index[kk],index[k]
        return index


    def fronts(self,pop):
        newrepu = np.array([])
        newfactors = np.array([])
        for i in range(0, pop.size,18):
            c = np.array([])
            for j in range(i,i+18):
                c = np.append(c,pop[j])
            newrepu = np.append(newrepu, self.obj_rep(c))
            newfactors = np.append(newfactors, (1/(self.obj_of(c)+self.obj_ind(c))))

        plt.scatter(newrepu, newfactors, c='r', marker='o', s=25)
        plt.xlabel('Reputation')
        plt.ylabel('Other Factors')
        plt.show()

    def prepareGen(self,index,pop):
        newpop = np.array([])
        for i in range(0,int(index.size / 2)):
            for j in range(int(index[i]*18),int(index[i]*18 + 18)):
                newpop = np.append(newpop,pop[int(j)])
        return newpop

    def mutation(self,population):
        for i in range(8, population.size, 18):
            x = random.randint(0, 9) % 3
            if x == 2:
                for j in range(i + x * 3, i + 10):
                    if population[i] == 0:
                        population[i] = 1
                    else:
                        population[i] = 0
            else:
                for j in range(i + x * 3, i + (x + 1) * 3):
                    if population[i] == 0:
                        population[i] = 1
                    else:
                        population[i] = 0
        return population

    def crossover2(self,newpop):
        arr = np.array([])
        for i in range(0, newpop.size):
            arr = np.append(arr, newpop[i])
        for i in range(0, int(newpop.size/18), 2):
            ccc = random.randint(1, 20) % 3
            x1 = ccc * 2
            x2 = ((ccc + 1) % 3) * 2

            a, b = arr[i * 18 + x1], arr[i * 18 + x1 + 1]
            arr[i * 18 + x1], arr[i * 18 + x1 + 1] = arr[(i + 1) * 18 + x1], arr[(i + 1) * 18 + x1 + 1]
            arr[(i + 1) * 18 + x1], arr[(i + 1) * 18 + x1 + 1] = a, b

            a, b = arr[i * 18 + x2], arr[i * 18 + x2 + 1]
            arr[i * 18 + x2], arr[i * 18 + x2 + 1] = arr[(i + 1) * 18 + x2], arr[(i + 1) * 18 + x2 + 1]
            arr[(i + 1) * 18 + x2], arr[(i + 1) * 18 + x2 + 1] = a, b
        for i in range(8, newpop.size, 36):
            x = random.randint(0, 9) % 3
            if x == 2:
                for j in range(i + x * 3, i + 10):
                    arr[i],arr[i+18]= arr[i+18],arr[i]
            else:
                for j in range(i + x * 3, i + (x + 1) * 3):
                    arr[i],arr[i+18]= arr[i+18],arr[i]
        for i in range(0, newpop.size):
            newpop = np.append(newpop, arr[i])
        return newpop