import pygame


pygame.init()
dis=pygame.display.set_mode((1500 ,700))
bs=3
ts=int(700/bs)
lw=5
cw=25
crw=15
fs=15
red=(100,0,0)
blue=(0,0,100)
green=(0,100,0)
white=(250,250,250)
black=(0,0,0)
board=[[None]*bs or i in range (bs)]



def db():
    dis.fill(black)
    for i in range (1,bs):
        pygame.draw.line(dis,green,(0,i*ts),(1500,i*ts),lw)
        pygame.draw.line(dis,green,(i*ts*2,0),(i*ts*2,1100),lw)
    for i in range(bs):
        for j in range(bs):
            if board[i][j]=="x"
    pygame.display.update()

db()
a=1
while a <100000000:
    a+=1