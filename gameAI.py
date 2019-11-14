import tkinter

class Judgment:
    def __init__(self, boardList, ballList):
        self.boardList = boardList
        self.ballList = ballList
    
    def judgeBoardStatus(self):
        for board in self.boardList:
            for ball in self.ballList:
                (boardCenter, boardLR) = board.ballOnLR(ball)
                boardUP = board.ballOnUD(ball)
                if (boardUP < 0):
                    board.lose += 1
                elif (boardCenter >= 0 and boardUP == 0):
                    board.touchBall = True
                else:
                    board.touchBall = False

class BoardAIArray:
    def __init__(self):
        pass

class BoardAI:
    def __init__(self, selfBoard, otherBoardList, ballList, boardAIArray):
        self.board = board
        self.otherBoardList = otherBoardList
        self.ballList = ballList
        self.aiArray = boardAIArray