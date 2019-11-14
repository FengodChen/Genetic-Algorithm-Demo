import tkinter
import gameObj
import gameAI

def createGUI(width, height):
    tk = tkinter.Tk()
    canvas = tkinter.Canvas(tk, width=width, height=height)
    canvas.pack()
    return (tk, canvas)

def test(bat, ba, judge, canvas):
    bat1.draw()
    ba1.draw()
    bat1.turnLeft()
    ba1.move()
    judge.judgeLose()
    if (not bat1.lose):
        canvas.after(10, test, bat, ba, judge, canvas)

if __name__ == "__main__":
    (tk, canvas) = createGUI(500, 500)
    bat1 = gameObj.Board(200, 0, 10, 40, canvas, 500, 500, "board1", "right")
    #bat1.draw()
    ba1 = gameObj.Ball(400, 100, 5, canvas, "ball1", (3/4)*3.1415, 1)
    judge = gameAI.Judgment([bat1], [ba1])
    #ba1.draw()
    test(bat1, ba1, judge, canvas)
    tkinter.mainloop()