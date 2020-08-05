w={}
while True:
    print('1.建立詞彙')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗')
    print('6.離開')
    d=input('請輸入選項:')
    d=int(d)
    if d==1:
        e=input('請輸入英文:')
        c=input('請輸入中文:')
        w[e]=c
    elif d==2:
        print(w)
    elif d==3:
        t=input('請輸入英文:')
        if t in w:
            ans=w[t]
            print(ans)
        else:
            print('沒有這個單字')
    elif d==4:
        f=input('請輸入中文:')
#        ans=
        print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    #elif ip==2:
        
     