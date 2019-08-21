import RPi.GPIO as GPIO
import MFRC522
import signal
from time import sleep

uid = None
prev_uid = None 
continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
mfrc522 = MFRC522.MFRC522()

# Welcome message
print "Door is Locked"


# This loop keeps checking for chips.
# If one is near it will get the UID

while continue_reading:
    
    # Scan for cards    
    (status,TagType) = mfrc522.MFRC522_Request(mfrc522.PICC_REQIDL)

    # If a card is found
    if status == mfrc522.MI_OK:
        # Get the UID of the card
        (status,uid) = mfrc522.MFRC522_Anticoll()
        if uid!=prev_uid:
           prev_uid = uid
           print("Door Is Unlocked")
	   sleep(5)
	   print("Door Is Locked")
               
