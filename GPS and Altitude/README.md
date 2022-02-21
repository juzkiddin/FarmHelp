# GPS and Altitude
    To get the GPS coordinate of the pepper plant and the altitude at which a peppercorn
    or disease is detected we need a device to provide us with these data. For that, we 
    use the NEO-6M GPS module and to extract the data from the module we need a microcontroller
    for that purpose we use the ESP8266 NodeMCU. NodeMCU has an inbuilt Wifi Modem that allows us
    to create a Web Server within the microcontroller and access the data from it using the
    IP address of the NodeMCU when it is connected to the assigned Wifi Network. Then we use a
    Python program to connect to the NodeMCU via its IP Address and obtain the required data and
    use it wherever necessary.
