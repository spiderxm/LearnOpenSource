print("\t\t\t\twelcome to uptech")
print("what you want to do-:\nwe have calculator\nwe have dice game")
print("for calculator type calc(first number,second number)\nfor dice game type dice()")
def calc(a,b):
    ch=input("enter the operation you want to do-:")
    if ch=='+':
        return a+b
    elif ch=='-':
       return a-b
    elif ch=='*':
        return a*b
    elif ch=='/':
        return a/b
    else:
        return """operation doesn't exist"""
def dice():
    import random
    import time
    print("\t\t**************DICE & ROLL GAME***************")
    print("write NEW for new game \n write exit to exit the game")
    CH=input("write your option:")
    while(CH=="NEW"):
        print("do you want to continue")
        ch=input("type Y for yes and N for no")
        
        while(ch=='Y'):
            player=random.randint(1,6)
            print("you rolled......")
            time.sleep(2)
            print("you rolled"+str(player))

            ai=random.randint(1,6)
            print("computer rolls......")
            time.sleep(2)
            print("computer rolls"+str(ai))
            print("do you want to continue")
            ch=input("type Y for yes and N for no")
            if(ch=='N'):
                exit()
            if(player>ai):
                print("you win")
                print("do you want to continue")
                ch=input("type Y for yes and N for no")
                if(ch=='N'):
                    exit()

            if(player<ai):
                print("you loose")
                print("do you want to continue")
                ch=input("type Y for yes and N for no")
                if(ch=='N'):
                    exit()

                while(ch=='Y'):
                    player=random.randint(1,6)
                    print("you rolled......")
                    time.sleep(2)
                    print("you rolled"+str(player))

                    ai=random.randint(1,6)
                    print("computer rolls......")
                    time.sleep(2)
                    print("computer rolls"+str(ai))
                    if(player>ai):
                        print("you win")
                        print("do you want to continue")
                        ch=input("type Y for yes and N for no")
                        if(ch=='N'):
                            exit()

            if(player<ai):
                print("you loose")
                print("do you want to continue")
                ch=input("type Y for yes and N for no")
                if(ch=='N'):
                    exit()
                    while(player==ai):
                        print("its tie")
                        print("continue")
                        time.sleep(3)
                        player=random.randint(1,6)
                        print("you rolled......")
                        time.sleep(4)
                        print("you rolled"+str(player))

                        ai=random.randint(1,6)
                        print("computer rolls......")
                        time.sleep(4)
                        print("computer rolls"+str(ai))
                        if(player>ai):
                            print("you win")
                        if(player<ai):
                            print("you loose")
                        print("do you want to continue")
                        ch=input("type Y for yes and N for no")
                        if(ch=='N'):
                            exit()
            

        


        while(player==ai):
            print("its tie")
            print("continue")
            time.sleep(3)
            player=random.randint(1,6)
            print("you rolled......")
            time.sleep(4)
            print("you rolled"+str(player))

            ai=random.randint(1,6)
            print("computer rolls......")
            time.sleep(4)
            print("computer rolls"+str(ai))
            if(player>ai):
                print("you win")
            if(player<ai):
                print("you loose")
            print("do you want to continue")
            ch=input("type Y for yes and N for no")
            while(ch=='Y'):
                player=random.randint(1,6)
                print("you rolled......")
                time.sleep(2)
                print("you rolled"+str(player))

                ai=random.randint(1,6)
                print("computer rolls......")
                time.sleep(2)
                print("computer rolls"+str(ai))
                if(player>ai):
                    print("you win")
                    print("do you want to continue")
                    exit()

                if(player<ai):
                    print("you loose")
                    print("do you want to continue")
                    ch=input("type Y for yes and N for no")
                if(ch=='N'):
                    exit()
                while(player==ai):
                    print("its tie")
                    print("continue")
                    time.sleep(3)
                    player=random.randint(1,6)
                    print("you rolled......")
                    time.sleep(4)
                    print("you rolled"+str(player))

                    ai=random.randint(1,6)
                    print("computer rolls......")
                    time.sleep(4)
                    print("computer rolls"+str(ai))
                    if(player>ai):
                        print("you win")
                    if(player<ai):
                        print("you loose")
                
                print("do you want to continue")
                ch=input("type Y for yes and N for no")
                if(ch=='N'):
                    exit()
        while(ch=='N'):
            break
        

        


        

