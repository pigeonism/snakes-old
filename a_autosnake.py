import pygame
from random import randint
#from time import gmtime, strftime

# Autosnake [b_autosnake.key_nav()] for auto mode
#import b_autosnake

class Base(object):

    def __init__(self):
        # env variables
        print("Base class init")
        # colours, black and white for now
        self.BLACK = [0,0,0,0]
        self.WHITE = [255,255,255,255]
        
        self.speed_mod = "D" # initially down, or maybe random later    
        self.mod_accel = 10
        # a rect [x,y, width, height]
        self.coords =[0,0]
        self.squares = [[self.coords[0],self.coords[1],10,10]]
        self.loop = True
        
        self.screen_size = [600,600]

        self.collide_check = True   

    def add_square(self):  # called by timer & space
        #squares.append( squares[:-1] + ....   ) # add a new one that copies the information of ONLY the final square
        self.squares.append([self.squares[0][0], self.squares[0][1],10,10])

    def del_square(self): # cheat function to shorten tail.
        del self.squares[-1]
        
        print("ouch")

    #def u_turn(self): # another cheat for sharp turns using autosnake module
        # read current direction from self.speed_mod, pass this to autosnake and it will sharp turn in opposite direction

        # also find which half we're in later and pass that information too [ & where other squares are ]
        #b_autosnake.key_nav(self.speed_mod) # string U D L R

    def save_coordinates(self, data): # record on quit the time until collision and coordinates
        #self.time_c = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        
        f = open("plots", 'a')
        f.write("#START\n")
        for i in range( len(data) ):
            f.write(str(data[i])+"\n")
        f.write("#END\n")
        f.close()

    # load a previous sequence and watch, see
    def replay(self):
        # count how many 'START' flags, data inbetween start and end is moved into a list or draw them all?
        f = open("plots", 'r')
        mass_squares = f.read() # while getline str != END, newsquares.append( getlines[i] )  
        f.close()
        session = mass_squares[mass_squares.find("START"):mass_squares.find("END")]
        print(session)
        print(type(session))

    def run(self): # MAIN

        pygame.init()

        screen = pygame.display.set_mode(self.screen_size) # -32

        pygame.display.set_caption("My Snakes ")

        #screen.set_colorkey(self.WHITE,0) # transparency test
        #screen.convert_alpha()


        #print pygame.display.Info()
        #print pygame.display.get_driver()

        # initially add squares every few seconds, then change to only add new squares when a parcel is collected
        clock = pygame.time.Clock()

        while  self.loop:

            # limit to 10 times per second
            clock.tick(10)
            

            #logic TEMP speed modifier also based on key press. modify after drawing to avoid skip in line
            if self.speed_mod == "U": self.squares[0][1] -= self.mod_accel
            if self.speed_mod == "D": self.squares[0][1] += self.mod_accel
            if self.speed_mod == "L": self.squares[0][0] -= self.mod_accel
            if self.speed_mod == "R": self.squares[0][0] += self.mod_accel


            # event loop, change loop flag if quit.
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT:
                     self.loop = False # Flag that we are done so we exit this loop

                if event.type == pygame.KEYDOWN:
                    print("K_UP here afhdskjghaj")
                    #print pygame.key.name(0), "sljfslkdfj"
                    if event.key == pygame.K_UP:
                        self.add_square()
                        self.speed_mod = "U"
                        print("KEY UP PRESSED")
                        self.squares[0][1] -= 10 # temp
                    if event.key == pygame.K_DOWN:
                        self.add_square()
                        self.speed_mod = "D"
                        print("KEY DOWN PRESSED")
                        # change y, add to y of squares
                        self.squares[0][1] += 10 # temp
                    if event.key == pygame.K_RIGHT:
                        self.add_square()
                        self.speed_mod = "R"
                        print("RIGHT ARROW PRESSED")
                        self.squares[0][0] += 10
                        #self.squares[0].move_ip(10)
                    if event.key == pygame.K_LEFT:
                        self.add_square()
                        self.speed_mod = "L"
                        print("LEFT ARROW PRESSED")
                        self.squares[0][0] -= 10

                    # callng Cheat functions
                    # key space is TEST FOR ADD SQUARE FUNCTION
                    if event.key == pygame.K_SPACE:
                        # removing square to create a gap to slip through later
                        self.del_square()
                        #print self.squares
                        print("cheat!")
                    #if event.key == pygame.K_t:
                        # quick turn, needs improvement
                        #self.u_turn()
                        #print "T PRESSED U TURNING"
                    #if event.key == pygame.K_c:
                        # cross over path
                        #print "Crossing pathway mode"
                        #self.collide_check = not self.collide_check 
                        #print "flag is: ", self.collide_check
            # IF Collide
            # exp
            if self.collide_check:
                for i in range(1,len(self.squares) ):
            
                    if self.squares[0][0]  == self.squares[i][0] and self.squares[0][1] == self.squares[i][1]:
                        # PLAY game over sound
                        #self.squares = [[self.screen_size[0] /2,self.screen_size[1] / 2,10,10]]
                        print("COLLISION ")
                        # save pic of screen
                        pygame.image.save(screen, "failbin/fail"+str( randint(0, 100))+str( randint(0, 1000))+".png" )
                        # die
                        print(self.squares[-1][0] * self.squares[-1][1])
                        self.loop = False

                    elif self.squares[0][0] < 0:
                        #print "bounds negative x direction, bye."
                        self.loop = False
                    elif self.squares[0][0] > self.screen_size[0]:
                        #print "bounds positive x, bigger than screen, bye."
                        self.loop = False
                    elif self.squares[0][1] > self.screen_size[1]:
                        self.loop = False
                    elif self.squares[0][1] < 0:
                        self.loop = False
            
            # see space key press called add square. IF parcel found call add_square(), so collision function here instead
            self.add_square()

            # fill screen
            screen.fill(self.WHITE)

            # draw, read the squares list, draw each one
    
            # if not replay:

            # one cube, next cube a multiple expressed in position, same dimension
            # pygame.draw.rect(screen,black,[20,20,250,100],2) 
            for i in range( len( self.squares) ): pygame.draw.rect(screen,  self.BLACK,  self.squares[i])

            
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
        
        # save
        self.save_coordinates(self.squares)
        self.replay()
        # quit
        pygame.quit()

snakes = Base()
snakes.run()
