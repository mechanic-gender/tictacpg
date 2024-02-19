import random

import pygame

pygame.init()
size=(700,700)
dis = pygame.display.set_mode((700, 700))
bs = 3
ts = int(700 / bs)
lw = 5
cw = 25
crw = 15
fs = 7
red = (100, 0, 0)
blue = (0, 0, 100)
green = (0, 100, 0)
white = (250, 250, 250)
black = (0, 0, 0)
board = [[None] * bs for i in range(bs)]


def db():
    dis.fill(black)
    for i in range(1, bs):
        pygame.draw.line(dis, green, (0, i * ts), (size[0], i * ts), lw)
        pygame.draw.line(dis, green, (i * ts, 0), (i * ts, size[0]), lw)
    for i in range(bs):
        for j in range(bs):
            if board[i][j] == "X":
                pygame.draw.line(dis, white, (i * ts + cw, j * ts + cw), ((i + 1) * ts - cw, (j + 1) * ts - cw), cw)
                pygame.draw.line(dis, white, ((i + 1) * ts - cw, j * ts + cw), (i * ts + cw, (j + 1) * ts -cw), cw)
            elif board[i][j] == "0":
                pygame.draw.circle(dis, white, ((i * ts) + ts // 2, (j * ts) + ts // 2), (ts // 2 - cw), cw)


def check_winner():
    for i in range(bs):

        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] is not None):
            return board[i][0]

        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] is not None):
            return board[0][i]

        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
            return board[0][0]


        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            return board[0][2]


        return None

def main():
    turn="X"
    font=pygame.font.SysFont("Script",fs)
    while True:
        for event in pygame.event.get():
            if  event.type==pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                tx=x//ts
                ty=y//ts
                if board[tx][ty]is None:
                    board[tx][ty]=turn
                    if turn=="X":
                        turn = "0"
                    else:
                        turn = "X"
        db()
        winner=check_winner()
        if winner is not None:
            print("victory",winner)
            dis.fill(black)
            a=font.render(f"{winner} wins",True,(250,250,250))
            dis.blit(a,(350,350))
            pygame.display.update()
            pygame.time.wait(150)
            return
        elif all([all(row)for row in board])and(winner is None):
            print("tie")
            dis.fill(black)
            a=font.render(f"no pasaran",True,(250,250,250))
            dis.blit(a,(350,350))
            pygame.display.update()
            pygame.time.wait(150)
            while True :
                dis1=pygame.display.set_mode((1500,1500))
                dis1.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                pygame.display.update()

        #todo прикрутить проверку победы
        pygame.display.update()

if __name__=="__main__":
    main()