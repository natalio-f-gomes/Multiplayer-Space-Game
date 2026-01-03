import os
import pygame

class Game:
    def __init__(self):
        pygame.font.init()
        pygame.mixer.init()

        self.BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets",'GrEnade+1.mp3'))
        self.BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets",'Gun+Silencer.mp3'))

        self.WIDTH, self.HEIGHT = 900,500
        #make the main surface aka the winodw
        self.WINDOW = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("SPACE MULTIPLAYER GAME")

        self.YELLOW_HIT = pygame.USEREVENT+1
        self.RED_HIT = pygame.USEREVENT+2

        self.HEALTH_FONT = pygame.font.SysFont('comicSans',40)
        self.WINNER_FONT = pygame.font.SysFont('comicSans',100)
        self.WHITE = (255,255,255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.PURPLE = (128, 0, 128)
        self.ORANGE = (255, 165, 0)
        self.PINK = (255, 192, 203)
        self.GRAY = (128, 128, 128)

        self.BORDER = pygame.Rect(self.WIDTH//2-5,0,10,self.HEIGHT)

        #frames per second, instead of using loop
        self.FPS = 60
        self.VELOCITY = 5
        self.BULLET_VELOCITY = 5
        self.MAX_BULLETS = 3

        self.SPACESHIP_WIDHT = 55
        self.SPACESHIP_HEIGHT = 40



        #ge the image, us the os object because in diffrent operating system use diffrent path
        self.YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
        #resize the yellow spaceship
        self.YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(self.YELLOW_SPACESHIP_IMG,(self.SPACESHIP_WIDHT,self.SPACESHIP_HEIGHT)),90)

        #rotate the image to x degree



        self.RED_SPACESHIP_IMG = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
        #resize the yellow spaceship
        self.RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(self.RED_SPACESHIP_IMG,(self.SPACESHIP_WIDHT,self.SPACESHIP_HEIGHT)),270)

        self.SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets",'space.jpeg')),(self.WIDTH,self.HEIGHT))
    def draw_winner(self,text):
        draw_text = self.WINNER_FONT.render(text,1,self.WHITE)
        self.WINDOW.blit(draw_text,(self.WIDTH/2 - draw_text.get_width() /2,self.HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000)
    def draw_window(self,red,yellow,red_bullet, yellow_bullet, red_health, yellow_health):
        #the order matters
        # set the background of the winodw to white
        self.WINDOW.blit(self.SPACE,(0,0))
        pygame.draw.rect(self.WINDOW, self.BLACK, self.BORDER)
        self.red_health_text = self.HEALTH_FONT.render("Health: " + str(red_health),1,self.PURPLE)
        self.yellow_health_text = self.HEALTH_FONT.render("Health: " + str(yellow_health), 1, self.PURPLE)
        self.WINDOW.blit(self.red_health_text,(self.WIDTH-self.red_health_text.get_width()-10,10))
        self.WINDOW.blit(self.yellow_health_text, (10, 10))

        #add spaceship to the window using blit keyword
        #
        self.WINDOW.blit(self.YELLOW_SPACESHIP,(yellow.x,yellow.y))
        self.WINDOW.blit(self.RED_SPACESHIP,(red.x, red.y))

        for bullet in red_bullet:
            pygame.draw.rect(self.WINDOW,self.RED, bullet)

        for bullet in yellow_bullet:
            pygame.draw.rect(self.WINDOW,self.YELLOW, bullet)


        # update the display
        pygame.display.update()

    def handle_ship_movement(self,keys_pressed,yellow,red):
        # if keys that are pressed is 'a' move to the left, change the x coordinate of yellow spaceship to the
        # value of VELOCITY, in the while loop when the user press the a keyboard, the program will subract VELOCITY value
        # of the x coordinate of the yellow spaceship
        # same applies for the up,down, right

        if keys_pressed[pygame.K_a] and yellow.x - self.VELOCITY>0:  # LEFT
            yellow.x -= self.VELOCITY

        if keys_pressed[pygame.K_d] and yellow.x + self.VELOCITY< self.BORDER.x -30:  # RIGHT
            yellow.x += self.VELOCITY

        if keys_pressed[pygame.K_w] and yellow.y - self.VELOCITY>0:  # UP
            yellow.y -= self.VELOCITY

        if keys_pressed[pygame.K_s] and yellow.y + self.VELOCITY <self.HEIGHT - 50:  # DOWN
            yellow.y += self.VELOCITY

        if keys_pressed[pygame.K_LEFT] and red.x - self.VELOCITY >self.BORDER.x:  # LEFT
            red.x -= self.VELOCITY

        if keys_pressed[pygame.K_RIGHT] and red.x + self.VELOCITY < self.WIDTH -30:  # RIGHT
            red.x += self.VELOCITY

        if keys_pressed[pygame.K_UP] and red.y - self.VELOCITY >0:  # UP
            red.y -= self.VELOCITY

        if keys_pressed[pygame.K_DOWN] and red.y + self.VELOCITY< self.HEIGHT - 50:  # DOWN
            red.y += self.VELOCITY


    def handle_bullets(self,yellow_bullets,red_bullets, yellow,red):
        for bullet in yellow_bullets:
            bullet.x += self.BULLET_VELOCITY
            #check is bullet collides with the red bullet
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.RED_HIT))
                yellow_bullets.remove(bullet)
            elif bullet.x > self.WIDTH:
                yellow_bullets.remove(bullet)


        for bullet in red_bullets:
            bullet.x -= self.BULLET_VELOCITY
            # check is bullet collides with the red bullet
            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.YELLOW_HIT))
                red_bullets.remove(bullet)
            elif bullet.x < 0:
                red_bullets.remove(bullet)

    def main(self):
        #
        self.red = pygame.Rect(700,300,self.SPACESHIP_WIDHT,self.SPACESHIP_HEIGHT)
        self.yellow = pygame.Rect(100, 300, self.SPACESHIP_WIDHT, self.SPACESHIP_HEIGHT)

        yellow_bullets = []
        red_bullets = []

        red_health = 10
        yellow_health =10

        clock = pygame.time.Clock()
        run = True
        #make sure we run this while loop at FPS
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and len(yellow_bullets)<self.MAX_BULLETS:
                        # draw bullet
                        bullet = pygame.Rect(self.yellow.x + self.yellow.width, self.yellow.y + self.yellow.height//2-2, 10,5)
                        yellow_bullets.append(bullet)
                        self.BULLET_FIRE_SOUND.play()
                    if event.key == pygame.K_m and len(red_bullets)<self.MAX_BULLETS:
                        bullet = pygame.Rect(self.red.x , self.red.y + self.yellow.height // 2 - 2, 10, 5)
                        red_bullets.append(bullet)
                        self.BULLET_FIRE_SOUND.play()
                if event.type == self.RED_HIT:
                    red_health-=1
                    self.BULLET_HIT_SOUND.play()
                if event.type == self.YELLOW_HIT:
                    self.BULLET_HIT_SOUND.play()
                    yellow_health-=1
            winner_text = ""
            if red_health<=0:
                winner_text = "Yellow Wins"
            if yellow_health<=0:
                winner_text = "Red Wins"
            if winner_text != "":
                self.draw_winner(winner_text)
                break


            keys_pressed = pygame.key.get_pressed()
            self.handle_ship_movement(keys_pressed,self.yellow,self.red)

            self.handle_bullets(yellow_bullets,red_bullets, self.yellow,self.red)
            self.draw_window(self.red,self.yellow,red_bullets, yellow_bullets,red_health,yellow_health)

        self.main()


