num=int(input("Enter the number: "))
list=[]


while num>0:
    x=num%10
    list.append(x)
    y=num//10
    num=y

list.reverse()


a=list[0]
for i in list[1:]:
    if i>a:
        a=i

print(f'The highest digit is  {a}')