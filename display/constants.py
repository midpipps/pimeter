'''
All the constants for the display
'''
from PIL import Image
from PIL import ImageFont

# COMMAND LINE
I2C_COMMAND = "i2cdetect -y 1"
IP_COMMAND = "hostname -I | cut -d \" \" -f1"
DISK_COMMAND = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
WIFI_COMMAND = "iwconfig wlan0 | grep \"Link Quality\" | cut -d\"=\" -f3 | cut -d\" \" -f1"
#COMMAND LINE

#SCREEN DISPLAY CONSTS
RST = 24 #not used on pi oled
TOPBARIMAGE = Image.open('tempprobe.ppm').convert('1')
FONT = ImageFont.load_default()
#CONNECT SIZE IS WIDTH, HEIGHT
CONNECT_SIZE = (16, 16)
CONNECT_ICONS = {
    'A':{
        'address' : 0x48,
        'location' : (0, 0),
        'disconnected' : (0,
                          0,
                          CONNECT_SIZE[0],
                          CONNECT_SIZE[1]),
        'connected' : (0,
                       CONNECT_SIZE[1],
                       CONNECT_SIZE[0],
                       CONNECT_SIZE[1] * 2)
    },
    'B':{
        'address' : 0x49,
        'location' : (CONNECT_SIZE[0] + 1, 0),
        'disconnected' : (CONNECT_SIZE[0],
                          0,
                          CONNECT_SIZE[0] * 2,
                          CONNECT_SIZE[1]),
        'connected' : (CONNECT_SIZE[0],
                       CONNECT_SIZE[1],
                       CONNECT_SIZE[0] * 2,
                       CONNECT_SIZE[1] * 2)
    },
    'C':{
        'address' : 0x4A,
        'location' : ((CONNECT_SIZE[0] * 2) + 2, 0),
        'disconnected' : (CONNECT_SIZE[0] * 2,
                          0,
                          CONNECT_SIZE[0] * 3,
                          CONNECT_SIZE[1]),
        'connected' : (CONNECT_SIZE[0] * 2,
                       CONNECT_SIZE[1],
                       CONNECT_SIZE[0] * 3,
                       CONNECT_SIZE[1] * 2)
    },
    'D':{
        'address' : 0x4B,
        'location' : ((CONNECT_SIZE[0] * 3) + 3, 0),
        'disconnected' : (CONNECT_SIZE[0] * 3,
                          0,
                          CONNECT_SIZE[0] * 4,
                          CONNECT_SIZE[1]),
        'connected' : (CONNECT_SIZE[0] * 3,
                       CONNECT_SIZE[1],
                       CONNECT_SIZE[0] * 4,
                       CONNECT_SIZE[1] * 2)
    }
}
#END CONNECT

#START WIFI
WIFI_START = 100
WIFI_FIL = CONNECT_SIZE[0] * 4
WIFI_SIZE = (4, 16)
WIFI_ICONS = {
    -95 : {
        'location' : (WIFI_START, 0),
        'inactive' : (WIFI_FIL,
                      0,
                      WIFI_FIL + WIFI_SIZE[0],
                      WIFI_SIZE[1]),
        'active' : (WIFI_FIL,
                    WIFI_SIZE[1],
                    WIFI_FIL + WIFI_SIZE[0],
                    WIFI_SIZE[1] * 2)
    },
    -85 : {
        'location' : (WIFI_START + WIFI_SIZE[0] + 1, 0),
        'inactive' : (WIFI_FIL + WIFI_SIZE[0],
                      0,
                      WIFI_FIL + (WIFI_SIZE[0] * 2),
                      WIFI_SIZE[1]),
        'active' : (WIFI_FIL + WIFI_SIZE[0],
                    WIFI_SIZE[1],
                    WIFI_FIL + (WIFI_SIZE[0] * 2),
                    WIFI_SIZE[1] * 2)
    },
    -75 : {
        'location' : (WIFI_START + (WIFI_SIZE[0] * 2) + 2, 0),
        'inactive' : (WIFI_FIL + (WIFI_SIZE[0] * 2),
                      0,
                      WIFI_FIL + (WIFI_SIZE[0] * 3),
                      WIFI_SIZE[1]),
        'active' : (WIFI_FIL + (WIFI_SIZE[0] * 2),
                    WIFI_SIZE[1],
                    WIFI_FIL + (WIFI_SIZE[0] * 3),
                    WIFI_SIZE[1] * 2)
    },
    -65 : {
        'location' : (WIFI_START + (WIFI_SIZE[0] * 3) + 3, 0),
        'inactive' : (WIFI_FIL + (WIFI_SIZE[0] * 3),
                      0,
                      WIFI_FIL + (WIFI_SIZE[0] * 4),
                      WIFI_SIZE[1]),
        'active' : (WIFI_FIL + (WIFI_SIZE[0] * 3),
                    WIFI_SIZE[1],
                    WIFI_FIL + (WIFI_SIZE[0] * 4),
                    WIFI_SIZE[1] * 2)
    }
}
#END WIFI
