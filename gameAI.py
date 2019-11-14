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
                    board.lose = True
                elif (boardCenter >= 0 and boardUP == 0):
                    board.touchBall = True

class BoardAI:
    def __init__(self, selfBoard, otherBoardList, ballList, aiArray):
        self.board = board
        self.otherBoardList = otherBoardList
        self.ballList = ballList
        self.aiArray = aiArray