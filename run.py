'''
The running things here
'''
import time
from display.screen import Screen
def main():
    '''
    run the program and keep everything updating and going
    '''
    thescreen = Screen()
    for i in range(0, 10):
        thescreen.updaterunning()
        time.sleep(.05)
    thescreen.cleardisplay()

if __name__ == '__main__':
    main()
