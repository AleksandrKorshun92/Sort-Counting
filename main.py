#Сортировка подсчетом

list = [12,2,3,3,3,1,25,78,78,8,9,4,2,1,1,] 
a = max(list) + 1
b = [0] * a
sortlist = [] 
for i in list:
    b[i] += 1
     
for i in range(max(list) + 1):
    if b[i] > 0:
        while b[i]>0:
            sortlist.append((i))
            b[i]-=1
        
print(sortlist)