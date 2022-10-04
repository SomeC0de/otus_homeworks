import paho.mqtt.client as mqtt
from morse_converter import indicate_msg_with_led
from led_blink import led_blink_once
from led_blink import led_pin_init
from led_blink import led_pin_deinit

msg_indic = []
isConnected = 0
is_morse_proceed = 0
is_led_proceed = 0

def on_connect(client, userdata, flag, rc):
    global isConnected
    print("Connected with result code:" + str(rc))
    if rc == 0:
        isConnected = 1
        client.publish("connect", "true", 1)


def on_disconnect(client, userdata, rc):
    global isConnected
    print("Unexpected disconnection")
    isConnected = 0


# For both topics corresponding flag is set during reception only if
# another flag is reset. It is implemented to prevent or resolve
# possible conflict when both flags are set.
def on_message(client, userdata, msg):
    global is_led_proceed
    global is_morse_proceed
    global msg_indic

    # If Raspberry Pi gets topic for LED blink it only sets
    # corresponding flag
    if msg.topic == "led/single":
        if 0 == is_led_proceed and 0 == is_morse_proceed:
            print ("Set flag to launch LED handler")
            is_led_proceed = 1
        elif 1 == is_led_proceed and 0 == is_morse_proceed:
            print("Handler LED in progress...(do nothing)")
            pass
        elif 1 == is_morse_proceed and 0 == is_led_proceed:
            print("Already busy by Morse handler...(do nothing)")
            pass
        else: #both flags are 1, handle error
            print ("Simultaneous access to LED - reset both flags")
            is_morse_proceed = 0
            is_led_proceed = 0


    # If Raspberry Pi gets topic for payload indication it converts
    # payload to UTF-8 in addition
    if msg.topic == "topic/morse":
        if 0 == is_led_proceed and 0 == is_morse_proceed:
            print ("Set flag to launch Morse handler")
            is_morse_proceed = 1
            msg_indic = format(msg.payload.decode("utf-8"))
        elif 1 == is_led_proceed and 0 == is_morse_proceed:
            print("Already busy by LED handler...(do nothing)")
            pass
        elif 1 == is_morse_proceed and 0 == is_led_proceed:
            print("Handler Morse in progress...(do nothing)")
            pass
        else: #both flags are 1, handle error
            print ("Simultaneous access to LED - reset both flags")
            is_morse_proceed = 0
            is_led_proceed = 0

try:
    led_pin_init()

    client = mqtt.Client(client_id="RPi_3")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.username_pw_set("RPi_3", "weak_password")

    client.connect("192.168.0.101", 1883, 60)
    client.loop_start()
    client.subscribe("led/single")
    client.subscribe("topic/morse")

    # Execute appropriate handler for each flag or resolve conflict
    # if both flags are set or do nothing if both flags are reset
    while True:
        if 1 == is_led_proceed and 0 == is_morse_proceed:
            print("Handle LED")
            led_blink_once()
            is_led_proceed = 0
        elif 1 == is_morse_proceed and 0 == is_led_proceed:
            print("Handle Morse")
            indicate_msg_with_led(msg_indic)
            is_morse_proceed = 0
        elif 1 == is_morse_proceed and 1 == is_led_proceed:
            print ("Simultaneous access to LED - reset both flags")
            is_morse_proceed = 0
            is_led_proceed = 0
        else:
            pass
            #print ("Waiting...")

    client.loop_stop()

except KeyboardInterrupt:
    led_pin_deinit()


finally:
    led_pin_deinit()
