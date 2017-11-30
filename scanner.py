# Feed angle distance pairs to arduino

import os
from sweeppy import Sweep
import serial
import time

class Scanner():
    SAMPLE_RATE = 32

    START_BYTE = '$'
    END_BYTE   = '!'

    ANGLE_BYTES = 6
    DISTANCE_BYTES = 5
    SCAN_FORMAT = '{}%0{}d/%0{}d{}'.format(START_BYTE,ANGLE_BYTES, DISTANCE_BYTES, END_BYTE)

    def run(self):
        ACM_Port = 0
        while not os.path.exists('/dev/ttyACM%d' % ACM_Port):
            ACM_Port += 1

        USBTTY_Port = 0
        while not os.path.exists('/dev/ttyUSB%d' % USBTTY_Port):
            USBTTY_Port += 1

        ser = serial.Serial('/dev/ttyACM%d' % ACM_Port, 9600, parity=serial.PARITY_EVEN)
        with Sweep('/dev/ttyUSB%d' % USBTTY_Port) as sweep:
            sweep.set_sample_rate(Scanner.SAMPLE_RATE)
            sweep.start_scanning()

            for scan in sweep.get_scans():
                print(len(scan.samples))
                for s in scan.samples:
                    print(Scanner.SCAN_FORMAT % (s.angle, s.distance))
                    ser.write(bytes(Scanner.SCAN_FORMAT % (s.angle, s.distance), 'utf-8'))
                    time.sleep(.05)

if __name__ == '__main__':
    s = Scanner()
    s.run()
