import time

from Tkinter import *
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Got this from thinkgeeks
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}
# --

BASIC_TIME_UNIT = 0.4

# Setup led
led0=LED(18) # (Pin 12)


# GUI setup
win = Tk()
win.title("LED Morse Code")

# Led Commands
def test_function():
    print "Tested successfully"

def close():
    # Untoggle led
    led0.off()
    RPi.GPIO.cleanup()
    win.destroy()
# --

def blinkLed(time_to_blink):
    # Space between character
    time.sleep(BASIC_TIME_UNIT)
    # Turn on
    if led0.is_lit:
        print "Already on"
    else:
        led0.on()
    time.sleep(time_to_blink * BASIC_TIME_UNIT)
    # Turn off
    led0.off()
# --


def do_morse_code(text_string):
    text_string = text_string.upper()
    print text_string
    for letter in text_string:
        if letter == ' ':
            print "Space"
            time.sleep(7 * BASIC_TIME_UNIT)
            continue
        elif letter in MORSE_CODE_DICT:
            print letter + MORSE_CODE_DICT[letter]
            code_string = MORSE_CODE_DICT[letter]
            for bit_ in code_string:
                if bit_ == '-':
                    blinkLed(3)
                elif bit_ == '.':
                    blinkLed(1)
            # --
        time.sleep(3 * BASIC_TIME_UNIT)
        # --
    # --
    return
# --

# Morse Code Text box

textInput = Entry(win, bg='bisque2')#textvariable=v,
textInput.grid(row=0,column=1)

# Morse code function
def run_morse():
    # Untoggle led
    led0.off()
    # Toggle chosen led
    text_value = textInput.get()
    if len(text_value) > 12 or len(text_value) < 0:
        print"Text is too long - 12 char min"
        return
    # --
    
    do_morse_code(text_value)
    
# --

# Run code with text

ledButton = Button(win, text='Enter', command=run_morse, bg='bisque2', height=1, width=24)
ledButton.grid(row=1,column=1)

# Exit Button
exitButton = Button(win, text='Exit', command=close, bg='red', height=1, width=6)
exitButton.grid(row=2, column=1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()




