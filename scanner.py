# Feed angle distance pairs to arduino

import os
from sweeppy import Sweep
import serial
import time


class Scanner():
    START_BYTE = '$'
    END_BYTE   = '!'

    ANGLE_BYTES = 3     # ok for 6 digits
    DISTANCE_BYTES = 3  # ok for 5 digits
    SCAN_FORMAT = '{}%0{}d/%0{}d{}'.format(START_BYTE,ANGLE_BYTES, DISTANCE_BYTES, END_BYTE)

    def sampleBytes(self, angle, distance):
        return bytes(Scanner.START_BYTE, 'utf-8') \
               + angle.to_bytes(Scanner.ANGLE_BYTES, byteorder='little') \
               + distance.to_bytes(Scanner.DISTANCE_BYTES, byteorder='little') \
               + bytes(Scanner.END_BYTE, 'utf-8')

    def run(self):

        ACM_Port = 0
        while not os.path.exists('/dev/ttyACM%d' % ACM_Port):
            ACM_Port += 1

        USBTTY_Port = 0
        while not os.path.exists('/dev/ttyUSB%d' % USBTTY_Port):
            USBTTY_Port += 1

        ser = serial.Serial('/dev/ttyACM%d' % ACM_Port, 9600) #, parity=serial.PARITY_EVEN)
        with Sweep('/dev/ttyUSB%d' % USBTTY_Port) as sweep:
            sweep.start_scanning()
            for scan in sweep.get_scans():
                for s in scan.samples:
                    print(Scanner.SCAN_FORMAT % (s.angle, s.distance))
                    ser.write(self.sampleBytes(s.angle, s.distance))
                    time.sleep(.05)

if __name__ == '__main__':
    s = Scanner()
    s.run()
