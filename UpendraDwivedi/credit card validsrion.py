a=['0','1','2','3','4','5','6','7','8','9','-']
for i in range(int(input())):
    b=input()
    c=[]
    d=[]
    for i in range(len(b)):
        if b[i].isdigit():
            c.append(b[i])
            
    if len(c)!=16:
        print("invalid")
    
    else:
        if b[0]=='4' or b[0]=='5' or b[0]=='6': #validating first character
            for i in b:
                if i not in b:
                    print("invalid")
                else:                                                #validation condition 2
                    d.append(i)
                    count=1
                    l=""
                    if len(d)==len(b):
                        for i in range(len(d)):
                            if d[i]=='-':
                                if (i+1)%5!=0:
                                    l="invalid"
                        if l=="invalid":
                            print("inavalid")
                        else:                                       #if all valid then c will enter for further validation
                            g=""

                            for i in range(len(c)-1):
                                f=c[i]
                                if f == c[i+1]:
                                    count=count+1
                                    if count==4:
                                        g="invalid"
                                        print("invalid")
                                else:
                                    count=1
                            if g=="":
                                print("valid")
                           
                                    
                        
        else:
            print("invalid")
