import random
ang = 1
while ang != 2:
    print("Welcome to Tic Tac Toe")
    place1 = 1
    place2 = 2
    place3 = 3
    place4 = 4
    place5 = 5
    place6 = 6
    place7 = 7
    place8 = 8
    place9 = 9
    print(" ", place1, " | ", place2, " | ", place3, " ")
    print("-----------------")
    print(" ", place4, " | ", place5, " | ", place6, " ")
    print("-----------------")
    print(" ", place7, " | ", place8, " | ", place9, " ")
    mode = int(input("Select Mode of your game i.e Press 1 for single player mode and 2 for Multiplayer mode: "))
    if mode == 2 :
        print("You selected multiplayer mode")
        symbol = int(input("Player1 please choose a symbol(press 1 for x and 2 for o): "))
        if symbol == 1 :
            player1 = "x"
            player2 = "o"
        elif symbol == 2 :
            player1 = "o"
            player2 = "x"
        toss = random.randint(1, 2)
        if toss == 1:
            print(player1 , " who is player 1 wins the toss")
            z = 1
        else:
            print(player2 , " who is player 2 wins the toss")
            z = 2
            player1,player2=player2,player1
        count = 0
        while count <= 9:
                turn1 = int(input(player1+" please Enter a number between 1 to 9:"))
                if turn1 == 1 and place1 != player1 and place1 != player2 :
                    place1 = player1
                elif turn1 == 2 and place2 != player1 and place2 != player2:
                    place2 = player1
                elif turn1 == 3 and place3 != player1 and place3 != player2 :
                    place3 = player1
                elif turn1 == 4 and place4 != player1 and place4 != player2:
                    place4 = player1
                elif turn1 == 5 and place5 != player1 and place5 != player2:
                    place5 = player1
                elif turn1 == 6 and place6 != player1 and place6 != player2:
                    place6 = player1
                elif turn1 == 7 and place7 != player1 and place7 != player2:
                    place7 = player1
                elif turn1 == 8 and place8 != player1 and place8 != player2:
                    place8 = player1
                elif turn1 == 9 and place9 != player1 and place9 != player2:
                    place9 = player1
                else:
                    print("The spot is already taken!Enter again!")
                    continue
                print(" ", place1, " | ", place2, " | ", place3, " ")
                print("-----------------")
                print(" ", place4, " | ", place5, " | ", place6, " ")
                print("-----------------")
                print(" ", place7, " | ", place8, " | ", place9, " ")
                z = 1
                count += 1
                if count == 9:
                    print("Oops its a draw!")
                    break
                ########WINNING CHECK######## DUDE :P
                if (place1 == place2 == place3) or (place1 == place4 == place7) or (place4 == place5 == place6) \
                        or (place7 == place8 == place9) or (place2 == place5 == place8) or (place3 == place6 == place9) \
                        or (place1 == place5 == place9) or (place3 == place5 == place7):
                    print(player1, " wins the game")
                    break
                player1,player2=player2,player1
        start = input("press y to play a new game otherwise n to exit ")
        if start == "N" or start == "n":
            ang = 2
            print(" Thanks for playing hope you enjoyed ")
            break
        elif start == "Y" or start == "y":
            ang = 1
    elif(mode == 1):
        symbol = int(input("Player1 please choose a symbol(press 1 for x and 2 for o): "))
        if symbol == 1 :
            player1 = "x"
            computersign = "o"
        elif symbol == 2 :
            player1 = "o"
            computersign = "x"
        toss = random.randint(1, 2)
        if toss == 1:
            print(player1 , " who is player 1 wins the toss")
            computerturn=0
        else:
            print("computer wins the toss")
            z = 2
            computerturn=1
        count = 0
        while count<9:
            if(computerturn==0):
                turn1 = int(input(player1+" please Enter a number between 1 to 9:"))
                if turn1 == 1 and place1 != player1 and place1 != computersign :
                    place1 = player1
                elif turn1 == 2 and place2 != player1 and place2 != computersign:
                    place2 = player1
                elif turn1 == 3 and place3 != player1 and place3 != computersign :
                    place3 = player1
                elif turn1 == 4 and place4 != player1 and place4 != computersign:
                    place4 = player1
                elif turn1 == 5 and place5 != player1 and place5 != computersign:
                    place5 = player1
                elif turn1 == 6 and place6 != player1 and place6 != computersign:
                    place6 = player1
                elif turn1 == 7 and place7 != player1 and place7 != computersign:
                    place7 = player1
                elif turn1 == 8 and place8 != player1 and place8 != computersign:
                    place8 = player1
                elif turn1 == 9 and place9 != player1 and place9 != computersign:
                    place9 = player1
                else:
                    print("The spot is already taken!Enter again!")
                    continue
                print(" ", place1, " | ", place2, " | ", place3, " ")
                print("-----------------")
                print(" ", place4, " | ", place5, " | ", place6, " ")
                print("-----------------")
                print(" ", place7, " | ", place8, " | ", place9, " ")
            elif(computerturn==1):
                print("-------------Computer turn----------------")
                if((place2==place3==computersign)or(place4==place7==computersign)or(place5==place9==computersign)) and place1!= player1:
                    place1=computersign
                elif((place1==place3==computersign)or(place5==place8==computersign)) and place2!= player1:
                    place2=computersign
                elif((place2==place1==computersign)or(place6==place9==computersign)or(place5==place7==computersign)) and place3!= player1:
                    place3=computersign
                elif((place5==place6==computersign)or(place1==place7==computersign)) and place4!= player1:
                    place4=computersign
                elif((place4==place6==computersign)or(place2==place8==computersign) or (place1==place9==computersign) or (place3==place7==computersign)) and place5!= player1:
                    place5=computersign
                elif((place5==place4==computersign)or(place3==place9==computersign)) and place6!= player1:
                    place6=computersign
                elif((place1==place4==computersign)or(place9==place8==computersign)or(place5==place3==computersign)) and place7!= player1:
                    place7=computersign
                elif((place5==place2==computersign)or(place7==place9==computersign)) and place8!=player1:
                    place8=computersign
                elif((place8==place7==computersign)or(place5==place1==computersign) or (place6==place3==computersign)) and place9!= player1:
                    place9=computersign
                elif((place2==place3==player1)or(place4==place7==player1)or(place5==place9==player1)) and place1!= computersign:
                    place1=computersign
                elif((place1==place3==player1)or(place5==place8==player1)) and place2!= computersign:
                    place2=computersign
                elif((place2==place1==player1)or(place6==place9==player1)or(place5==place7==player1)) and place3!= computersign:
                    place3=computersign
                elif((place5==place6==player1)or(place1==place7==player1)) and place4!= computersign:
                    place4=computersign
                elif((place4==place6==player1)or(place2==place8==player1) or (place1==place9==player1) or (place3==place7==player1)) and place5!= computersign:
                    place5=computersign
                elif((place5==place4==player1)or(place3==place9==player1)) and place6!= computersign:
                    place6=computersign
                elif((place1==place4==player1)or(place9==place8==player1)or(place5==place3==player1)) and place7!= computersign:
                    place7=computersign
                elif((place5==place2==player1)or(place7==place9==player1)) and place8!=player1:
                    place8=computersign
                elif((place8==place7==player1)or(place5==place1==player1) or (place6==place3==player1)) and place9!= computersign:
                    place9=computersign
                elif(place5!=computersign and place5!=player1):
                    place5=computersign
                elif(place5==player1 and place7!=player1 and place7!=computersign):
                    place7=computersign
                elif(place5==place3==player1 and place7==computersign and place1!=computersign and place1!=player1):
                    place1=computersign
                elif(place5==computersign and ((place4==place3==player1)or(place4==place2==player1)) and place1!=computersign and place1!=player1):
                    place1=computersign
                elif(place5==computersign and ((place2==player1 and place6==player1)or(place2==place9==player1)) and place3!=computersign and place3!=player1):
                    place3=computersign
                elif(place5==computersign and ((place6==place8==player1)or(place6==place7==player1)) and place9!=computersign and place9!=player1):
                    place9=computersign
                elif(place5==computersign and ((place8==place4==player1)or(place8==place1==player1)) and place7!=computersign and place7!=player1):
                    place7=computersign
                elif(place5!=player1 and place5!=computersign):
                    place5=computersign
                elif(place2!=player1 and place2!=computersign):
                    place2=computersign
                elif(place4!=player1 and place4!=computersign):
                    place4=computersign
                elif(place6!=player1 and place6!=computersign):
                    place6=computersign
                elif(place8!=player1 and place8!=computersign):
                    place8=computersign
                elif(place1!=player1 and place1!=computersign):
                    place1=computersign
                elif(place3!=player1 and place3!=computersign):
                    place3=computersign
                elif(place7!=player1 and place7!=computersign):
                    place7=computersign
                elif(place9!=player1 and place9!=computersign):
                    place9=computersign
                print(" ", place1, " | ", place2, " | ", place3, " ")
                print("-----------------")
                print(" ", place4, " | ", place5, " | ", place6, " ")
                print("-----------------")
                print(" ", place7, " | ", place8, " | ", place9, " ")
            computerturn = not computerturn
            count += 1
            if count == 9:
                print("Oops its a draw!")
                break
            ########WINNING CHECK######## DUDE :P
            if (place1 == place2 == place3) or (place1 == place4 == place7) or (place4 == place5 == place6) \
                    or (place7 == place8 == place9) or (place2 == place5 == place8) or (place3 == place6 == place9) \
                    or (place1 == place5 == place9) or (place3 == place5 == place7):
                print(player1, " wins the game")
                break
        start = input("press y to play a new game otherwise n to exit ")
        if start == "N" or start == "n":
            ang = 2
            print(" Thanks for playing hope you enjoyed ")
            break
        elif start == "Y" or start == "y":
            ang = 1
        
