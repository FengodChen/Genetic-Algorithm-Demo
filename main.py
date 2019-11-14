#! /usr/bin/python3

import tkinter
import gameObj
import gameAI

def createGUI(width, height):
    tk = tkinter.Tk()
    tk.resizable(0, 0)
    canvas = tkinter.Canvas(tk, width=width, height=height)
    canvas.pack()
    return (tk, canvas)

def test(bat, ba, judge, canvas):
    bat1.draw()
    ba1.draw()
    bat1.turnRight()
    ba1.move()
    judge.judgeBoardStatus()
    #if (not bat1.lose):
    canvas.after(10, test, bat, ba, judge, canvas)

if __name__ == "__main__":
    cWidth = 500
    cHeight = 500
    (tk, canvas) = createGUI(cWidth, cHeight)
    bat1 = gameObj.Board(200, 0, 10, 40, canvas, cWidth, cHeight, "board1", "right")
    #bat1.draw()
    ba1 = gameObj.Ball(400, 100, 5, canvas, cWidth, cHeight, "ball1", (3/8)*3.1415, 1)
    judge = gameAI.Judgment([bat1], [ba1])
    #ba1.draw()
    test(bat1, ba1, judge, canvas)
    
    tkinter.mainloop()