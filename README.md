# gyro_turn_on_light
This repository aim for practice to use module MPU6050 3-axis Accelerometer/Gyro Module with raspberry pi for understanding I2C and IMU module.

Pre-install:
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
ref: https://pinout.xyz/pinout/i2c

Pre-config:
raspi-config Tool via Terminal

1.Run sudo raspi-config.
2.Use the down arrow to select 5 Interfacing Options
3.Arrow down to I2C.
4.Select yes when it asks you to enable I2C,
5.Also select yes if it asks about automatically loading the kernel module.
6.Use the right arrow to select the <Finish> button.
7.Select yes when it asks to reboot.
ref: https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all
