import pygame
import sys
import random
import pygame_widgets

def bubblesort(screen,data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i- 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            screen.fill((0,0,0))
            buttons(screen)
            show_data(screen,data)
            pygame.time.delay(10)
            pygame.display.update()

def insertionsort(screen,data):
    for i in range(1,len(data)):
        temp = data[i]
        j = i - 1
        while j>=0 and data[j] >= temp:
            data[j+1] = data[j]
            j = j - 1
            screen.fill((0,0,0))
            buttons(screen)
            show_data(screen,data)
            pygame.time.delay(50)
            pygame.display.update()
            
        data[j+1] = temp
        screen.fill((0,0,0))
        buttons(screen)
        show_data(screen,data)
        pygame.time.delay(50)
        pygame.display.update()
    
def selectionsort(screen,data):
    for i in range(len(data)-1):
        small = i
        for j in range(i+1,len(data)):
            if data[j] < data[small]:
                small = j
        data[small],data[i] = data[i],data[small]   
        screen.fill((0,0,0))
        buttons(screen)
        show_data(screen,data)
        pygame.time.delay(50)
        pygame.display.update()     

def merge(screen,data,l,mid, r):
    temp = []
    i = l; j = mid+1
    # pygame.event.pump() 
    while i<=mid and j<=r:
        screen.fill((0,0,0))
        buttons(screen)
        show_data(screen,data)
        pygame.time.delay(50)
        pygame.display.update() 
        if data[i] < data[j]:
            temp.append(data[i])  
            i+=1
        else:
            temp.append(data[j])   
            j+=1
            
    while i<=mid:
        screen.fill((0,0,0))
        buttons(screen)
        show_data(screen,data)
        pygame.time.delay(50)
        pygame.display.update()
        temp.append(data[i])  
        i+=1
    while j<=r:
        screen.fill((0,0,0))
        buttons(screen)
        show_data(screen,data)
        pygame.time.delay(50)
        pygame.display.update()  
        temp.append(data[j])  
        j+=1
    j = 0
    for i in range(l, r+1): 
        # pygame.event.pump() 
        data[i] = temp[j]
        j+= 1
        buttons(screen)
        show_data(screen,data)
        pygame.time.delay(50)
        pygame.display.update()  


def mergesort(screen,data,l,r):
    if l<r:
        mid = (l+r)//2
        mergesort(screen,data,l,mid)
        mergesort(screen,data,mid+1,r)
        merge(screen,data,l,mid,r)

def partition(screen,data,l,r):
    loc = l
    while True:
        while data[loc]<=data[r] and loc!=r:
            r = r - 1
        if loc==r:
            return loc
        data[loc],data[r] = data[r],data[loc]
        screen.fill((0,0,0))
        buttons(screen)
        show_data(screen,data)
        pygame.time.delay(50)
        pygame.display.update()  
        loc = r
        while data[loc]>=data[l] and loc!=l:
            l = l + 1
        if loc==l:
            return loc
        data[loc],data[l] = data[l],data[loc]
        screen.fill((0,0,0))
        buttons(screen)
        show_data(screen,data)
        pygame.time.delay(50)
        pygame.display.update()  
        loc = l

def quicksort(screen, data,l,r):
    if l<r:
        x = partition(screen,data,l,r)
        quicksort(screen, data, l,x-1)
        quicksort(screen, data, x+1,r)

# Rect(left, top, width, height) Rect (pos, size) Rect(obj)
def show_data(screen,data):
    for i in range(len(data)):
        pygame.draw.rect(screen, (255,130, 10), pygame.Rect((i*5,600-data[i]), (2,data[i])))


def buttons(screen):
    pygame.draw.rect(screen, (148,211,217), pygame.Rect((0,0), (1000,100)))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect((25,25), (200,50)))
    text = font.render("Back",(255,255,255),(0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (120,50)
    screen.blit(text, textRect)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect((775,25), (200,50)))
    text = font.render("Start",(255,255,255),(0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (870,50)
    screen.blit(text, textRect)
 

def buttons_select(screen,data):
    while True:
        pygame_widgets.update(pygame.event.get())
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x>= 25 and x <= 225 and y >=25 and y <= 75:
                    data = randomdata()
                    main_screen(screen,data) 
                if x>=775 and x <= 975 and y>=25 and y<=75:
                    return True

def processselect():
    pygame.time.delay(10)
    screen.fill((0,0,0))
    pygame.display.update()
    show_data(screen,data)
    pygame.display.update()
    pygame.time.delay(20)
    buttons(screen)
    pygame.display.update()

def main_screen(screen,data):
    data = randomdata()
    screen.fill((0,0,0))
    pygame.display.update()
    for i in range(8):
        if i == 0:
            pygame.draw.rect(screen, (255,130, 10), pygame.Rect(((250,10), (500,60))))
            text = font.render("Bubble Sort",(255,255,255),(0,0,0)) 
            textRect = text.get_rect() # set the center of the rectangular object.
            textRect.center = (500,35)
            screen.blit(text, textRect)
        else:
            pygame.draw.rect(screen, (255,130, 10), pygame.Rect(((250,70*i+10), (500,60))))
            if i==1:
                text = font.render("Insertion Sort",(255,255,255),(0,0,0)) 
                textRect = text.get_rect()
                textRect.center = (500,110)
                screen.blit(text, textRect)
            elif i==2:
                text = font.render("Selection Sort",(255,255,255),(0,0,0)) 
                textRect = text.get_rect()
                textRect.center = (500,180)
                screen.blit(text, textRect)
            elif i==3:
                text = font.render("Merge Sort",(255,255,255),(0,0,0)) 
                textRect = text.get_rect()
                textRect.center = (500,250)
                screen.blit(text, textRect)
            elif i==4:
                text = font.render("Quick Sort",(255,255,255),(0,0,0)) 
                textRect = text.get_rect()
                textRect.center = (500,320)
                screen.blit(text, textRect)
            elif i==5:
                pass
            elif i==6:
                pass
            elif i==7:
                pass

        pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                if x >= 250 and x <= 750 and y >=10 and y <= 70:
                    processselect()
                    start = buttons_select(screen, data)
                    if start == True:
                        bubblesort(screen, data)
                        while True:
                            buttons_select(screen, data)
                    # break
                if x >= 250 and x <= 750 and y >=80 and y <= 140:
                    processselect()
                    start = buttons_select(screen, data)
                    if start == True:
                        insertionsort(screen, data)
                        while True:
                            buttons_select(screen, data)               
                if x >= 250 and x <= 750 and y >=150 and y <= 210:
                    processselect()
                    start = buttons_select(screen, data)
                    if start == True:
                        selectionsort(screen, data)
                        while True:
                            buttons_select(screen, data)
                if x >= 250 and x <= 750 and y >=220 and y <= 280:
                    processselect()
                    start = buttons_select(screen, data)
                    if start == True:
                        mergesort(screen, data,0,len(data)-1)
                        while True:
                            buttons_select(screen, data)
                if x >= 250 and x <= 750 and y >=290 and y <= 350:
                    processselect()
                    start = buttons_select(screen, data)
                    if start == True:
                        quicksort(screen, data,0,len(data)-1)
                        while True:
                            buttons_select(screen, data)
                if x >= 250 and x <= 750 and y >=360 and y <= 420:
                    print("5")
                if x >= 250 and x <= 750 and y >=430 and y <= 490:
                    print("6")
                if x >= 250 and x <= 750 and y >=500 and y <= 560:
                    print("7")
            pygame_widgets.update(pygame.event.get())
            pygame.display.update()

def randomdata():
    data = []
    for i in range(100):
        data.append(random.randint(25,475))
    return data

        
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600), 0, 32)
pygame.display.set_caption("Visualizer")

data = randomdata()
font = pygame.font.SysFont("Comic Sans MS",35)
main_screen(screen,data)