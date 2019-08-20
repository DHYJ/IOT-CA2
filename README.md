**ST0324 Internet of Things CA2 Step-by-step Tutorial**

**SCHOOL OF COMPUTING (SOC)**

# IOT CA2 Smart Home

# Step-by-step Tutorial

ST 0324 Internet of Things (IOT)

# Table of Contents

- Section 1 Overview of Smart Home
- Section 2 Hardware required
- Section 3 Hardware Diagram
- Section 4 Create a “Thing”
- Section 5 DynamoDB Setup
- Section 7 Reading RFID/NFC tags setup
- Section 8 Program setup
- Section 9 Web interface setup
- Section 10 Expected outcome
- Section 11 References

# Section 1 Overview of Smart Home
## A. What is Smart Home about?

Smart Home enables users to remotely monitor and manage applicances such as lighting, humidity and door access. There are several features to our project. Firstly, users will be able to view the humidity of their house via a web application. Secondly, users will be able to control their lightings remotely by clicking the on and off button on the web application. Aside from that, users will also be able to view how bright is their home is. Last but not least, we also have an RFID feature that allows user to access their door with a access card instead of the traditional way of using keys. The door will be open for 5 seconds and after that the door will be locked automatically. We also made a function that allows users to view real time values of their humidity, light and temperture level. 

## B. How the final RPI set-up looks like

```
Final Set-up
```
![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/Setup.jpeg)

## C. Web Application 

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/Web%20UI.jpeg)

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/Graph.jpeg)

# Section 2 Hardware required

## A. Hardware checklist

Our application has several functions that requires specific hardware and below is the list of hardware needed and explains the details about each hardware.

**2 Light Dependant Resistor (LDR)**

An LDR is a component that has a (variable) resistance that changes with the light intensity that falls upon it. This allows them to be used to sense light values. We will use this hardware to sense the light values of the surroundings.


![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/ldr.jpg)


**2 Analog to Digital converters (MCP3008)**

The Raspberry Pi has no built in analogue inputs which means it makes it difficult to use many of the available sensors, with this converter it helps to convert analog to digital signals for the RPI.


![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/MCP3008.jpg)

**4 LED (Any colour)**

The LED lights indicates whether the lights are on or off. Insert the LED with the anode (long leg) towards the board.


![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/LED.jpg)

**2 DHT Sensors**

DHT sensors are used to measure temperature and relative humidity. These sensors contain a chip that does analog to digital conversion and spit out a digital signal with the temperature and humidity. We used to to monitor the temperature and humidity.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/DHT%20Sensor.png)

**2 RFID / NFC MFRC522 Card Reader Module**

This module can read/write to tags and cards and also "act" like a NFC tag. The RFID Reader Module can be used in a wide variety of hobbyist and commercial applications, including access control. We use the card to access to the main door by tapping on the NFC card reader.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/NFC.jpg)

**1 RPI Camera Module**

We use the RPI camera module to take pictures and it will upload to AWS cloud service (S3 bucket). The camera has a function to detect general object such as humans, bottle etc.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/RPI%20Module.jpg)

## Section 3 Hardware Diagram

In this section, The Fritzing iagram shows all the necessary components described in Section 2.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/Fritzing.png)

## Section 4 Create a “Thing”

#### Setting Up Your “Thing”

Firstly, navigate to IoT Core within the AWS website by clicking on services, then IoT Core.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing.png)

Under manage, select things and choose register a thing.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing2.png)

Choose Create a single thing.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing3.png)

Give a name for your thing, for example, SmartHome. Ignore the rest of the fields. Click next.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing4.PNG)

Select create certificate and you will be redirected to the following page. Download all
four files. As for the root CA, download the Amazon Root CA3

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing5.PNG)

## Section 5 DynamoDB Setup

#### DynamoDB

First, navigate to DynamoDB within the AWS website by clicking on services, then
DynamoDB. Click create table.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing6.PNG)

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing7.PNG)

Once done, rename the four files accordingly.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing8.PNG)

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing9.PNG)

Move the four files into a directory in the raspberry pi (RPI).

Click activate.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing10.PNG)

Click register thing. Policy will be created later.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing11.png)

Go to policies under the secure section. Select create a policy.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing12.png)

Give a name for your policy, for example, SmartHomePolicy and enter the following under
Add statements

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/Setupofthing13.PNG)

Go to certificates under secure section. Select the certificate you created previously,
and click attach policy. Attach the policy you created previously.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/SetupofThing14.PNG)

#### Create AWS Role

Run the following command on your Raspberry Pi to install the AWS Command-line client on your Raspberry Pi

```
sudo pip install awscli --upgrade --user
```
Edit the .profile to include the path of the AWS client

```
sudo nano ~/.profile
```

Add in the following code after the last line and save the file

```
export PATH=~/.local/bin:$PATH
```

Type the following command at the command-line prompt to make the new settings take effect immediately

```
source ~/.profile
```
Type the following command to install the AWS Command-Line Interface Client on your Raspberry Pi

```
sudo pip install awscli
```
Copy down your AWS educate’s Access Key ID and Secret Access Key ID.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/AWS.PNG)
