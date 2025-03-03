a_set=set(['python', "java", 'c#'])
b_set=set(["acb,bcd,bcd","qwer"])
a_set.update(b_set)
print(a_set)
a_set.remove("c#")
'c#'
print (a_set)


list=[1,2,3,4,5,6,7,8,9]
sum=0
for i in list:
    sum=sum+i
print("sum is ",sum)
list.insert(3,9)
print(list)
list[len(list):]=[23]
list1=list
print(list)
list.extend(list1)
print(list)
list.pop(3)
list.remove(3)
print(list)
list.sort(key=None,reverse=False)

print(list)

print(list.index(23))