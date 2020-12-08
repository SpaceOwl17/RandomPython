for i in range (1,100000):
    
    num = (i)
    div9 = (i % 9)
    div8 = (i % 8)
    div7 = (i % 7)
    div6 = (i % 6)
    div5 = (i % 5)
    div4 = (i % 4)
    div3 = (i % 3)
    div2 = (i % 2)
    div1 = (i % 1)
    
    ans = (div9 + div8 + div7 + div6 + div5 + div4 + div3 + div2 + div1)
    
    if ans == 0:
        print(num)
    
    