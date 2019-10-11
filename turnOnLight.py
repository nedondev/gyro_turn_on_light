import readSensor as rs
import time
import RPi.GPIO as GPIO

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(7, GPIO.OUT)
    light = 0 #define 0 to be off
    GPIO.output(7, light)
    rs.initial_sensor_module()
    print(rs.started)
    while(True):
        try:
            data = rs.read_filtered_out()
            angle_x = data['angle_x']
            angle_y = data['angle_y']
            angle_z = data['angle_z']
            print("angle_x: %f, angle_y: %f, angle_z: %f"\
                %(angle_x, angle_y, angle_z))
            if(angle_x > 20 and not light):
                print("turn light ON")
                light = 1
                GPIO.output(7, light)
                time.sleep(0.5)
            elif(angle_x < - 20 and light):
                print("turn light OFF")
                light = 0
                GPIO.output(7, light)
                time.sleep(0.5)
        #occur when IOError
        except TypeError:
            time.sleep(1.5)
            rs.initial_sensor_module()
        except KeyboardInterrupt:
                print("Clenning...")
            GPIO.cleanup() # this ensures a clean exit 
            exit()
