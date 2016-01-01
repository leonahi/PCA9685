import smbus
import numpy as np
import time
from pca9685_global import *

bus = smbus.SMBus(1)

def PCA9685_Init():
    mode1_mask = 0x00 | PCA9685_MODE1_BITM_AI | PCA9685_MODE1_BITM_SLEEP | PCA9685_MODE1_BITM_ALLCALL
    print(PCA9685_I2C_ADDRESS)
    print(PCA9685_MODE1_REG)
    print(type(mode1_mask))
    
    #data = bus.read_i2c_block_data(0x70, 0x06, 1)
    #print(data)
    
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, PCA9685_MODE1_REG, [48])
    time.sleep(.00005);
    
    # Set frequency to 50 Hz
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, PCA9685_PRE_SCALE, [121]) 
    time.sleep(.0005)
    
    mode1_mask = 0x00 | PCA9685_MODE1_BITM_RESTART | PCA9685_MODE1_BITM_AI | PCA9685_MODE1_BITM_ALLCALL
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, PCA9685_MODE1_REG, [mode1_mask])

    
def PCA9685_SetFreq(channel=0, dutycycle=50):
    on = int(40.95 * dutycycle)
    off = abs(4095 - on)
    on_l = int(np.uint8(on))
    on_h = on >> 8
    off_l = int(np.uint8(off))
    off_h = off >> 8
    print("On : {}".format(on))
    print("Off : {}".format(off))
    print("On_L : {}".format(on_l))
    print("On_H : {}".format(on_h))    
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, (PCA9685_LED0_ON_L + (4*channel)), [0x00])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, (PCA9685_LED0_ON_H + (4*channel)), [0x00])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, (PCA9685_LED0_OFF_L + (4*channel)), [off_l])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, (PCA9685_LED0_OFF_H + (4*channel)), [off_h])
    
def PCA9685_ChangePWM(channel, pwm):
    if pwm > 4096:
        pwm = 0
    elif pwm < 0:
        pwm = 0
        
    off_l = int(np.uint8(pwm))
    off_h = pwm >> 8
    
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, (PCA9685_LED0_ON_L + (4*channel)), [0x00])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, (PCA9685_LED0_ON_H + (4*channel)), [0x00])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, (PCA9685_LED0_OFF_L + (4*channel)), [off_l])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, (PCA9685_LED0_OFF_H + (4*channel)), [off_h])

def PCA9685_AllChannelOff():
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, PCA9685_ALL_LED_ON_L, [0x00])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, PCA9685_ALL_LED_ON_H, [0x00])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, PCA9685_ALL_LED_OFF_L, [0x00])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, PCA9685_ALL_LED_OFF_H, [0x10])

def PCA9685_AllChannelOn():
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, PCA9685_ALL_LED_ON_L, [0x00])
    bus.write_i2c_block_data(PCA9685_I2C_ADDRESS, PCA9685_ALL_LED_ON_H, [0x10])

  #data =  bus.read_i2c_block_data(BMP180_I2C_ADDRESS, BMP180_REGISTER_EEPROM, 22)
  #bus.write_i2c_block_data(BMP180_I2C_ADDRESS, BMP180_REGISTER_CONTROL, [BMP180_COMMAND_TEMPERATURE])


if __name__ == "__main__":
    PCA9685_Init()

    # Small Servo 
    #PCA9685_ChangePWM(13, 114)
    #time.sleep(2)
    
    #PCA9685_ChangePWM(13, 525)
    #time.sleep(2)
    
    """
    for i in range(411):
        PCA9685_ChangePWM(13, 114 + i)
        time.sleep(.005)
    for i in range(411):
        PCA9685_ChangePWM(13, 525 - i)
        time.sleep(.005)
    """
    
    """
    for i in range(400):
        PCA9685_ChangePWM(13, 123 + i)
        time.sleep(.005)
    for i in range(400):
        PCA9685_ChangePWM(13, 523 - i)
        time.sleep(.005)
    
    PCA9685_ChangePWM(13, 323)
    time.sleep(5)
    """
    
    """
    PCA9685_ChangePWM(15, 153)
    #PCA9685_ChangePWM(13, 104)
    time.sleep(3)
    #PCA9685_ChangePWM(15, 154)
    #PCA9685_ChangePWM(13, 204)
    #time.sleep(2)
    PCA9685_ChangePWM(15, 338)
    time.sleep(3)
    PCA9685_ChangePWM(15, 530)
    #PCA9685_ChangePWM(13, 307)
    time.sleep(3)
    """
    """
    time.sleep(2)
    PCA9685_ChangePWM(15, 409)
    #PCA9685_ChangePWM(13, 409)
    time.sleep(2)
    PCA9685_ChangePWM(15, 500)
    #PCA9685_ChangePWM(13, 500)
    time.sleep(2)
    """
  
    """
    time.sleep(2)
    PCA9685_SetFreq(channel=0, dutycycle=5)
    time.sleep(1)
    PCA9685_SetFreq(channel=0, dutycycle=10)
    time.sleep(1)
    PCA9685_SetFreq(channel=0, dutycycle=15)
    time.sleep(1)
    PCA9685_SetFreq(channel=0, dutycycle=20)
    time.sleep(1)
    PCA9685_SetFreq(channel=0, dutycycle=25)
    time.sleep(1)
    PCA9685_SetFreq(channel=0, dutycycle=30)
    time.sleep(1)
    PCA9685_SetFreq(channel=0, dutycycle=35)
    time.sleep(1)
    PCA9685_SetFreq(channel=0, dutycycle=40)
    time.sleep(1)
    PCA9685_SetFreq(channel=0, dutycycle=45)
    time.sleep(1)
    """
    """
    print("Start PWM")
    for i in range(4095):
        print("Done")
        PCA9685_ChangePWM(0, i)
        time.sleep(.001)
    """
    """
    print("Done")
    PCA9685_ChangePWM(0, 100)
    input()
    
    print("Done")
    PCA9685_ChangePWM(0, 11)
    input()
    
    print("Done")
    PCA9685_ChangePWM(0, 12)
    input()
    
    print("Done")
    PCA9685_ChangePWM(0, 13)
    input()
    
    PCA9685_ChangePWM(0, 14)
    input()
    
    PCA9685_ChangePWM(0, 15)
    input()
    """
    PCA9685_AllChannelOff()
    

