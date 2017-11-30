# Feed angle distance pairs to arduino

import os
from sweeppy import Sweep
import serial
import time

START_BYTE = '$'
END_BYTE   = '!'

ANGLE_BYTES = 6
DISTANCE_BYTES = 5
SCAN_FORMAT = '{}%0{}d/%0{}d{}'.format(START_BYTE,ANGLE_BYTES, DISTANCE_BYTES, END_BYTE)

ACM_Port = 0
while not os.path.exists('/dev/ttyACM%d' % ACM_Port):
    ACM_Port += 1

USBTTY_Port = 0
while not os.path.exists('/dev/ttyUSB%d' % USBTTY_Port):
    USBTTY_Port += 1

ser = serial.Serial('/dev/ttyACM%d' % ACM_Port, 9600, parity=serial.PARITY_EVEN)
with Sweep('/dev/ttyUSB%d' % USBTTY_Port) as sweep:
    sweep.start_scanning()
    for scan in sweep.get_scans():
        for s in scan.samples:
            print(SCAN_FORMAT % (s.angle, s.distance))
            ser.write(bytes(SCAN_FORMAT % (s.angle, s.distance), 'utf-8'))
            time.sleep(.05)
