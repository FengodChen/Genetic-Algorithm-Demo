import tkinter
import numpy as np
import math

class Judgment:
    def __init__(self, boardList, ballList):
        self.boardList = boardList
        self.ballList = ballList
    
    def judgeBoardStatus(self):
        touchBallFlag = False
        for board in self.boardList:
            for ball in self.ballList:
                (boardCenter, boardLR) = board.ballOnLR(ball)
                boardUP = board.ballOnUD(ball)
                if (boardUP < 0):
                    board.lose += 1
                    ball.useful = False
                elif (boardCenter >= 0 and boardUP == 0):
                    if (not touchBallFlag):
                        board.isTouchBall = True
                        board.touchBall = ball
                        touchBallFlag = True
                else:
                    if (not touchBallFlag):
                        board.isTouchBall = False
                        board.touchBall = None

    def nextTurn(self):
        for board in self.boardList:
            board.draw()
        for ball in self.ballList:
            ball.draw()

class BoardAIArray:
    def __init__(self):
        # Answer: Turn left or right, and speed, and ball weight
        # Ball: dt LR(,) dt UD()
        self.ballMovement = np.random.rand(2, 1, 3)
        # Ball: LR(, ) UD()
        self.ballPosition = np.random.rand(2, 1, 3)
        # Ball Value: [dt LR, dt UD], [LR, UD]
        self.ballValue = np.random.rand(2, 2, 1, 3)
        # Bloak: LRBloak(, )
        self.bloakPosition = np.random.rand(2, 1, 2)

        # Answer: Set ball direction
        # Answer: Set ball speed
        # Rival: LRBloak(, )
        self.rivalPosition = np.random.rand(2, 1, 5)


class BoardAI:
    def __init__(self, selfBoard, otherBoard, ballList, boardAIArray):
        self.selfBoard = selfBoard
        self.otherBoard = otherBoard
        self.ballList = ballList
        self.ballNum = len(ballList)
        self.boardAIArray = boardAIArray
        # ballStatus[] = [ballOnLR] + [ballOnUD]
        self.ballStatus = []

        for ball in ballList:
            bC, bLR = self.selfBoard.ballOnLR(ball)
            bUD = self.selfBoard.ballOnUD(ball)
            self.ballStatus.append([bC, bLR, bUD])
        
        self.ballStatus = np.array(self.ballStatus)
    
    def calculateBoardMovement(self):
        boardTurnLR = 0
        boardTurnSpeed = 0
        for ptr in range(self.ballNum):
            (bC, bLR) = self.selfBoard.ballOnLR(self.ballList[ptr])
            bUD = self.selfBoard.ballOnUD(self.ballList[ptr])
            ballStatus = np.array([bC, bLR, bUD])
            dBallStatus = ballStatus - self.ballStatus[ptr]
            self.ballStatus[ptr] = ballStatus

            dBoardLR = np.matmul(dBallStatus, self.boardAIArray.ballMovement[0].T)
            dBoardLRWeight = np.matmul(dBallStatus, self.boardAIArray.ballValue[0][0].T)
            boardLR = np.matmul(ballStatus, self.boardAIArray.ballPosition[0].T)
            boardLRWeight = np.matmul(dBallStatus, self.boardAIArray.ballValue[0][1].T)
            boardTurnLR += dBoardLR*dBoardLRWeight + boardLR*boardLRWeight

            dBoardSpeed = np.matmul(dBallStatus, self.boardAIArray.ballMovement[1].T)
            dBoardSpeedWeight = np.matmul(dBallStatus, self.boardAIArray.ballValue[1][0].T)
            boardSpeed = np.matmul(ballStatus, self.boardAIArray.ballPosition[1].T)
            boardSpeedWeight = np.matmul(dBallStatus, self.boardAIArray.ballValue[1][1].T)
            boardTurnLR += dBoardSpeed*dBoardSpeedWeight + boardSpeed*boardSpeedWeight
        
        (blL, blR) = self.selfBoard.getLRBloak()
        bloakArray = np.array([blL, blR])
        
        boardTurnLR += np.matmul(bloakArray, self.boardAIArray.bloakPosition[0].T)
        boardTurnSpeed += np.matmul(bloakArray, self.boardAIArray.bloakPosition[1].T)

        return (boardTurnLR, boardSpeed)
    
    def calculateBallMovement(self, ball):
        (bL, bR) = self.selfBoard.getLRBloak()
        (rbL, rbR) = self.otherBoard.getLRBloak()
        (ballM, tmp) = self.selfBoard.ballOnLR(ball)
        rivalLocation = np.array([bL, bR, rbL, rbR, ballM])
        ballSpeed = np.matmul(rivalLocation, BoardAIArray.rivalPosition[0].T)
        ballDirection = np.matmul(rivalLocation, BoardAIArray.rivalPosition[1].T)

        return (ballSpeed, ballDirection)
    
    def moveBoard(self):
        (boardTurnLR, boardSpeed) = self.calculateBoardMovement()
        boardSpeed = int(boardSpeed)
        if (boardTurnLR < 0):
            self.selfBoard.turnLeft(boardSpeed)
        elif (boardTurnLR > 0):
            self.selfBoard.turnRight(boardSpeed)
        else:
            pass    # Do nothing
    
    def setBallMovement(self):
        if (self.selfBoard.isTouchBall):
            (ballSpeed, ballDirection) = self.calculateBallMovement(self.selfBoard.touchBall)
            ballDirection %= 180.0
            ballDirection = (ballDirection / 360.0) * 2 * math.pi
            if (self.selfBoard.reboundSurface == "left"):
                ballDirection += math.pi / 2.0
            elif (self.selfBoard.reboundSurface == "right"):
                ballDirection -= math.pi / 2.0
            elif (self.selfBoard.reboundSurface == "up"):
                ballDirection += math.pi
            elif (self.selfBoard.reboundSurface == "down"):
                ballDirection += 0
            ball.speed = float(ballSpeed)
            ball.moveDirection = float(ballDirection)
    
    def nextTurn(self):
        self.moveBoard()
        self.setBallMovement()
        for ball in self.ballList:
            ball.move()