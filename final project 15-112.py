import random
playersList= []
mainList=[0]*51
redIndex=[-1,-1,-1,-1]
blueIndex=[-1,-1,-1,-1]
yellowIndex=[-1,-1,-1,-1]
greenIndex=[-1,-1,-1,-1]
Base=[-2,-3,-4,-5,-6,-7]

def ifSomeoneWon():
    return

    
def nextPlayer(i):
    if playersList[i]==23:
        nextPlayer=playersList[0]

    else:
        nextPlayer=playersList[i+1]
        
    return nextPlayer

def getList(player):
    if player==playerR:
        return redIndex
    if player==playerB:
        return blueIndex
    if player==playerY:
        return yellowIndex
    if player==playerG:
        return greenIndex
def playTurn(player,playerI,score):
    if len(score)==1:
        print "which one,1,2,3,4 would you like to move with score",score[0]
        move=raw_input("Enter here: ")
        while playerI[int(move)-1]==-1:
            p= raw_input("sorry your character is not out of the house, write 'choose other' to choose another one or press quit if you have no option: " )
            if "quit"in p.lower():
                return 
            else:
                move=raw_input("Enter here: ")
        while abs(int(move))>=4:
            print "invalid, try again"
            move=raw_input("Enter here: ")
        if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[0]>int(end[player]):
            d= abs(score[0]-(abs(51-(playerI[abs(int(move))-1]))))
            playerI[abs(int(move))-1]+=d
            mainList[playerI[abs(int(move)-1)]]+=player
            e=score[0]-d
            Base[e]=(abs(base[e])+base[e])+player
            
            
            
            
            
            
        else:
            mainList[playerI[int(move)-1]]-=player
            playerI[abs(int(move))-1]+=score[0]
            playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%52
            mainList[playerI[int(move)-1]]+=player
        print "mainList:",mainList
    if len(score)==2:
        print "which one do u want to move with score",score[0]
        move=raw_input("Enter here: ")
        while abs(int(move))>=4:
            print "invalid move, try again"
            move=raw_input("Enter here: ")
        if playerI[abs(int(move))-1]==-1:
            playerI[abs(int(move))-1]=int(start[player]) 
            mainList[playerI[abs(int(move))-1]]+=player
        elif playerI[abs(int(move))-1]!=-1:
            if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[0]>int(end[player]):
                d= abs(score[0]-(abs(51-(playerI[abs(int(move))-1]))))
                playerI[abs(int(move))-1]+=d
                mainList[playerI[abs(int(move)-1)]]+=player
                e=score[0]-d
                Base[e]=(abs(base[e])+base[e])+player
            else:
                mainList[playerI[int(move)-1]]-=player
                playerI[abs(int(move))-1]+=score[0]
                playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%52
                mainList[playerI[int(move)-1]]+=player
        print "okay now think about your second score: ",score[1]
        move=raw_input("Enter the character you would like to move,1,2,3, or 4 here: ")
        while playerI[int(move)-1]==-1:
            p= raw_input("sorry your character is not out of the house,choose another one or press next if you have no option: " )
            if "quit"in p.lower():
                return
            else:
                move=raw_input("Enter here: ")
        while abs(int(move))>=4:
            print "invalid, try again"
            move=raw_input("Enter here: ")
        if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[1]>int(end[player]):
            
            d= abs(score[0]-(abs(51-(playerI[abs(int(move))-1]))))
            playerI[abs(int(move))-1]+=d
            mainList[playerI[abs(int(move)-1)]]+=player
            e=score[0]-d
            Base[e]=(abs(base[e])+base[e])+player
        else:
            mainList[playerI[int(move)-1]]-=player
            playerI[abs(int(move))-1]+=score[1]
            playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%52
            mainList[playerI[int(move)-1]]+=player
        print "mainList:",mainList
    if len(score)==3:
        print "which one do u want to move with score",score[0]
        move=raw_input("Enter here: ")
        while abs(int(move))>=4:
            print "invalid move, try again"
            move=raw_input("Enter here: ")
        if playerI[abs(int(move))-1]==-1:
            playerI[abs(int(move))-1]=int(start[player])
            mainList[playerI[abs(int(move))-1]]+=player
        elif playerI[abs(int(move))-1]!=-1:
            if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[0]>int(end[player]):
                d= abs(score[0]-(abs(51-(playerI[abs(int(move))-1]))))
                playerI[abs(int(move))-1]+=d
                mainList[playerI[abs(int(move)-1)]]+=player
                e=score[0]-d
                Base[e]=(abs(base[e])+base[e])+player
            else:
                mainList[playerI[int(move)-1]]-=player
                playerI[abs(int(move))-1]+=score[0]
                playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%52
                mainList[playerI[int(move)-1]]+=player
        print "okay now think about your second score: ",score[1]
        move=raw_input("Enter the character you would like to move,1,2,3, or 4 here: ")
        while abs(int(move))>=4:
            print "invalid move, try again"
            move=raw_input("Enter here: ")
        if playerI[abs(int(move))-1]==-1:
            playerI[abs(int(move))-1]=int(start[player])
            mainList[playerI[abs(int(move))-1]]+=player
        elif playerI[abs(int(move))-1]!=-1:
            if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[1]>int(end[player]):
                d= abs(score[0]-(abs(51-(playerI[abs(int(move))-1]))))
                playerI[abs(int(move))-1]+=d
                mainList[playerI[abs(int(move)-1)]]+=player
                e=score[0]-d
                Base[e]=(abs(base[e])+base[e])+player
            else:
                mainList[playerI[int(move)-1]]-=player
                playerI[abs(int(move))-1]+=score[1]
                playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%52
                mainList[playerI[int(move)-1]]+=player
        print "okay now think about your third score: ",score[2]
        move=raw_input("Enter the character you would like to move,1,2,3, or 4 here: ")
        while playerI[int(move)-1]==-1:
            p= raw_input("sorry your character is not out of the house,choose another one or press next if you have no option: " )
            if "quit"in p.lower():
                return
            else:
                move=raw_input("Enter here: ")
        while abs(int(move))>=4:
            print "invalid, try again"
            move=raw_input("Enter here: ")
        if playerI[abs(int(move))-1]<int(end[player]) and playerI[abs(int(move))-1]+score[2]>int(end[player]):
            d= abs(score[0]-(abs(51-(playerI[abs(int(move))-1]))))
            playerI[abs(int(move))-1]+=d
            mainList[playerI[abs(int(move)-1)]]+=player
            e=score[0]-d
            Base[e]=(abs(base[e])+base[e])+player
        else:
            mainList[playerI[int(move)-1]]-=player
            playerI[abs(int(move))-1]+=score[2]
            playerI[abs(int(move))-1]=playerI[abs(int(move))-1]%52
            mainList[playerI[int(move)-1]]+=player
        print "mainList:",mainList
        
        
        
        
        
        
        
        
            
            
            
        




#################------------Main Code------------------#####################
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

while "Next" not in inp:
    if int(inp)==1 and Rcheck==False:
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
    


play=raw_input("write 'PLAY' to playo or write 'QUIT': " )
while play.lower()!="Quit":
    for player in playersList:
        myList=getList(player)
        print "Its the turn of: ",player
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
                while roll==6 and countSix<=3 :
                    score.append(roll)
                    print "you got six, roll again"
                    countSix+=1
                    print "rolling dice..."
                    roll=random.randint(1,6)
                    print "dice: ", roll
                    score.append(roll)
                    print "your score: ",score
                done=False
        if countSix==3:
            print "turn cancelled, you got three sixes"
            player=nextPlayer[player]
        print "now that you know your score, time to make a move"
        playTurn(player,myList,score)
            

    
