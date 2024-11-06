# Lucas Brinks
# range practice
# 11/4/24

for i in range(1,20+1):
    print(i)
#for i in range(1,1000001):
    #print(i)
mill = [1,5,10,20,25,50,55,100,150,300,500,1200,5000,10000,50000,1000000]
for i in range(mill):
    min = min(i)
    max = max(i)
    sum = sum(i)
    print(f'''The smallest number is {min}
    The biggest number is {max}
    The sum is {sum}''')
