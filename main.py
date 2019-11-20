#! /usr/bin/python3

import tkinter
import math

import gameObj
import gameAI

def createGUI(width, height):
    tk = tkinter.Tk()
    tk.resizable(0, 0)
    canvas = tkinter.Canvas(tk, width=width, height=height)
    canvas.pack()
    return (tk, canvas)

def haveGame(boardAIList, judge, canvas):
    for boardAI in boardAIList:
        boardAI.nextTurn()
    judge.nextTurn()
    judge.judgeBoardStatus()
    #if (not bat1.lose):
    canvas.after(10, haveGame, boardAIList, judge, canvas)

if __name__ == "__main__":
    cWidth = 500
    cHeight = 500
    (tk, canvas) = createGUI(cWidth, cHeight)

    board1 = gameObj.Board(0, 100, 10, 40, canvas, cWidth, cHeight, "board1", "right")
    board2 = gameObj.Board(490, 300, 10, 40, canvas, cWidth, cHeight, "board2", "left")
    ball1 = gameObj.Ball(400, 100, 5, canvas, cWidth, cHeight, "ball1", (3/8)*math.pi)
    ballList = [ball1]

    aiArray1 = gameAI.BoardAIArray()
    aiArray2 = gameAI.BoardAIArray()
    boardAI1 = gameAI.BoardAI(board1, board2, ballList, aiArray1)
    boardAI2 = gameAI.BoardAI(board2, board1, ballList, aiArray2)
    boardAIList = [boardAI1, boardAI2]

    judge = gameAI.Judgment([board1, board2], ballList)

    haveGame(boardAIList, judge, canvas)
    
    tkinter.mainloop()