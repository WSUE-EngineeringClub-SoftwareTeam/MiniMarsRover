#LOGIC CLASS WILL HAVE TWO THINGS
#SERIAL CONTROL CLASS I DEFINE
#GUI CLASS I DEFINE
#LOGIC CLASS WILL PASS FROM SERIAL CLASS TO GUI CLASS
#LOGIC CLASS WILL ALSO HOLD THINGS LIKE "FIGURE 8"


import pygame
import serial


class SerialController:
    #We should be able to select
    #Baud Rate
    #Com port

    #We should also be able to send messages
    # (Chars?) (Strings?) solution: (leave generic)

    def __init__(self):
        self.ser = serial.Serial(timeout=2)
        self.baudrate = 9600
        self.port = 'COM1'

    def config(self, port, baud=9600):
        self.port = port
        self.baud = baud
        self.ser.baudrate = baud
        self.ser.port = port

    def open(self):
        self.ser.open()

    def write(self, message):
        self.ser.write(message)
       # print(message)

class drivingWindow:

    def __init__(self):

        #initalize package for font and pygame
        self.window = pygame.display
        self.open = False
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("andrew yang 2020")
        self.font = pygame.font.SysFont('Comic Sans MS', 18)

        #Small height and width
        self.width = 250
        self.height = 250

        #Set default to stop
        self.recentCommand = 'x'


    #Boot the UI
    def start_up(self):
        self.open = True
        self.window = pygame.display.set_mode((self.width, self.height))
        self.config()

    #Configure buttons
    def config(self):
        self.W_button = pygame.draw.rect(self.window, (0, 0, 240), ((self.width/2)-15, (self.height/2) -65, 30, 30))
        self.A_button = pygame.draw.rect(self.window, (0, 0, 240), ((self.width/2)-55, (self.height/2) -25, 30, 30))
        self.S_button = pygame.draw.rect(self.window, (0, 0, 240), ((self.width/2)-15, (self.height/2) -25, 30, 30))
        self.D_button = pygame.draw.rect(self.window, (0, 0, 240), ((self.width/2)+25, (self.height/2) -25, 30, 30))
        self.X_button = pygame.draw.rect(self.window, (0, 0, 240), ((self.width/2)+25, (self.height/2) +15, 30, 30))
        self.Q_button = pygame.draw.rect(self.window, (0, 0, 240), ((self.width/2)-55, (self.height/2) -65, 30, 30))
        self.E_button = pygame.draw.rect(self.window, (0, 0, 240), ((self.width/2)+25, (self.height/2) -65, 30, 30))
        self.configLetters()

    def configLetters(self):
        W_text = self.font.render('W', False, (222, 222, 100))
        self.window.blit(W_text, (((self.width / 2) - 8), (self.height/2) -60))
        S_text = self.font.render('S', False, (222, 222, 100))
        self.window.blit(S_text, (((self.width / 2) - 8), (self.height/2) -20))
        A_text = self.font.render('A', False, (222, 222, 100))
        self.window.blit(A_text, (((self.width / 2) - 48), (self.height/2) -20))
        D_text = self.font.render('D', False, (222, 222, 100))
        self.window.blit(D_text, (((self.width / 2) + 32),  (self.height/2) -20))
        Q_text = self.font.render('Q', False, (222, 222, 100))
        self.window.blit(Q_text, (((self.width / 2) - 48 ),  (self.height/2) -60))
        E_text = self.font.render('E', False, (222, 222, 100))
        self.window.blit(E_text, (((self.width / 2) +32),  (self.height/2) -60))
        X_text = self.font.render('X', False, (222, 222, 100))
        self.window.blit(X_text, (((self.width / 2) + 32),  (self.height/2) +20))

    #Watch for events, upon certain events change
    #relevant member attributes (probably last button selected)
    def UI_loop(self):
        if(self.open):
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.open = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_w]:
                        self.W_button= pygame.draw.rect(self.window,  (240, 0, 240), ((self.width/2)-15, (self.height/2) -65, 30, 30))
                        self.recentCommand = 'w'
                    if pressed[pygame.K_a]:
                        self.A_button= self.A_button = pygame.draw.rect(self.window, (240, 0, 240), ((self.width/2)-55, (self.height/2) -25, 30, 30))
                        self.recentCommand = 'a'
                    if pressed[pygame.K_s]:
                        self.S_button=pygame.draw.rect(self.window, (240, 0, 240), ((self.width/2)-15, (self.height/2) -25, 30, 30))
                        self.recentCommand = 's'
                    if pressed[pygame.K_d]:
                        self.D_button=pygame.draw.rect(self.window, (240, 0, 240), ((self.width/2)+25, (self.height/2) -25, 30, 30))
                        self.recentCommand = 'd'
                    if pressed[pygame.K_q]:
                        self.Q_button= pygame.draw.rect(self.window, (240, 0, 240), ((self.width/2)-55, (self.height/2) -65, 30, 30))
                        self.recentCommand = 'q'
                    if pressed[pygame.K_e]:
                        self.E_button=pygame.draw.rect(self.window, (240, 0, 240), ((self.width/2)+25, (self.height/2) -65, 30, 30))
                        self.recentCommand = 'e'
                    if pressed[pygame.K_x]:
                        self.X_button=pygame.draw.rect(self.window, (240, 0, 240), ((self.width/2)+25, (self.height/2) +15, 30, 30))
                        self.recentCommand = 'x'
                    self.configLetters()



                if event.type == pygame.KEYUP:
                    self.config()

             pygame.display.flip()


class logicDriver:

    def __init__(self):
        self.UI = drivingWindow()
        self.serial = SerialController()

    def boot(self):
        self.UI.start_up()
        self.serial.config("COM6")
        self.serial.open()

    def loop(self):
        while(self.UI.open):
            # Poll my GUI
            self.UI.UI_loop()
            # Send my serial value as bytes and attempt to write it
            self.serial.write(self.UI.recentCommand.encode())


# Runs our program (The logic class)
program = logicDriver()
program.boot()
program.loop()
