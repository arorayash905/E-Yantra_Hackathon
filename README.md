# E-Yantra_Hackathon
# Kritrim Intelligence IoT Yantra
## We are designing an IoT kit based on various sensor and a computer vision solution to fight against Covid-19. 
### 1- We are using DHT11 for measuring Humidity and temperature for the patient's room.
### 2- LM35 sensor for patient’s body temperature and SCD30 for measuring various gas availability in the patient's room.
### 3- We also design an untouchable sanitiser dispenser using ultrasonic HC-SR04 and a servo motor to dispense the sanitiser. 
## On the other hand, we also write two programs in python 3 for real-time mask detection and CCTV footage processing for social distancing between two or more people in the hospital and other premises.

![Plot](https://github.com/arorayash905/E-Yantra_Hackathon/blob/main/plot.png)
####              Learning and Testing curve of Mask Detection

![Social Distancing](https://github.com/arorayash905/E-Yantra_Hackathon/blob/main/output.gif)
#### University premises CCTV Phootage shows risk factor between persons
## To processing various sensors data in a single frame. We are using HTML and Django web framework for python in which we listed three buttons for each sensor. Named as Room Temperature, Body Temperature and Gas detection to run the program simultaneously.
### A button that initialises our program of sensor DHT 11 and the data received from DHT 11 will be saved under a CSV format file which again used by: Matplotlib.pyplot to plot a real-time graph of the temperature, be it room temperature or a body temperature of the patients

## Environment
### Programming Languages: Python3 and HTML, C++
### Packages and Library: Tensorflow, Numpy, Matplotlib, OpenCV, utils, Yolo V3, Coco(Datasets), Django
### Hardware Components: Raspberry Pi 3/4, Pi camera/USB Camera or CCTV, Servo Motor.
### Sensors: DHT11, LM35, SCD30, HC-SR04
