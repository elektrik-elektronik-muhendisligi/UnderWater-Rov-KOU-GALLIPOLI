import pygame
import sys
import serial

pygame.init()  
pygame.joystick.init()  

try:
	j = pygame.joystick.Joystick(0)
	j.init() # init instance
	print ("Enabled joystick: {0}".format(j.get_name()))
except pygame.error:
	print ("no joystick found.")

joysticks = [pygame.joystick.Joystick(0) for x in range(pygame.joystick.get_count())]
print (joysticks)

display_width = 800
display_height = 600



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('joystick ile ilgili işlemler')
red = (255, 0, 0)
def gameLoop():
    gameExit = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    while not gameExit:

        block_size = 20
        lead_x_change = 0
        lead_y_change = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('goodbye')
                sys.exit()
            if event.type == pygame.JOYAXISMOTION:  
                if j.get_axis(0) >= 0.5:
                    #print ("right has been pressed")  
                    lead_x_change = block_size
                    lead_y_change = 0
                if j.get_axis(0) <= -1:
                   # print ("left has been pressed")  
                    lead_x_change = -block_size
                    lead_y_change = 0
                    #print (lead_x_change, lead_y_change)

                if j.get_axis(1) >= 0.5:
                    lead_y_change = block_size
                    lead_x_change = 0
                    #print ("Down has been pressed")  
                if j.get_axis(1) <= -1:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    #print ("Up has been pressed")    
                #print(j.get_axis(0))
                #print("Joystick Moved")
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick Button pressed")
                print(j.get_axis(0))

        lead_x += lead_x_change
        lead_y += lead_y_change
        pygame.draw.rect(gameDisplay, red, [lead_x, lead_y , 10, 10])
        pygame.display.update()



gameLoop()

pygame.joystick.quit()
