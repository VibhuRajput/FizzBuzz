answer=[]
for i in range(1,101):
    s=""
    if(i%3==0):
        s+= "fizz"
    if(i%5==0):
        s+="buzz"
    if(i%3!=0 and i%5!=0):
        s=i
    answer.append(s)
for i in answer:
    print(i)
