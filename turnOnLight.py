import readSensor as rs
import time

if __name__ == "__main__":
    light = 0 #define 0 to be off
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
                time.sleep(1.5)
            elif(angle_x < - 20 and light):
                print("turn light OFF")
                light = 0
                time.sleep(1.5)
        except KeyError:
            time.sleep(1.5)
            rs.initial_sensor_module()
