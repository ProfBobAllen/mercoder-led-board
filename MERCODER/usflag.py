###################################################
#  MERCODER  LED  LIGHT  BOARD  PYTHON  TEMPLATE  #
#                                                 #
# Copy this code into a file with .py extension.  #
# Leave the line: from LEDLIB import *  untouched #
# Place your code below the MAIN CODE line below. #
#                                                 #
###################################################

#####################  LEAVE ALONE  ###############
#  This includes all of the LED lights libraries  #
###################################################

from LEDLIB import *


#####################  MAIN  CODE   ###############

setColor(WHITE)  # WHITE background, build rest around this
for col in range(0,18,4):  # Five red stripes (not accurate)
    setColColor(col,RED)
    setColColor(col+1,RED)
makeBox(0,8,10,10,BLUE)

# Add some stars
for row in range(1,8,2):
    for col in range(9,16,2):
        setColorAt(row,col,WHITE)
        setColorAt(row+1,col+1,WHITE)
lights.show()

###  If you want something to repeat, 
###     uncomment the following or write your own loop

#while True:
    #print('Looping through your code.')
    #colorWipeDown(ORANGE)
    #time.sleep(2)
    #colorWipeLR(RED)
    #time.sleep(2)
    #colorWipeDown(BLUE)
    #time.sleep(2)
    #colorWipeLR(GREEN)
    #time.sleep(2)
    #colorWipeDown(DARKBLUE)
    #time.sleep(2)
    #setColor(YELLOW)
    #time.sleep(2)
    #setColor(WHITE)
    #time.sleep(2)
