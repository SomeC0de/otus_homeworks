#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

time_unit_sec = 1

pin_led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)
GPIO.output(pin_led, GPIO.LOW)

class MorseLetter:

    def __init__(self, letter, symbols_seq):
        self.sign = letter
        self.symb_set = list(symbols_seq)

    def indicate(self):
        for cnt in range(len(self.symb_set)):
            self.symb_set[cnt]()


def dash():
    GPIO.output(pin_led, GPIO.HIGH)
    time.sleep(3 * time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)

def dot():
    GPIO.output(pin_led, GPIO.HIGH)
    time.sleep(time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)

def dsh_dt_ps():
    GPIO.output(pin_led, GPIO.LOW)
    time.sleep(time_unit_sec)
    GPIO.output(pin_led, GPIO.LOW)

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

symb_gap = MorseLetter(" ", [dsh_dt_ps, dsh_dt_ps, dsh_dt_ps, dsh_dt_ps, dsh_dt_ps, dsh_dt_ps, dsh_dt_ps])

morse_alphabet = [letter_a, letter_b, letter_c, letter_d, letter_e, letter_f, letter_g, letter_h, letter_i, letter_j,
                  letter_k, letter_l, letter_m, letter_n, letter_o, letter_p, letter_q, letter_r, letter_s, letter_t,
                  letter_u, letter_v, letter_w, letter_x, letter_y, letter_z,
                  symb_gap,
                  figure_0, figure_1, figure_2, figure_3, figure_4, figure_5, figure_6, figure_7, figure_8, figure_9]

out_seq = [] # Contains sequence of functions for indication

message = input("Enter a message and press ENTER: ").lower()

is_inv_msg = 0

# Verify that message contains allowable symbols only and making
for idx_msg in range(len(message)):
    idx_abc = 0
    for idx_abc in range(len(morse_alphabet)):
        if morse_alphabet[idx_abc].sign == message[idx_msg]:
            out_seq.append(morse_alphabet[idx_abc])
            break

    # Every sign in alphabet is checked and no appropriate symbol has found
    if (idx_abc + 1) == len(morse_alphabet):
        print("Invalid text")
        is_inv_msg = 1
        break

    # Verify whether letters are separated by gap or not
    #else:
        #if (idx_msg + 1) != " ":
            

if is_inv_msg == 0:
    for k in range(len(out_seq)):
        out_seq[k].indicate()

GPIO.cleanup()
