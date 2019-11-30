import os
import glob
import time


class Sensores:
    S1=None
    S2=None
    S3=None
    

    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        
         

        
        
    def read_temp_raw(self,device_file):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
 
    def read_temp(self,device_file):
        lines = read_temp_raw(device_file)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c

    def readT(slef,n):
        t=0
        if n==1:
            if glob.glob('/sys/bus/w1/devices/28*')[0]:
                carpetaS1 = glob.glob(self.rootSensores + '28*')[0]
                self.S1 = carpetaS1 + '/w1_slave'
                t=read_temp(S1)
        elif n==2:
            if glob.glob('/sys/bus/w1/devices/28*')[1]:
                carpetaS2 = glob.glob(self.rootSensores + '28*')[1]
                self.S2 = carpetaS2 + '/w1_slave'
                t=read_temp(S2)
        elif n==3:
            if glob.glob('/sys/bus/w1/devices/28*')[2]:
                carpetaS3 = glob.glob(self.rootSensores + '28*')[2]
                self.S3 = carpetaS3 + '/w1_slave'
                t=read_temp(S3)
        return t

        

        

        



