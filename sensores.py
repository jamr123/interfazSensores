import os
import glob
import time
import os.path as path


class Sensores:
    
    SN1=None
    SN2=None
    SN3=None

    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        listaSensores=glob.glob('/sys/bus/w1/devices/28*')
        if len(listaSensores)>0:
           self.SN1=glob.glob('/sys/bus/w1/devices/28*')[0]
        else:
            self.SN1=None

        if len(listaSensores)>1:
           self.SN2=glob.glob('/sys/bus/w1/devices/28*')[1]
        else:
            self.SN2=None

        if len(listaSensores)>2:
           self.SN3=glob.glob('/sys/bus/w1/devices/28*')[2]
        else:
            self.SN3=None 

        
        
    def read_temp_raw(self,device_file):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
 
    def read_temp(self,device_file):
        lines = self.read_temp_raw(device_file)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw(device_file)
            if lines[0].strip()[-2:] == 'NO':
                break
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c
        return 0

    def readT(self,n):
        t=None
        
        if path.exists(self.SN1):
            if n==1:
                S1 = self.SN1 + '/w1_slave'
                t=self.read_temp(S1)
        else:
            t=None
            
        return t

        

        

        



