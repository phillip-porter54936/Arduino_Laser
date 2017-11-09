# Test sending laser data to arduino


from sweeppy import Sweep
import serial

import time

ser = serial.Serial('/dev/ttyACM1', 9600)

with Sweep('/dev/ttyUSB1') as sweep:
    sweep.start_scanning()

    for scan in sweep.get_scans():
        ser.write(bytes('{}'.format(scan), 'utf-8'))
        time.sleep(5)