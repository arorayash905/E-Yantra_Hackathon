Django based python script
This is a Python script on clicking HTML button | Script Output on Html 

Here we are creating a button which intialise our program of sensor DHT 11 
and the data received from DHT 11 will be saved under a CSV format file which again used by:
Matplotlib.pyplot to plot a real time graph of the temperature, be it room temperature or a body temperature of the patients

Basically I created three files in button python 

views.py : In this file python script that has to be excuted is written and the button that has to be used for that particular script

urls file: To connect the button with the excutable file named as views.py

Home.html : This html tamplate named as home.html is created for the button to create a simple UI to excute the running of sensor and to retrieve the data from sensor to the admin
at 127.0.0.1:80
in case you want it at your home network then use apache to achieve it in your LAN based url.
