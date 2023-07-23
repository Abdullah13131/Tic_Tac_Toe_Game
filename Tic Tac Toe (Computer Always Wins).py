import random

Start_again = 1

while Start_again != 2:
    print(" HELLO AND WELCOME TO TIC TAC TOE GAME ")
    
    num_01,num_02,num_03,num_04,num_05,num_06,num_07,num_08,num_09 =1,2,3,4,5,6,7,8,9
    
    print(" ", num_01, " | ", num_02, " | ", num_03, " ")
    print("-----------------")
    print(" ", num_04, " | ", num_05, " | ", num_06, " ")
    print("-----------------")
    print(" ", num_07, " | ", num_08, " | ", num_09, " ")
    
    select_mode = int(input(" Select the mode of your game i.e, For Single Player Mode,Press 1 and For Multiplayer Mode, Press 2 : "))
    
    if select_mode == 2 :
        print(" You have selected the Multiplayer Mode ")
        
        Symbol = int(input("Player_01,Please choose your Symbol( For X,Press 1 and for O,Press 2 ) : "))
        
        if Symbol == 1 :
            Player_01 = "X"
            Player_02 = "O"
        elif Symbol == 2 :
            Player_01 = "O"
            Player_02 = "X"
            
        Toss = random.randint(1, 2)
        
        if Toss == 1:
            print(Player_01 , " Who is Player_01,Win's the Toss ")
            z = 1
        else:
            print(Player_02 , " Who is Player_02,Win's the Toss ")
            z = 2
            Player_01,Player_02=Player_02,Player_01
            
        Count = 0
        while Count <= 9:
                Turn_01 = int(input(Player_01+" Please enter a number between 1-9 : "))
                if Turn_01 == 1 and num_01 != Player_01 and num_01 != Player_02 :
                    num_01 = Player_01
                elif Turn_01 == 2 and num_02 != Player_01 and num_02 != Player_02:
                    num_02 = Player_01
                elif Turn_01 == 3 and num_03 != Player_01 and num_03 != Player_02 :
                    num_03 = Player_01
                elif Turn_01 == 4 and num_04 != Player_01 and num_04 != Player_02:
                    num_04 = Player_01
                elif Turn_01 == 5 and num_05 != Player_01 and num_05 != Player_02:
                    num_05 = Player_01
                elif Turn_01 == 6 and num_06 != Player_01 and num_06 != Player_02:
                    num_06 = Player_01
                elif Turn_01 == 7 and num_07 != Player_01 and num_07 != Player_02:
                    num_07 = Player_01
                elif Turn_01 == 8 and num_08 != Player_01 and num_08 != Player_02:
                    num_08 = Player_01
                elif Turn_01 == 9 and num_09 != Player_01 and num_09 != Player_02:
                    num_09 = Player_01
                else:
                    print(" This spot is already taken ! Please enter another number ! ")
                    continue
                
                print(" ", num_01, " | ", num_02, " | ", num_03, " ")
                print("-----------------")
                print(" ", num_04, " | ", num_05, " | ", num_06, " ")
                print("-----------------")
                print(" ", num_07, " | ", num_08, " | ", num_09, " ")
                z = 1
                Count += 1
                if Count == 9:
                    print(" The Match is Tie ! ")
                    break
                
                ########WINNING CHECK########
                
                if (num_01 == num_02 == num_03) or (num_01 == num_04 == num_07) or (num_04 == num_05 == num_06) \
                        or (num_07 == num_08 == num_09) or (num_02 == num_05 == num_08) or (num_03 == num_06 == num_09) \
                        or (num_01 == num_05 == num_09) or (num_03 == num_05 == num_07):
                    print(Player_01, " Win's this game ")
                    break
                
                Player_01,Player_02=Player_02,Player_01
                
        Start = input(" Press Y to play a new game,again otherwise, n to exit ")
        
        if Start == " N " or Start == " n ":
            Start_again = 2
            print(" Thanks for playing the game. I hope you enjoyed it! ")
            break
        elif Start == "Y" or Start == "y":
            Start_again = 1
    elif(select_mode == 1):
        Symbol = int(input(" Player_01 Please choose your Symbol( For X,Press 1 and for O,Press 2 ) : "))
        if Symbol == 1 :
            Player_01 = "X"
            Computer_Sign = "O"
        elif Symbol == 2 :
            Player_01 = "O"
            Computer_Sign = "X"
        Toss = random.randint(1, 2)
        if Toss == 1:
            print(Player_01 , " Who is Player_01, Win's the Toss ")
            Computer_Turn=0
        else:
            print(" Computer Win's the Toss ")
            z = 2
            Computer_Turn=1
        Count = 0
        
        while Count<9:
            if(Computer_Turn==0):
                Turn_01 = int(input(Player_01+" Please enter a number between 1-9 : "))
                
                if Turn_01 == 1 and num_01 != Player_01 and num_01 != Computer_Sign :
                    num_01 = Player_01
                elif Turn_01 == 2 and num_02 != Player_01 and num_02 != Computer_Sign:
                    num_02 = Player_01
                elif Turn_01 == 3 and num_03 != Player_01 and num_03 != Computer_Sign :
                    num_03 = Player_01
                elif Turn_01 == 4 and num_04 != Player_01 and num_04 != Computer_Sign:
                    num_04 = Player_01
                elif Turn_01 == 5 and num_05 != Player_01 and num_05 != Computer_Sign:
                    num_05 = Player_01
                elif Turn_01 == 6 and num_06 != Player_01 and num_06 != Computer_Sign:
                    num_06 = Player_01
                elif Turn_01 == 7 and num_07 != Player_01 and num_07 != Computer_Sign:
                    num_07 = Player_01
                elif Turn_01 == 8 and num_08 != Player_01 and num_08 != Computer_Sign:
                    num_08 = Player_01
                elif Turn_01 == 9 and num_09 != Player_01 and num_09 != Computer_Sign:
                    num_09 = Player_01
                else:
                    print(" This spot is already taken ! Please enter another number ! ")
                    continue
                
                print(" ", num_01, " | ", num_02, " | ", num_03, " ")
                print("-----------------")
                print(" ", num_04, " | ", num_05, " | ", num_06, " ")
                print("-----------------")
                print(" ", num_07, " | ", num_08, " | ", num_09, " ")
            elif(Computer_Turn==1):
                
                print("------------- Computer turn ----------------")
                
                if((num_02==num_03==Computer_Sign)or(num_04==num_07==Computer_Sign)or(num_05==num_09==Computer_Sign)) and num_01!= Player_01:
                    num_01=Computer_Sign
                    
                elif((num_01==num_03==Computer_Sign)or(num_05==num_08==Computer_Sign)) and num_02!= Player_01:
                    num_02=Computer_Sign
                    
                elif((num_02==num_01==Computer_Sign)or(num_06==num_09==Computer_Sign)or(num_05==num_07==Computer_Sign)) and num_03!= Player_01:
                    num_03=Computer_Sign
                    
                elif((num_05==num_06==Computer_Sign)or(num_01==num_07==Computer_Sign)) and num_04!= Player_01:
                    num_04=Computer_Sign
                    
                elif((num_04==num_06==Computer_Sign)or(num_02==num_08==Computer_Sign) or (num_01==num_09==Computer_Sign) or (num_03==num_07==Computer_Sign)) and num_05!= Player_01:
                    num_05=Computer_Sign
                    
                elif((num_05==num_04==Computer_Sign)or(num_03==num_09==Computer_Sign)) and num_06!= Player_01:
                    num_06=Computer_Sign
                    
                elif((num_01==num_04==Computer_Sign)or(num_09==num_08==Computer_Sign)or(num_05==num_03==Computer_Sign)) and num_07!= Player_01:
                    num_07=Computer_Sign
                    
                elif((num_05==num_02==Computer_Sign)or(num_07==num_09==Computer_Sign)) and num_08!=Player_01:
                    num_08=Computer_Sign
                    
                elif((num_08==num_07==Computer_Sign)or(num_05==num_01==Computer_Sign) or (num_06==num_03==Computer_Sign)) and num_09!= Player_01:
                    num_09=Computer_Sign
                    
                elif((num_02==num_03==Player_01)or(num_04==num_07==Player_01)or(num_05==num_09==Player_01)) and num_01!= Computer_Sign:
                    num_01=Computer_Sign
                    
                elif((num_01==num_03==Player_01)or(num_05==num_08==Player_01)) and num_02!= Computer_Sign:
                    num_02=Computer_Sign
                    
                elif((num_02==num_01==Player_01)or(num_06==num_09==Player_01)or(num_05==num_07==Player_01)) and num_03!= Computer_Sign:
                    num_03=Computer_Sign
                    
                elif((num_05==num_06==Player_01)or(num_01==num_07==Player_01)) and num_04!= Computer_Sign:
                    num_04=Computer_Sign
                    
                elif((num_04==num_06==Player_01)or(num_02==num_08==Player_01) or (num_01==num_09==Player_01) or (num_03==num_07==Player_01)) and num_05!= Computer_Sign:
                    num_05=Computer_Sign
                    
                elif((num_05==num_04==Player_01)or(num_03==num_09==Player_01)) and num_06!= Computer_Sign:
                    num_06=Computer_Sign
                    
                elif((num_01==num_04==Player_01)or(num_09==num_08==Player_01)or(num_05==num_03==Player_01)) and num_07!= Computer_Sign:
                    num_07=Computer_Sign
                    
                elif((num_05==num_02==Player_01)or(num_07==num_09==Player_01)) and num_08!=Player_01:
                    num_08=Computer_Sign
                    
                elif((num_08==num_07==Player_01)or(num_05==num_01==Player_01) or (num_06==num_03==Player_01)) and num_09!= Computer_Sign:
                    num_09=Computer_Sign
                    
                elif(num_05!=Computer_Sign and num_05!=Player_01):
                    num_05=Computer_Sign
                    
                elif(num_05==Player_01 and num_07!=Player_01 and num_07!=Computer_Sign):
                    num_07=Computer_Sign
                    
                elif(num_05==num_03==Player_01 and num_07==Computer_Sign and num_01!=Computer_Sign and num_01!=Player_01):
                    num_01=Computer_Sign
                    
                elif(num_05==Computer_Sign and ((num_04==num_03==Player_01)or(num_04==num_02==Player_01)) and num_01!=Computer_Sign and num_01!=Player_01):
                    num_01=Computer_Sign
                    
                elif(num_05==Computer_Sign and ((num_02==Player_01 and num_06==Player_01)or(num_02==num_09==Player_01)) and num_03!=Computer_Sign and num_03!=Player_01):
                    num_03=Computer_Sign
                    
                elif(num_05==Computer_Sign and ((num_06==num_08==Player_01)or(num_06==num_07==Player_01)) and num_09!=Computer_Sign and num_09!=Player_01):
                    num_09=Computer_Sign
                    
                elif(num_05==Computer_Sign and ((num_08==num_04==Player_01)or(num_08==num_01==Player_01)) and num_07!=Computer_Sign and num_07!=Player_01):
                    num_07=Computer_Sign
                    
                elif(num_05!=Player_01 and num_05!=Computer_Sign):
                    num_05=Computer_Sign
                    
                elif(num_02!=Player_01 and num_02!=Computer_Sign):
                    num_02=Computer_Sign
                    
                elif(num_04!=Player_01 and num_04!=Computer_Sign):
                    num_04=Computer_Sign
                    
                elif(num_06!=Player_01 and num_06!=Computer_Sign):
                    num_06=Computer_Sign
                    
                elif(num_08!=Player_01 and num_08!=Computer_Sign):
                    num_08=Computer_Sign
                    
                elif(num_01!=Player_01 and num_01!=Computer_Sign):
                    num_01=Computer_Sign
                    
                elif(num_03!=Player_01 and num_03!=Computer_Sign):
                    num_03=Computer_Sign
                    
                elif(num_07!=Player_01 and num_07!=Computer_Sign):
                    num_07=Computer_Sign
                    
                elif(num_09!=Player_01 and num_09!=Computer_Sign):
                    num_09=Computer_Sign
                    
                print(" ", num_01, " | ", num_02, " | ", num_03, " ")
                print("-----------------")
                print(" ", num_04, " | ", num_05, " | ", num_06, " ")
                print("-----------------")
                print(" ", num_07, " | ", num_08, " | ", num_09, " ")
                
            Computer_Turn = not Computer_Turn
            Count += 1
            if Count == 9:
                print("Th Match is Tied ! ")
                break
            
            ########WINNING CHECK########
            if (num_01 == num_02 == num_03) or (num_01 == num_04 == num_07) or (num_04 == num_05 == num_06) \
                    or (num_07 == num_08 == num_09) or (num_02 == num_05 == num_08) or (num_03 == num_06 == num_09) \
                    or (num_01 == num_05 == num_09) or (num_03 == num_05 == num_07):
                print(Player_01, " Win's the game")
                break
            
        Start = input("press y to play a new game otherwise n to eXit ")
        if Start == "N" or Start == "n":
            Start_again = 2
            print(" Thanks for playing hope you enjoyed ")
            break
        elif Start == "Y" or Start == "y":
            Start_again = 1
        
