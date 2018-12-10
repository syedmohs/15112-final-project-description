import Tkinter
import random
def whoWon(player,playerI): #to check after every move if someone won
    if playerI[0]==-2 and playerI[1]==-2 and playerI[2]==-2 and playerI[3]==-2:
        return True
        
#here the logic of the game is being implemented
def logic():
    playersList= [] #List where current playing players will be added
    global mainList
    mainList=[0]*51 #mainlist is a list where esch index represents a white square in the board
    redIndex=[-1,-1,-1,-1]
    blueIndex=[-1,-1,-1,-1]
    yellowIndex=[-1,-1,-1,-1] #these are the lists of the index of each charactr of each player in the mainlist
    greenIndex=[-1,-1,-1,-1]
    global Base
    Base=[-2,-3,-4,-5,-6,-7] #list that represents final destination of a character
    
    def nextPlayer(i):
        if playersList[i]==23:
            nextPlayer=playersList[0]

        else:
            nextPlayer=playersList[i+1]
            
        return nextPlayer

    def getList(player): #takes the player as parameter and returns its respective indeces list of each charcter in the mainlist
        if player==playerR:
            return redIndex
        if player==playerB:
            return blueIndex
        if player==playerY:
            return yellowIndex
        if player==playerG:
            return greenIndex
    def playTurn(player,playerI,score): #main function that implements the turns and updates the position of the characters in the mainlist
        global Base
        global mainList
        if len(score)==1:
            print "which one,1,2,3,4 would you like to move with score",score[0] #asks for which character it wants to move with the score(score is a list)
            move=raw_input("Enter here: ")
            while move!="1"and move!="2" and move!="3" and move!="4":
                print "Invalid,try again"
                move=raw_input("Enter here again: ") #invalid input if something other than 1-4 is put in
                
            while playerI[int(move)-1]==-1:  # notifies the user that it cannot take a player out of its home without a six
                p= raw_input("sorry your character is not out of the house, write 'choose other' to choose another one or press quit if you have no option: " )
                if "quit"in p.lower():
                    return 
                else:
                    move=raw_input("Enter here: ")
            while abs(int(move))>4:
                print "invalid, try again"
                move=raw_input("Enter here: ")
            while playerI[abs(int(move))-1]==-2: # here if the users character has already exited the game then the user is notified that it cannot move a cahrcater that has exited the game
                move=raw_input("character has moved out, choose other: ")
            if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[0]>int(end[player]): #this prevetns the charater form moving past its final destination with the score
                d= playerI[abs(int(move))-1]+score[0]
                e= abs(int(end[player])- d)
                mainList[playerI[int(move)-1]]-=player #removes character from main list
                Base[e-1]=player #and adds it to the base list(final destination)
                playerI[abs(int(move))-1]=-2
                print "base:", Base
                print "mainlist ", mainList
                
            else:
                mainList[playerI[int(move)-1]]-=player # if character is able to move then updates its pisiton in the mainlist this process is repeated.
                playerI[abs(int(move))-1]+=score[0] 
                playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%51
                mainList[playerI[int(move)-1]]+=player
            if whoWon(player,playerI):
                print player,"you won"
            print "mainList:",mainList
        #the previous process is also implemented similarly when the score is moret than 1 element
        if len(score)==2: #means got a six and some other score
            print "which one do u want to move with score",score[0]
            move=raw_input("Enter here: ")
            while move!="1"and move!="2" and move!="3" and move!="4": #checking for invalid input again same as vefore
                print "Invalid,try again"
                move=raw_input("Enter here again: ")
                

            while abs(int(move))>4:
                print "invalid move, try again"
                move=raw_input("Enter here: ")
            while playerI[abs(int(move))-1]==-2:
                move=raw_input("character has moved out, choose other: ")
            if playerI[abs(int(move))-1]==-1: #now the first score is obviously a six and if the player chooses a character in its home then it can be taken out 
                playerI[abs(int(move))-1]=int(start[player]) 
                mainList[playerI[abs(int(move))-1]]+=player
            elif playerI[abs(int(move))-1]!=-1:
                if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[0]>int(end[player]): #this prevetns the charater form moving past its final destination with the score
                    d= playerI[abs(int(move))-1]+score[0]
                    e= abs(int(end[player])- d)
                    mainList[playerI[int(move)-1]]-=player
                    Base[e-1]=player #removes character from main list
                    playerI[abs(int(move))-1]=-2
                    print "base:", Base
                    print "mainlist,: ",mainList
    
                else:
                    mainList[playerI[int(move)-1]]-=player
                    playerI[abs(int(move))-1]+=score[0]
                    playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%51
                    mainList[playerI[int(move)-1]]+=player
            print "okay now think about your second score: ",score[1] #rest of the s[rocess is same as when you have score other than 6
            move=raw_input("Enter the character you would like to move,1,2,3, or 4 here: ")
            while move!="1"and move!="2" and move!="3" and move!="4":
                print "Invalid,try again"
                move=raw_input("Enter here again: ")
            while playerI[abs(int(move))-1]==-2:
                move=raw_input("character has moved out, choose other: ")
                

            while playerI[int(move)-1]==-1:
                p= raw_input("sorry your character is not out of the house,choose another one or press next if you have no option: " )
                if "quit"in p.lower():
                    return
                else:
                    move=raw_input("Enter here: ")
            while abs(int(move))>4:
                print "invalid, try again"
                move=raw_input("Enter here: ")
            while playerI[abs(int(move))-1]==-2:
                move=raw_input("character has moved out, choose other: ")
            if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[1]>int(end[player]):
                d= playerI[abs(int(move))-1]+score[0]
                e= abs(int(end[player])- d)
                mainList[playerI[int(move)-1]]-=player
                Base[e-1]=player
                playerI[abs(int(move))-1]=-2
                print "base:", Base
                print "mainList:",mainlist
            else:
                mainList[playerI[int(move)-1]]-=player
                playerI[abs(int(move))-1]+=score[1]
                playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%51
                mainList[playerI[int(move)-1]]+=player
            if whoWon(player,playerI):
                print player,"you won"
            print "mainList:",mainList
        if len(score)==3: #here you have a 6,6 and a score other than a 6
            print "which one do u want to move with score",score[0]
            move=raw_input("Enter here: ")
            while move!="1"and move!="2" and move!="3" and move!="4":
                print "Invalid,try again"
                move=raw_input("Enter here again: ")
                

            while abs(int(move))>4:
                print "invalid move, try again"
                move=raw_input("Enter here: ")
            while playerI[abs(int(move))-1]==-2:
                move=raw_input("character has moved out, choose other: ")
            if playerI[abs(int(move))-1]==-1:
                playerI[abs(int(move))-1]=int(start[player])
                mainList[playerI[abs(int(move))-1]]+=player
            elif playerI[abs(int(move))-1]!=-1:
                if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[0]>int(end[player]):
                    d= playerI[abs(int(move))-1]+score[0]
                    e= abs(int(end[player])- d)
                    mainList[playerI[int(move)-1]]-=player
                    Base[e-1]=player
                    playerI[abs(int(move))-1]=-2
                    print "base:", Base
                    print "mainList:",mainlist
                else:
                    mainList[playerI[int(move)-1]]-=player
                    playerI[abs(int(move))-1]+=score[0]
                    playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%51
                    mainList[playerI[int(move)-1]]+=player
            print "okay now think about your second score: ",score[1]
            move=raw_input("Enter the character you would like to move,1,2,3, or 4 here: ")
            while move!="1"and move!="2" and move!="3" and move!="4":
                print "Invalid,try again"
                move=raw_input("Enter here again: ")
                

            while abs(int(move))>4:
                print "invalid move, try again"
                move=raw_input("Enter here: ")
            while playerI[abs(int(move))-1]==-2:
                move=raw_input("character has moved out, choose other: ")
            if playerI[abs(int(move))-1]==-1:
                playerI[abs(int(move))-1]=int(start[player])
                mainList[playerI[abs(int(move))-1]]+=player
            elif playerI[abs(int(move))-1]!=-1:
                if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[1]>int(end[player]):
                    d= playerI[abs(int(move))-1]+score[0]
                    e= abs(int(end[player])- d)
                    mainList[playerI[int(move)-1]]-=player
                    Base[e-1]=player
                    playerI[abs(int(move))-1]=-2
                    print "base:", Base
                    print "mainList:",mainList
                else:
                    mainList[playerI[int(move)-1]]-=player
                    playerI[abs(int(move))-1]+=score[1]
                    playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%51
                    mainList[playerI[int(move)-1]]+=player
            print "okay now think about your third score: ",score[2]
            move=raw_input("Enter the character you would like to move,1,2,3, or 4 here: ")
            while move!="1"and move!="2" and move!="3" and move!="4":
                print "Invalid,try again"
                move=raw_input("Enter here again: ")
                
            while playerI[abs(int(move))-1]==-2:
                move=raw_input("character has moved out, choose other: ")
            while playerI[int(move)-1]==-1:
                p= raw_input("sorry your character is not out of the house,choose another one or press next if you have no option: " )
                if "quit"in p.lower():
                    return
                else:
                    move=raw_input("Enter here: ")
            while abs(int(move))>4:
                print "invalid, try again"
                move=raw_input("Enter here: ")
            while playerI[abs(int(move))-1]==-2:
                move=raw_input("character has moved out, choose other: ")
            if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[2]>int(end[player]):
                d= playerI[abs(int(move))-1]+score[0]
                e= abs(int(end[player])- d)
                mainList[playerI[int(move)-1]]-=player
                Base[e-1]=player
                playerI[abs(int(move))-1]=-2
                print "base:", Base
                print "mainList:",mainlist
            else:
                mainList[playerI[int(move)-1]]-=player
                playerI[abs(int(move))-1]+=score[2]
                playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%51
                mainList[playerI[int(move)-1]]+=player
            if whoWon(player,playerI):
                print player,"you won"
            print "mainList:",mainList
            
            
            
            
            
            
            
            
                
                
                
            




    #################------------Main Code------------------#####################
    wnd.destroy() #this the code that asks for input then calls the main playerTurn function
    print mainList
    inp= raw_input("Choose from player 1,2,3 or 4 or type Next to continue: ")
    Rcheck=False
    Bcheck=False
    Ycheck=False
    Gcheck=False
    playersCount=0
    playerR=None
    playerB=None
    playerY=None
    playerG=None
    start={13:"0",17:"39",19:"26",23:"13"}
    end={13:"50",17:"37",19:"24",23:"11"}

    while "next" not in inp.lower() and playersCount<=4:
        if int(inp)==1 and Rcheck==False: #as the playerws choose their playeres, the players are added into the playersList
            print "you are red"
            Rcheck=True
            playersCount+=1
            playerR= 13
            playersList.append(playerR)
        elif int(inp)==2 and Bcheck==False:
            print "you are blue"
            Bcheck=True
            playersCount+=1
            playerB=17
            playersList.append(playerB)
        elif int(inp)==3 and Ycheck==False:
            print "you are yellow"
            Ycheck=True
            playersCount+=1
            playerY=19
            playersList.append(playerY)
        elif int(inp)==4 and Gcheck==False:
            print "you are green"
            Gcheck=True
            playersCount+=1
            playerG=23
            playersList.append(playerG)
        else:
            print "Invalid input, try again"
        inp=raw_input("Choose from player 1,2,3 or 4 or type 'Next' to continue: ")
        


    play=raw_input("write 'PLAY' to play or write 'QUIT': " )
    while play.lower()!="quit":
        for player in playersList:
            myList=getList(player)
            print "Its the turn of: ",player # this part finds out the score and appends it in a list then asks for the user input on how the player wanats to use their score
            score=[]
            print "rolling dice..."
            roll= random.randint(1,6)
            print "dice: ", roll
            countSix=0
            done = True
            while done and len(score) <= 3:
                if roll!=6:
                    done= False
                    score.append(roll)
                    print "your score is : ",score
                elif roll==6:
                    score.append(roll)
                    while roll==6 and countSix<3 :  
                        print "you got six, roll again"
                        countSix+=1
                        print "rolling dice..."
                        roll=random.randint(1,6)
                        print "dice: ", roll
                        score.append(roll)
                        print "your score: ",score
                    done=False
            if countSix==3:
                return
            print "now that you know your score, time to make a move"
            playTurn(player,myList,score)
def quitGame(): #quit game function
    wnd.destroy()


def instructions(): #part of gui where instructions pop up when you press the instructions button
    global wnd3
    wnd3=Tkinter.Toplevel()
    wnd3.title("Instructions")
    wnd3.geometry("600x600")
    image2=Tkinter.PhotoImage(file="inst.gif")
    c1=Tkinter.Canvas(wnd3,width=900,height=900,bg="white")
    c1.create_image((300,300),image=image2)
    c1.pack()
    wnd3.mainloop()
    
def startScreen(): #start screen gui
    global wnd
    wnd= Tkinter.Tk()
    wnd.title("Start Screen")
    image= Tkinter.PhotoImage(file="wall.gif")
    w=image.width()
    h=image.height()
    x=200
    y=50
    wnd.geometry("%dx%d+%d+%d" % (w, h, x, y))
    panel = Tkinter.Label(wnd,text="LUDO", image=image)
    panel.pack(side='top', fill='both', expand='yes')
    lab = Tkinter.Label(panel,text="LUDO",font=("Helvetica", 100, "bold italic"),foreground ="Green",background="Black")
    btn1 = Tkinter.Button(panel, text='Start New Game',width=15,height=1,font=("Helvetica", 10, "bold italic"),foreground ="Yellow",background="Black",command=logic) #this is the start game button that plays the game(calls the logic part of the game)
    btn2 = Tkinter.Button(panel, text='Instructions',width=15,height=1,font=("Helvetica", 10, "bold italic"),foreground ="Yellow",background="Black",command=instructions)#button for instructons
    btn4 = Tkinter.Button(panel, text='Quit',width=15,height=1,font=("Helvetica", 10, "bold italic"),foreground ="Yellow",background="Black",command=quitGame) #button to quit game
    lab.pack()
    btn1.pack()
    btn2.pack()
    btn4.pack()
    wnd.mainloop()

startScreen()                       

