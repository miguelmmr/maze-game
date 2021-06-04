import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
VEL = 10
moveU = False
moveD = False
moveL = False
moveR = False
lvlstart = True
# WHITE = (255, 255, 255), RED = (255, 0, 0), GREEN = (0,255,0), BLUE = (0,0,255), BLACK = (0, 0, 0), B = (0,50,255)
lvl = 1
player = pygame.Rect(50,100,10,10)

class Border:
    
    def __init__(self, x , y, w , h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x,y,w,h)
        
    def draw(self):
        pygame.draw.rect(WIN, (0,0,255), self.rect)

class Meta:
    def __init__(self, x , y ):
        self.rect = pygame.Rect(x,y,10,10)
    
    def draw(self):
        pygame.draw.rect(WIN, (0,255,0), self.rect)

class Player:
    def __init__(self, x, y , w , h):
        self.rect = pygame.Rect(x,y,w,h)
        
    def draw(self):
        pygame.draw.rect(WIN , (0,255,0), self.rect)

class Portal:
    def __init__(self, x1, y1 , x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.rect1 = pygame.Rect( x1 , y1 , 10 , 10)
        self.rect2 = pygame.Rect( x2 , y2 , 10 , 10)
        
    def draw1(self):
        pygame.draw.rect(WIN , (250,0,250), self.rect1)        
    def draw2(self):    
        pygame.draw.rect(WIN , (250,0,250), self.rect2)

def player_movement(player, playerStart , BORDER , meta, Portal ):
    
    global moveU , moveD , moveL , moveR ,lvl , lvlstart
    
    if player.x <0 or player.x>WIDTH or player.y<0 or player.y>HEIGHT:
        lvlstart = True
    if lvlstart:
        player.x = playerStart.x
        player.y = playerStart.y
        moveU = False
        moveD = False
        moveL = False
        moveR = False
        lvlstart = False
        
    def portal_mov(player, Portal , x , y):
        for portal in Portal:
            if portal.rect1.colliderect(player):
                player.x = portal.x2 + x
                player.y = portal.y2 + y 
            if portal.rect2.colliderect(player):
                player.x = portal.x1+x
                player.y = portal.y1+y
    
    if moveU:
        player.y -=VEL
        portal_mov(player, Portal , 0 , -VEL)
            
        for border in BORDER:
            if player.colliderect(border.rect):
                moveU =False
        if moveU==False:
            player.y +=VEL

    if moveD:
        player.y +=VEL     
        portal_mov(player, Portal , 0 , VEL)
        
        for border in BORDER:
            if player.colliderect(border.rect):
                moveD =False
        if moveD==False:
            player.y -=VEL
            
    if moveL:
        player.x -=VEL
        portal_mov(player, Portal , -VEL , 0)
        
        for border in BORDER:
            if player.colliderect(border.rect):
                moveL =False
        if moveL==False:
            player.x +=VEL
            
    if moveR:
        player.x += VEL
        portal_mov(player, Portal , VEL , 0)
                
        for border in BORDER:
            if player.colliderect(border.rect):
                moveR =False
        if moveR==False:
            player.x -=VEL
            
    if player.colliderect(meta):
            lvl +=1
            moveU = False
            moveD = False
            moveL = False
            moveR = False
            lvlstart = True
            

def main():
    global moveU , moveD , moveL , moveR , run , lvlstart
    clock = pygame.time.Clock()
    
    def draw_window(BORDER,meta, portal):
        WIN.fill((0,0,0))
                
        for i in BORDER[:]:
            i.draw()
        
        for i in portal[:]:
            i.draw1()
            i.draw2()
        
        pygame.draw.rect(WIN , (255,250,0), player)
        meta.draw()
        pygame.display.update()
    
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False                        
                
        if event.type == pygame.KEYDOWN:
            if moveD == False and moveL == False and moveR == False and moveU == False:
            
                if event.key ==pygame.K_UP:
                    if moveD == False and moveL == False and moveR == False:
                        moveU = True
    
                if event.key == pygame.K_DOWN:
                    if moveU == False and moveL == False and moveR == False:
                        moveD = True

                if event.key ==pygame.K_LEFT:
                    if moveU == False and moveD == False and moveR == False:
                        moveL = True

                if event.key == pygame.K_RIGHT:
                    if moveU == False and moveD == False and moveL == False:
                        moveR = True

        if lvl ==1:            
            playerStart = pygame.Rect(100,200,10,10)
            BORDER = [Border(500,0, 10,700),Border(0,20,10,500),Border(10,10,500,10) 
                  ,Border(0,300,150,10),Border(100,100,100,10), Border(450,100,10,150)]
            meta = Meta(490,200)            
            portal = []
            
        elif lvl==2:
            playerStart = pygame.Rect(100,100,10,10)
            BORDER = [Border(500,0, 10,300),Border(0,20,10,500),Border(0,450,300,10),Border(150,50,10,100)
                      ,Border(60,350,100,10),Border(120,240,220,10),Border(230,280,10,100),Border(340,300,10,200)]
            meta =Meta(250,100)            
            portal  = [Portal(350,100 , 250 , 250)]
            
        elif lvl==3:
            playerStart = pygame.Rect(450,250,10,10)
            BORDER = [Border(400,200, 10,100),Border(520,200,10,100),Border(400,200,80,10),Border(400,300,130,10),
                      Border(450,60,10,70),Border(450,60,100,10),Border(540,60,10,70),
                      Border(200,130,10,80),Border(230,130,100,10),Border(200,210,50,10),
                      Border(440,380,10,50),Border(300,430,300,10),Border(300,420,10,20),
                      Border(660,60,10,100),Border(600,150,70,10),Border(600,60,70,10),
                      Border(150,300,10,70),Border(150,290,70,10),Border(150,360,70,10),
                      Border(700,290,70,10),Border(700,360,70,10),Border(770,290,10,80)]
            meta =Meta(450,350)            
            portal = [Portal(360,350,530,350)]
            
        elif lvl == 4:
            playerStart = pygame.Rect(50,50,10,10)
            BORDER = [Border(0,20,100,10),Border(300,30,120,10),Border(20,130,120,10),
                      Border(350,50,10,80),Border(500,30,10,100),
                      Border(0,400,200,10),Border(0,380,10,20),Border(250,200,150,10),Border(80,180,10,100),
                      Border(300,400,100,10),Border(300,320,100,10),Border(300,320,10,30),Border(390,380,10,20),
                      Border(420,350,100,10),Border(520,330,10,30),
                      Border(550,120,100,10),Border(500,180,50,10),Border(600,250,10,50)]
            meta = Meta(500,300)
            portal = [Portal(140,260, 500, 190)]
            
        player_movement(player, playerStart, BORDER, meta, portal )
        draw_window(BORDER,meta,portal)
        
    pygame.quit()

main()

            