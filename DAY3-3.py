names=[]
scores=[]
highest=0
lowest=100
avg=0
total=0
x=input('輸入全班人數:')
x=int(x)
def abc(x,total):
    avg = total/x
    return avg 
for i in range(x):
    names.insert(i,input('輸入你的名字:'))
    scores.insert(i,int(input('輸入你的分數:')))
    total=total+scores[i]
avg = abc(x,total)
print('班平均:',avg)
#def awd():
#    awd=


for y in range(x):
    num=int(scores[y])
    if int(num)>int(highest):
        highest=scores[y]
    else:
        highest=int(highest)
print(y)    
#print('班上最高分:',highest,'分')
#for w in range(x):
#    num=int(scores[w])
#    if int(num)<int(lowest):
#        lowest=scores[w]
#    else:
#        lowest=int(lowest)
#print('班上最低分:',lowest,'分')