from re import X
import pygame
import numpy
pygame.init()

circlePos=[250,203]

height=800
width=1000
win=pygame.display.set_mode((1000,height))
font=pygame.font.SysFont("Arial",50)
selected=[1,1]
numbers=[]
rectWidth=50


def generate(num):
    global numbers
    numbers=[]
    for i in range(num+1):
        numbers.append(numpy.random.randint(1,101))
    return numbers


def drawScreen(numbers):
    win.fill((0,0,0))

    pygame.draw.rect(win,(255,255,255),(250,200,300,5))
    pygame.draw.circle(win,(134,164,200),(circlePos[0],circlePos[1]),15)

    text1=font.render("Bubble sort",True,(0,0,0))
    if selected[0]==1:
        pygame.draw.rect(win,(200,200,220),(100,100,300,50))
    else:
        pygame.draw.rect(win,(255,150,150),(100,100,300,50))
    win.blit(text1,(100,100))


    text2=font.render("Selection sort",True,(0,0,0))
    if selected[0]==-1:
        pygame.draw.rect(win,(200,200,220),(100,40,300,50))
    else:
        pygame.draw.rect(win,(255,150,150),(100,40,300,50))
    win.blit(text2,(100,40))


    text3=font.render("Descending",True,(0,0,0))
    if selected[1]==1:
        pygame.draw.rect(win,(200,200,220),(500,100,270,50))
    else:
        pygame.draw.rect(win,(255,150,150),(500,100,270,50))
    win.blit(text3,(500,100))

    text3=font.render("Ascending",True,(0,0,0))
    if selected[1]==-1:
        pygame.draw.rect(win,(200,200,220),(500,40,270,50))
    else:
        pygame.draw.rect(win,(255,150,150),(500,40,270,50))
    win.blit(text3,(500,40))


    for i in range(len(numbers)):
        pygame.draw.rect(win,(130,130,200),(i*rectWidth,height-500*numbers[i]/100,rectWidth,height))
        pygame.draw.rect(win,(255,255,255),(i*rectWidth,height-500*numbers[i]/100,rectWidth,height),width=1)  
    pygame.display.update()



def highlight(a,b,numbers):
    pygame.draw.rect(win,(130,0,0),(a*rectWidth,height-500*numbers[a]/100,rectWidth,height))
    pygame.draw.rect(win,(255,255,255),(a*rectWidth,height-500*numbers[a]/100,rectWidth,height),width=1)
    pygame.draw.rect(win,(0,130,0),(b*rectWidth,height-500*numbers[b]/100,rectWidth,height))
    pygame.draw.rect(win,(255,255,255),(b*rectWidth,height-500*numbers[b]/100,rectWidth,height),width=1)
    pygame.display.update()


def moveSlider():
    x,y=pygame.mouse.get_pos()
    repeat=True
    global rectWidth

    if numpy.sqrt((x-circlePos[0])**2+(y-circlePos[1])**2)<=15:
        prevX=x

        while repeat:
            x,y=pygame.mouse.get_pos()
            if 250<=x<=550 and prevX!=x:
                prevX=x
                circlePos[0]=x
                length=int(20+80*(x-250)/300)
                numbers=generate(length)
                rectWidth=width/length
                drawScreen(numbers)
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONUP:
                    repeat=False
    else:
        while repeat:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONUP:
                    repeat=False
        


def insertionSort(numbers):
    if selected[1]==1:
        sign=1
    else:
        sign=-1

    for i in range(len(numbers)):
        j=i
        while j>0:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()

            drawScreen(numbers)
            highlight(j,j-1,numbers)
            pygame.time.delay(10)
            if sign*numbers[j]<sign*numbers[j-1]:
                temp=numbers[j]
                numbers[j]=numbers[j-1]
                numbers[j-1]=temp
                j-=1
            else:
                break
    drawScreen(numbers)


def bubbleSort(numbers):
    if selected[1]==1:
        sign=1
    else:
        sign=-1
    
    for i in range(len(numbers)-1,-1,-1):
        for j in range(1,i+1):
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()

                drawScreen(numbers)
                highlight(j,j-1,numbers)
                pygame.time.delay(10)
                if sign*numbers[j]<sign*numbers[j-1]:
                    temp=numbers[j]
                    numbers[j]=numbers[j-1]
                    numbers[j-1]=temp
    drawScreen(numbers)
     


numbers=generate(20)
drawScreen(numbers)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if event.type==pygame.KEYDOWN:
            
            if event.unicode=='p':
                selected[0]*=-1
               
                drawScreen(numbers)
            elif event.unicode=='k':
                selected[1]*=-1
                drawScreen(numbers)
                
            elif event.unicode==' ':
                if selected[0]==1:
                    insertionSort(numbers)
                else:
                    bubbleSort(numbers)
            
        elif event.type==pygame.MOUSEBUTTONDOWN:
            moveSlider()
         