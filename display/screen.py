'''
class for keeping the screen up to date
'''
import datetime
import subprocess
import Adafruit_SSD1306 #Oled screen
from PIL import Image
from PIL import ImageDraw
import display.constants as constants

class Screen(object):
    '''
    do output to screen and keep everything up to date
    '''
    def __init__(self):
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=constants.RST, i2c_address=0x3C, i2c_bus=1)
        self.disp.begin() #initialize display
        self.disp.clear()
        self.disp.display()
        self.image = Image.new('1', (self.disp.width, self.disp.height))
        self.draw = ImageDraw.Draw(self.image)

    def _resetdrawimage(self):
        '''
        reset the image and the draw
        '''
        self.draw.rectangle((0, 0, self.disp.width, self.disp.height),
                            outline=0,
                            fill=0)

    def _updateconnections(self):
        '''
        update the screen with connected adcs on the i2c bus
        '''
        i2cdata = subprocess.check_output(constants.I2C_COMMAND, shell=True)\
                            .decode('UTF-8').replace('\n', '')

        for val in constants.CONNECT_ICONS.values():
            if hex(val['address']).replace('0x', '') in i2cdata:
                self.image.paste(constants.TOPBARIMAGE.crop(val['connected']),
                                 box=val['location'])
            else:
                self.image.paste(constants.TOPBARIMAGE.crop(val['disconnected']),
                                 box=val['location'])

    def _updatewifi(self):
        '''
        get the wifi db and update the bar graph
        '''
        signal_db = subprocess.check_output(constants.WIFI_COMMAND, shell=True)\
                            .decode('UTF-8').replace('\n', '')
        try:
            signal_db = int(signal_db)
        except ValueError:
            signal_db = -150

        for key, val in constants.WIFI_ICONS.items():
            if signal_db > key:
                self.image.paste(constants.TOPBARIMAGE.crop(val['active']), box=val['location'])
            else:
                self.image.paste(constants.TOPBARIMAGE.crop(val['inactive']), box=val['location'])

    def _updateother(self):
        '''
        update all the other information such
        datetime
        ip address
        diskspace
        '''
        ipadd = subprocess.check_output(constants.IP_COMMAND, shell=True) \
                          .decode('UTF-8').replace('\n', '')
        disk = subprocess.check_output(constants.DISK_COMMAND, shell=True) \
                         .decode('UTF-8').replace('\n', '')

        # Write two lines of text.
        self.draw.text((0, constants.CONNECT_SIZE[1]),
                       datetime.datetime.now().strftime("%m/%d/%Y %H:%M"),
                       font=constants.FONT,
                       fill=255)
        self.draw.text((0, constants.CONNECT_SIZE[1] + 16),
                       "IP: " + str(ipadd),
                       font=constants.FONT,
                       fill=255)
        self.draw.text((0, constants.CONNECT_SIZE[1] + 32),
                       str(disk),
                       font=constants.FONT,
                       fill=255)

    def updaterunning(self):
        '''
        update the display with the latest information
        '''
        # Draw a black filled box to clear the image.
        self._resetdrawimage()
        self._updateconnections()
        self._updatewifi()
        self._updateother()
        self.disp.image(self.image)
        self.disp.display()

    def cleardisplay(self):
        '''
        clear the display
        '''
        self.disp.clear()
        self.disp.display()
