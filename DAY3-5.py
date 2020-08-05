while True:
    print('======')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
    print('======')
    sel=input('歡迎光臨,請輸入選項:')
    sel=int(sel) 
    if sel==1:
        num=input('請輸入第一個數字:')
        num2=input('請輸入第二個數字:')
        num=int(num)
        num2=int(num2)
        ans=num+num2
        print(num,'+',num2,'=',ans)
    elif sel==2:
        num=input('請輸入第一個數字:')
        num2=input('請輸入第二個數字:')
        num=int(num)
        num2=int(num2)
        ans=num-num2
        print(num,'-',num2,'=',ans)
    elif sel==3:
        num=input('請輸入第一個數字:')
        num2=input('請輸入第二個數字:')
        num=int(num)
        num2=int(num2)
        ans=num*num2
        print(num,'x',num2,'=',ans)
    elif sel==4:
        num=input('請輸入第一個數字:')
        num2=input('請輸入第二個數字:')
        num=int(num)
        num2=int(num2)
        ans=num/num2
        print(num,'/',num2,'=',ans)
    elif sel==5:
        print('謝謝光臨')
        break
    else:
        print('對不起，請重新輸入')
    
    
    