# PyDoKu - A python based Sudoku solver
# https://github.com/Saket-Upadhyay/pydoku
import numpy as np
import colorama
from colorama import Fore, Style
global board
global count 
count=0
board=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

boardrefmap=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

def possible(x,y,e):
    global board
    for i in range(9):
        if board[x][i] == e:
            return False
    for i in range(9):
        if board[i][y] == e:
            return False
    xs=(x//3)*3
    ys=(y//3)*3

    for i in range(0,3):
        for j in range(0,3):
            if board[xs+i][ys+j] == e:
                return False
    return True

def solver():
    global count
    global board
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] == int(0):
                for e in range(1,10):
                    if possible(i,j,e) :
                        board[i][j] = e
                        solver()
                        board[i][j] = int(0)
                return
    print("POSSIBLE SOLUTION "+str(count+1)+"> ")
    count+=1
    showboard(board)

def initdefmap():
    global board
    global boardrefmap
    for i in range(9):
        for j in range(9):
            boardrefmap[i][j] =0
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                boardrefmap[i][j] = 1


def showboard(b):
    print(" ------------------------------------- ")
    for i in range(9):
        for j in range(9):
            if boardrefmap[i][j] == 1:
                if (j%3) == int(0):
                    print(" | ",end='')
                print(Fore.LIGHTGREEN_EX,end='')
                if board[i][j] == 0:
                    print(" "+"_"+" ",end='')
                    boardrefmap[i][j]=int(1)
                else :
                    print(" "+str(board[i][j])+" ",end='')  
                print(Style.RESET_ALL,end='')
                if (j) == int(8):
                    print(" | ",end='')
            else:
                print(Style.RESET_ALL,end='')
                if (j%3) == int(0):
                    print(" | ",end='')
                if board[i][j] == 0:
                    print(" "+"_"+" ",end='')
                    boardrefmap[i][j]=int(1)
                else :
                    print(" "+str(board[i][j])+" ",end='')  
                if (j) == int(8):
                    print(" | ",end='')
        
        print()
        if ((i+1)%3) == int(0):
            print(" ------------------------------------- ")



def populateboard():
    global board
    global boardrefmap
    dataframe=[]
    question=open("question.txt",'r')
    lines=question.readlines()
    question.close()


    for line in lines:
        data=line.strip('\n').split(',')
        for i in range(len(data)):
            data[i]=int(data[i])
            if data[i] < 0 or data[i] > 9:
                data[i]=0
        dataframe.append(data)

    board=dataframe


if __name__ == "__main__":

    populateboard()
    stat=True
    print("LOADING BOARD FROM THE FILE...")
    print("INIT BOARD_MAPS.")
    initdefmap()
    showboard(board)
    print("Solving ...")
    solver()
