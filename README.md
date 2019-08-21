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
- Section 6 Reading RFID/NFC tags setup
- Section 7 Program setup
- Section 8 Expected outcome


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

**8 Resistors (4 x 330 Ω Resistors, 4 x 10K Ω Resistor)**

Resistors help with the current flow and to prevent the Raspberry Pi from being damaged.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/330.jpg)

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/10k%20Resistor.jpg)

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

## Section 5 DynamoDB Setup

#### DynamoDB

First, Go to DynamoDB within the AWS website by clicking on services, then
DynamoDB. Click create table.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/DynamoDB1.png)

Enter the table name and the primary key, then click create.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/DynamoDB2.PNG)

Next, go back to IoT Core within the AWS website by clicking on services, then IoT
Core. Click Act, then create button at the top right corner.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/DynamoDB3.PNG)

Create the rule with the name “iotdata”.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/DynamoDB4.PNG)

Under Set one or more actions section, choose add action, select “split message into multiple
columns of a database table”. Select configure action. Under table name, select the
“iotdata” table. Under IAM role name, select the role you created previously, “iotlab11role”. For mine i'm using back an old role. Click add action, then create rule.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/DynamoDB5.PNG)

Now that we had created the rules, we can add items to the data
table. Navigate to the test section of IoT Core in AWS.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/DynamoDB6.PNG)

Scroll down to Publish. Enter the topic “sensors/light”. Enter the following in the text
field below:

```
{
“deviceid”: "HomeMonitor",
“Light”: “”
}
```
The data is in the iot table.

![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/DynamoDB.jpeg)

## Section 6 Reading RFID/NFC tags setup

#### Enable SPI and prepare the MFRC522 libraries

If your raspberry pi is new, you will need to configure it with the MFRC522 libraries, you can follow the following
instructions to set it up.

##### << Enable SPI via raspi-config >>

Run raspi-config, choose menu item “5 Interfacing Options” and enable SPI.

```
sudo rasp-config
```
![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/Facial.png)
![Alt text](https://github.com/DHYJ/IOT-CA2/blob/master/Images/Facial2.png)

##### << Enable device tree in boot.txt>>

Modify the /boot/config.txt to enable SPI

```
sudo nano /boot/config.txt
```

Ensure these lines are included in config.txt

```
device_tree_param=spi=on
dtoverlay=spi-bcm2835
```

**<< Install Python-dev>>**

Install the Python development libraries

```
sudo apt-get install python-dev
```

**<< Install SPI-Py Library >>**

Set up the SPI Python libraries 
```
git clone https://github.com/lthiery/SPI-Py.git
cd /home/pi/SPI-Py
sudo python setup.py install
```

**<< Install RFID library >>**

Clone the MFRC522-python library and copy out the required files to your project directory
```
git clone https://github.com/rasplay/MFRC522-python.git
cd MFRC52 2 - python
```
Edit the MFRC522.py file that you just cloned from GitHub.
```
sudo nano ~/iotca2/MFRC522.py
```
## Section 7 Program setup

To ensure that the guide is not to wordy, we won't be explain all the codes that we did for the project. Instead we will zip all the files needed for this project. 

### Installing Necessary Libraries

Install Mosquitto using the command below.

```
sudo apt-get install mosquitto mosquitto-clients
```
To run Node Red using the command below.

```
Node-red start
```
Install the AWS Python library

```
sudo pip install --upgrade --force-reinstall pip==9.0.3
sudo pip install AWSIoTPythonSDK --upgrade --disable-pip-version-check
sudo pip install --upgrade pip
```

## Section 8 Expected results

To view our project video please visit this link https://youtu.be/43--SwQEI5I

**LED Light** Lights can be turn on and off by using the web interface. Note that toilet light will only be turned on when the envirionment is dark.

**Humidity** DHT sensor will sense the humidity and temperture level will be reflected on the web and data will be stored in DynamoDB 

**Camera** Camera will be able to take pictures and detect if its an object or human and results will be displayed as well.

**RFID** User can scan the card to unlock the door

**Website** Website allows user to view real time values and turning off and on their lights. Apart from that, they will also be able to control the camera function and view the door status.

```
-- End of CA2 Step-by-step tutorial --
```
