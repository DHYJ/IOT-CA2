# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from gpiozero import MCP3008
from gpiozero import LED
import Adafruit_DHT
import decimal
import sys

adc = MCP3008(channel=0)
sensor_name = Adafruit_DHT.DHT11
sensor_pin = 4


# Custom MQTT message callback
def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")
	
host = "a254690l1ektgk-ats.iot.us-east-1.amazonaws.com"
rootCAPath = "rootca.pem"
certificatePath = "certificate.pem.crt"
privateKeyPath = "private.pem.key"

my_rpi = AWSIoTMQTTClient("PubSub-p1749126")
my_rpi.configureEndpoint(host, 8883)
my_rpi.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

my_rpi.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
my_rpi.configureDrainingFrequency(2)  # Draining: 2 Hz
my_rpi.configureConnectDisconnectTimeout(10)  # 10 sec
my_rpi.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
my_rpi.connect()
my_rpi.subscribe("sensors/home", 1, customCallback)
sleep(2)

# Publish to the same topic in a loop forever
loopCount = 0
while True:
	light = round(1024-(adc.value*1024))
	humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin)
	payload = '{ "temperature": ' + str(temperature) + ',"humidity": '+ str(humidity) + ',"light": ' + str(light) + ' }'
	my_rpi.publish("sensors/home", payload, 1)
	sleep(5)
