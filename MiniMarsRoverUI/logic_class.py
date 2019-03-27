#LOGIC CLASS WILL HAVE TWO THINGS
#SERIAL CONTROL CLASS I DEFINE
#GUI CLASS I DEFINE
#LOGIC CLASS WILL PASS FROM SERIAL CLASS TO GUI CLASS
#LOGIC CLASS WILL ALSO HOLD THINGS LIKE "FIGURE 8"


import pygame as pg
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
        self.window = pg.display
        self.open = False
        pg.init()
        pg.font.init()
        pg.display.set_caption("MiniRover Controller")
        self.font = pg.font.SysFont('Comic Sans MS', 18)


        #Small height and width
        self.width = 640
        self.height = 480

        #Set default to stop
        self.recentCommand = 'x'


    #Boot the UI
    def start_up(self):
        self.open = True
        self.window = pg.display.set_mode((self.width, self.height))
        self.window.fill(pg.Color("dodgerblue2"))
        self.config()

    #Configure buttons
    def config(self):
        self.W_button = pg.draw.rect(self.window, (0, 0, 240), ((self.width/2)-15, (self.height/2) -65, 30, 30))
        self.A_button = pg.draw.rect(self.window, (0, 0, 240), ((self.width/2)-55, (self.height/2) -25, 30, 30))
        self.S_button = pg.draw.rect(self.window, (0, 0, 240), ((self.width/2)-15, (self.height/2) -25, 30, 30))
        self.D_button = pg.draw.rect(self.window, (0, 0, 240), ((self.width/2)+25, (self.height/2) -25, 30, 30))
        self.X_button = pg.draw.rect(self.window, (0, 0, 240), ((self.width/2)+25, (self.height/2) +15, 30, 30))
        self.Q_button = pg.draw.rect(self.window, (0, 0, 240), ((self.width/2)-55, (self.height/2) -65, 30, 30))
        self.E_button = pg.draw.rect(self.window, (0, 0, 240), ((self.width/2)+25, (self.height/2) -65, 30, 30))
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
             for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.open = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    pressed = pg.key.get_pressed()
                    mods = pg.key.get_mods()
                    if pressed[pg.K_w]:
                        self.W_button= pg.draw.rect(self.window,  (240, 0, 240), ((self.width/2)-15, (self.height/2) -65, 30, 30))
                        self.recentCommand = 'w'
                        print(pressed[pg.K_w])
                    if pressed[pg.K_a]:
                        self.A_button= self.A_button = pg.draw.rect(self.window, (240, 0, 240), ((self.width/2)-55, (self.height/2) -25, 30, 30))
                        self.recentCommand = 'a'
                    if pressed[pg.K_s]:
                        self.S_button=pg.draw.rect(self.window, (240, 0, 240), ((self.width/2)-15, (self.height/2) -25, 30, 30))
                        self.recentCommand = 's'
                    if pressed[pg.K_d]:
                        self.D_button=pg.draw.rect(self.window, (240, 0, 240), ((self.width/2)+25, (self.height/2) -25, 30, 30))
                        self.recentCommand = 'd'
                    if pressed[pg.K_q]:
                        self.Q_button= pg.draw.rect(self.window, (240, 0, 240), ((self.width/2)-55, (self.height/2) -65, 30, 30))
                        self.recentCommand = 'q'
                    if pressed[pg.K_e]:
                        self.E_button=pg.draw.rect(self.window, (240, 0, 240), ((self.width/2)+25, (self.height/2) -65, 30, 30))
                        self.recentCommand = 'e'
                    if pressed[pg.K_x]:
                        self.X_button=pg.draw.rect(self.window, (240, 0, 240), ((self.width/2)+25, (self.height/2) +15, 30, 30))
                        self.recentCommand = 'x'
                    self.configLetters()



                if event.type == pg.KEYUP:
                    #This makes the car stop when you letgo of a button. Seems reasonable.
                    self.recentCommand = 'x'
                    self.config()

             pg.display.flip()

class loginScreen:

    def __init__(self):
        self.active = False
        self.current_text = "COM?"
        self.done = False
        self.valid_input = ''
        self.error_found = False
        self.error_text = ''

    def boot(self):
        pg.font.init()
        pg.init()
        self.screen = pg.display.set_mode((640, 480))
        self.width=480
        self.height=640
        self.font = pg.font.SysFont('arialrounded', 24)
        self.help_font = pg.font.SysFont('arialrounded', 16)
        self.clock = pg.time.Clock()
        self.input_box = pg.Rect(100, 150, 140, 32)
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.color = self.color_inactive
        pg.display.set_caption("MiniRover Controller")




    def loop(self):
        while not self.done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if self.input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        self.active = not self.active
                    else:
                        self.active = False
                    # Change the current color of the input box.
                    self.color = self.color_active if self.active else self.color_inactive
                if event.type == pg.KEYDOWN:
                    if self.active:
                        if event.key == pg.K_RETURN:
                            self.confirm_input(self.current_text)
                            self.current_text = ''
                        elif event.key == pg.K_BACKSPACE:
                            self.current_text = self.current_text[:-1]
                        else:
                            self.current_text += event.unicode

            self.screen.fill((30, 30, 30))
            # Render the current text.
            txt_surface = self.font.render(self.current_text,True, self.color)
            help_text_line1 = self.help_font.render("Hello! you need to enter a valid COM port into this box",True, self.color)
            self.screen.blit(help_text_line1, (self.input_box.x, self.input_box.y+50))
            help_text_line2 = self.help_font.render("Click the box to begin typing, press enter to try a com port.",True, self.color)
            self.screen.blit(help_text_line2, (self.input_box.x, self.input_box.y+65))
            help_text_line3 = self.help_font.render("EXAMPLE VALID INPUT: COM1 COM2 COM6",True, self.color)
            self.screen.blit(help_text_line3, (self.input_box.x, self.input_box.y-30))
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            self.input_box.w = width
            # Blit the text.
            self.screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
            # Blit the input_box rect.
            pg.draw.rect(self.screen, self.color, self.input_box, 2)
            if self.error_found:
                failed_com_text = self.help_font.render(self.error_text[0:90],True, self.color)
                self.screen.blit(failed_com_text, (50,50))
            pg.display.flip()
            self.clock.tick(30)

    # Ensure the chosen com port can reached before leaving login screen
    def confirm_input(self, user_input):
        if 3 < len(user_input) < 5:
            if user_input[0] == 'C':
                try:
                    int(user_input[3])
                    self.valid_input = user_input
                    test_serial = serial.Serial()
                    test_serial.baudrate = 9600
                    test_serial.port = self.valid_input
                    try:
                        test_serial.open()
                        test_serial.close()
                        self.done = True
                    except Exception as e:
                        print(e)
                        self.error_found = True
                        self.error_text = str(e)
                except:
                    return

class logicDriver:

    def __init__(self):
        self.drive_screen = drivingWindow()
        self.serial = SerialController()
        self.login_screen = loginScreen()
        self.valid_input = ''

    def boot_login(self):
        self.login_screen.boot()
        self.login_screen.loop()
        self.valid_input = self.login_screen.valid_input

    def boot_controller(self):
        self.drive_screen.start_up()
        self.serial.config(self.valid_input)
        self.serial.open()


    def loop(self):
        while(self.drive_screen.open):
            # Poll my GUI
            self.drive_screen.UI_loop()
            # Send my serial value as bytes and attempt to write it
            self.serial.write(self.drive_screen.recentCommand.encode())

# Runs our program (The logic class)

program = logicDriver()
program.boot_login()
program.boot_controller()
program.loop()




