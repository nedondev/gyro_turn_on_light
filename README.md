# gyro_turn_on_light
This repository aim for practice to use module MPU6050 3-axis Accelerometer/Gyro Module with raspberry pi for understanding I2C and IMU module.

Pre-install:
sudo apt-get install i2c-tools
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

checking IMU address:
sudo i2cdetect -y 1\
for MPU 6050 default at 0x68

reference :
YazarKerem İzgöl."Raspberry Pi 3 İle MPU6050 İvmeölçer/Jiroskop Kullanımı #17"
    Available: https://maker.robotistan.com/raspberry-pi-dersleri-16-mpu6050-ivmeolcerjiroskop-kullanimi/?utm_source=youtube&utm_medium=aciklama&utm_campaign=python_mpu6050
