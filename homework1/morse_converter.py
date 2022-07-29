#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

time_unit_sec = 1

# Number of pin means it placement on GPIO header, not a number Broadcom GPIO pin
# (i.e. not GPIO11). It used with GPIO.setmode(GPIO.BOARD) option, not GPIO.setmode(GPIO.BCM)
pin_led = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_led, GPIO.OUT)
GPIO.output(pin_led, GPIO.LOW)

# Class describes single letter printing presentation and it equivalent in Morse alphabet
# as sequence of 'dot', 'dash' and 'dsh_dt_ps' functions. These functions are described below.
class MorseLetter:

    def __init__(self, letter, symbols_seq):
        self.sign = letter
        self.symb_set = list(symbols_seq)

    def indicate(self):
        for cnt in range(len(self.symb_set)):
            self.symb_set[cnt]()

    def get_sign(self):
        return self.sign

# Method implements indication of 'dash' symbol. GPIO pin sets high on 3 seconds
def dash():
    GPIO.output(pin_led, GPIO.HIGH)
    time.sleep(3 * time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)

# Method implements indication of 'dash' symbol. GPIO pin sets high on 1 second
def dot():
    GPIO.output(pin_led, GPIO.HIGH)
    time.sleep(time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)

# Method implements indication of 'gap' between letters and between 'dash' and 'dot' symbols. GPIO pin sets low on 1 second
def dsh_dt_ps():
    GPIO.output(pin_led, GPIO.LOW)
    time.sleep(time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)

# Generate alphabetbased on 'MorseLetter' class
letter_a = MorseLetter("a", [dot, dsh_dt_ps, dash])
letter_b = MorseLetter("b", [dash, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dot])
letter_c = MorseLetter("c", [dash, dsh_dt_ps, dot, dsh_dt_ps, dash, dsh_dt_ps, dot])
letter_d = MorseLetter("d", [dash, dsh_dt_ps, dot, dsh_dt_ps, dot])
letter_e = MorseLetter("e", [dot])
letter_f = MorseLetter("f", [dot, dsh_dt_ps, dot, dsh_dt_ps, dash, dsh_dt_ps, dot])
letter_g = MorseLetter("g", [dash, dsh_dt_ps, dash, dsh_dt_ps, dot])
letter_h = MorseLetter("h", [dot, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dot])
letter_i = MorseLetter("i", [dot, dsh_dt_ps, dot])
letter_j = MorseLetter("j", [dot, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dash])
letter_k = MorseLetter("k", [dash, dsh_dt_ps, dot, dsh_dt_ps, dash])
letter_l = MorseLetter("l", [dot, dsh_dt_ps, dash, dsh_dt_ps, dot, dsh_dt_ps, dot])
letter_m = MorseLetter("m", [dash, dsh_dt_ps, dash])
letter_n = MorseLetter("n", [dash, dsh_dt_ps, dot])
letter_o = MorseLetter("o", [dash, dsh_dt_ps, dash, dsh_dt_ps, dash])
letter_p = MorseLetter("p", [dot, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dot])
letter_q = MorseLetter("q", [dash, dsh_dt_ps, dash, dsh_dt_ps, dot, dsh_dt_ps, dash])
letter_r = MorseLetter("r", [dot, dsh_dt_ps, dash, dsh_dt_ps, dot])
letter_s = MorseLetter("s", [dot, dsh_dt_ps, dot, dsh_dt_ps, dot])
letter_t = MorseLetter("t", [dash])
letter_u = MorseLetter("u", [dot, dsh_dt_ps, dot, dsh_dt_ps, dash])
letter_v = MorseLetter("v", [dot, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dash])
letter_w = MorseLetter("w", [dot, dsh_dt_ps, dash, dsh_dt_ps, dash])
letter_x = MorseLetter("x", [dash, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dash])
letter_y = MorseLetter("y", [dash, dsh_dt_ps, dot, dsh_dt_ps, dash, dsh_dt_ps, dash])
letter_z = MorseLetter("z", [dash, dsh_dt_ps, dash, dsh_dt_ps, dot, dsh_dt_ps, dot])

figure_0 = MorseLetter("0", [dash, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dash])
figure_1 = MorseLetter("1", [dot, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dash])
figure_2 = MorseLetter("2", [dot, dsh_dt_ps, dot, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dash])
figure_3 = MorseLetter("3", [dot, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dash, dsh_dt_ps, dash])
figure_4 = MorseLetter("4", [dot, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dash])
figure_5 = MorseLetter("5", [dot, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dot])
figure_6 = MorseLetter("6", [dash, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dot])
figure_7 = MorseLetter("7", [dash, dsh_dt_ps, dash, dsh_dt_ps, dot, dsh_dt_ps, dot, dsh_dt_ps, dot])
figure_8 = MorseLetter("8", [dash, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dot, dsh_dt_ps, dot])
figure_9 = MorseLetter("9", [dash, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dash, dsh_dt_ps, dot])

symb_word_gap = MorseLetter(" ", [dsh_dt_ps, dsh_dt_ps, dsh_dt_ps, dsh_dt_ps, dsh_dt_ps, dsh_dt_ps, dsh_dt_ps])
symb_lttr_gap = MorseLetter("", [dsh_dt_ps])

morse_alphabet = [letter_a, letter_b, letter_c, letter_d, letter_e, letter_f, letter_g, letter_h, letter_i, letter_j,
                  letter_k, letter_l, letter_m, letter_n, letter_o, letter_p, letter_q, letter_r, letter_s, letter_t,
                  letter_u, letter_v, letter_w, letter_x, letter_y, letter_z,
                  figure_0, figure_1, figure_2, figure_3, figure_4, figure_5, figure_6, figure_7, figure_8, figure_9,
                  symb_word_gap]

# Contains input message which converted to indication functions settings
out_seq = []

# Transform message letters to lower case to avoid "Invalid text" error. All letters in alphabet are by default in lower case, so upper case
# can be recognized as unknown symbol
message = input("Enter a message and press ENTER: ").lower()

# Flag to indicate that unknown symbol is found
is_inv_symb = 0

# Verify that message contains allowable symbols only and simultaneously add indication functions for known symbols to 'out_seq' list
for idx_msg in range(len(message)):
    idx_abc = 0
    is_inv_symb = 1
    for idx_abc in range(len(morse_alphabet)):
        if morse_alphabet[idx_abc].sign == message[idx_msg]:
            out_seq.append(morse_alphabet[idx_abc])
            is_inv_symb = 0
            break

    # Every sign in alphabet is checked and only known symbols have found
    if is_inv_symb == 0:
        # Verify that current and next symbols are in range of 'message' list 
        if idx_msg + 1 < len(message):
            # Current and next symbols are letters - insert gap pause between letters
            if (message[idx_msg] != " " and (message[idx_msg + 1]) != " "):
                out_seq.append(symb_lttr_gap)

# Indication block
if is_inv_symb == 0:
    if len(message) != 0:
        for k in range(len(out_seq)):
            out_seq[k].indicate()
else:
    print("Invalid text")

GPIO.cleanup()
