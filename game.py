import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
VEL = 10

lvlstart = True
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0 , 255 , 0)
BLUE = (0 , 0 , 255)
BLACK = (0 , 0 , 0)
PURPLE = (255 , 0 , 255)
lvl = 1

class Border:
    
    def __init__(self, x , y, w , h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x,y,w,h)
        
    def draw(self):        
        pygame.draw.rect(WIN, BLUE, self.rect)

class Meta:
    def __init__(self, x , y ):
        self.rect = pygame.Rect(x , y , 10 , 10)
    
    def draw(self):
        pygame.draw.rect(WIN, GREEN, self.rect)

class Player:

        
    def __init__(self, x , y ):

        self.rect = pygame.Rect(x , y , 10 , 10)        
        self.movement = [False , False , False , False]

    def draw(self):
        pygame.draw.rect(WIN , YELLOW , self.rect)

class Portal:
    def __init__(self , x1 , y1 , x2 , y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.rect1 = pygame.Rect( x1 , y1 , 10 , 10)
        self.rect2 = pygame.Rect( x2 , y2 , 10 , 10)
        
    def draw1(self):
        pygame.draw.rect(WIN , PURPLE , self.rect1)        
    def draw2(self):    
        pygame.draw.rect(WIN , PURPLE , self.rect2)

def player_movement(player , playerStart , BORDER , meta , Portal ):
    
    global lvl , lvlstart
    
    if player.rect.x <0 or player.rect.x>WIDTH or player.rect.y<0 or player.rect.y>HEIGHT:
        lvlstart = True

    if lvlstart:
        player.rect.x = playerStart.x
        player.rect.y = playerStart.y
        player.movement = [False , False , False , False]

        lvlstart = False
        
    def portal_mov(player, Portal , x , y):
        for portal in Portal:
            if portal.rect1.colliderect(player.rect):
                player.rect.x = portal.x2 + x
                player.rect.y = portal.y2 + y 
            if portal.rect2.colliderect(player.rect):
                player.rect.x = portal.x1+x
                player.rect.y = portal.y1+y
    
    def border_mov(player , Border , dir ):
        for border in BORDER:
            if player.rect.colliderect(border.rect):
                player.movement[dir] =False

    if player.movement[0]:
        player.rect.y -=VEL
        portal_mov(player , Portal , 0 , -VEL)        
        border_mov(player , BORDER , 0)
        
        if player.movement[0]==False:
            player.rect.y +=VEL

    if player.movement[1]:
        player.rect.y +=VEL     
        portal_mov(player , Portal , 0 , VEL)
        border_mov(player , BORDER , 1)
        
        if player.movement[1]==False:
            player.rect.y -=VEL
            
    if player.movement[2]:
        player.rect.x -=VEL
        portal_mov(player , Portal , -VEL , 0)
        border_mov(player , BORDER , 2)
        
        if player.movement[2]==False:
            player.rect.x +=VEL
            
    if player.movement[3]:
        player.rect.x += VEL
        portal_mov(player , Portal , VEL , 0)
        border_mov(player , BORDER , 3)
                
        if player.movement[3]==False:
            player.rect.x -=VEL
            
    if player.rect.colliderect(meta):
            lvl +=1

            lvlstart = True
            
Player = Player( 50 , 100)

def main():
    global run , lvlstart
    clock = pygame.time.Clock()
    
    def draw_window(player , BORDER , meta , portal):
        WIN.fill((0,0,0))
                
        for block in BORDER[:]:
            block.draw()
        
        for port in portal[:]:
            port.draw1()
            port.draw2()
        
        player.draw()
        meta.draw()
        pygame.display.update()
    
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False                        
                
        if event.type == pygame.KEYDOWN:
            if Player.movement[0] == False and Player.movement[1] == False and Player.movement[2] == False and Player.movement[3] ==False:
            
                if event.key ==pygame.K_UP:
                    Player.movement[0] = True
    
                if event.key == pygame.K_DOWN:
                    Player.movement[1] = True

                if event.key ==pygame.K_LEFT:
                    Player.movement[2] = True

                if event.key == pygame.K_RIGHT:
                    Player.movement[3] = True

        if lvl ==1:
            playerStart = pygame.Rect(100,200,10,10)
            BORDER = [Border(500,0, 10,700) , Border(0,20,10,500) , Border(10,10,500,10)
                  , Border(0,300,150,10) , Border(100,100,100,10) , Border(450,100,10,150)]
            meta = Meta(490,200)
            portal = []
            
        elif lvl==2:
            playerStart = pygame.Rect(100,100,10,10)
            BORDER = [Border(500,0, 10,300) , Border(0,20,10,500) , Border(0,450,300,10) , Border(150,50,10,100),
                      Border(60,350,100,10) , Border(120,240,220,10) , Border(230,280,10,100) , Border(340,300,10,200)]
            meta =Meta(250,100)
            portal  = [Portal(350,100 , 250 , 250)]
            
        elif lvl==3:
            playerStart = pygame.Rect(450,250,10,10)
            BORDER = [Border(400,200, 10,100) , Border(520,200,10,100) , Border(400,200,80,10) , Border(400,300,130,10),
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
            
        player_movement(Player ,  playerStart, BORDER, meta, portal )
        draw_window(Player , BORDER , meta , portal)
        
    pygame.quit()

main()
