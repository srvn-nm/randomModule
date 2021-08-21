import random
random.seed(2)
print('seed method: ',random.random(),'\n')
print('getstate method: ',random.getstate(),'\n')
# trying setstate method
print(random.random(),'\n')
state = random.getstate()
print(random.random(),'\n')
random.setstate(state)
print('setstate method: ',random.random(),'\n')
print('getrandbits method: ', random.getrandbits(8),'\n')
print('randrage method: ',random.randrange(3,9),'\n')
print('randint method: ',random.randint(3,9),'\n')
# trying choice method
mylist = ['apple','banana','cherry']
print('choice method: ',random.choice(mylist),'\n')
# trying choices method
print('choices method: ',random.choices(mylist,weights = [10,1,1], k = 14),'\n')
# trying shuffle method
random.shuffle(mylist)
print('shuffle method: ',mylist,'\n')
# trying sample method
print('sample method: ',random.sample(mylist, k = 2),'\n')
print('random method: ',random.random(),'\n')
print('uniform method: ', random.uniform(20,60),'\n')
print('triangular method: ',random.triangular(20,60,30),'\n')
print('betavariate method: ',random.betavariate(20.0,60.0),'\n')
print('gammavariate method: ',random.gammavariate(20.0,60.0),'\n')
print('gauss method: ',random.gauss(20.0,60.0),'\n')
print('lognormvariate method: ',random.lognormvariate(20.0,60.0),'\n')
print('normalvariate method: ',random.normalvariate(20.0,60.0),'\n')
print('vonmisesvariate method: ',random.vonmisesvariate(20.0,60.0),'\n')
print('paretovariate method: ',random.paretovariate(60.0),'\n')
print('weibullvariate method: ',random.weibullvariate(20.0,60.0),'\n')

