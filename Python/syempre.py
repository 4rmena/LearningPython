import sys
from time import sleep

def type_out(text, char_delay, pause_after):
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        sleep(char_delay)
    sleep(pause_after)

def syempre():
    lines = [
        [("S'yempre,", 0.1, 1), (" ikaw lang", 0.10, 1)], 
        [("Ang aking", 0.1, 0), (" iibigin,", 0.187, 0.11), (" ang aking", 0.1, 0 ), (" hahanapin", 0.187, 0.55)],
        [("Ang aking", 0.086, 0), (" susuyuin,", 0.16, 0.11), (" ang aking", 0.086, 0 ), (" yayakapin", 0.19, 0.55)],
        [("Sa araw at", 0.1, 0.189), (" gabi,", 0.08, 0.53 ), (" ikaw lang sa", 0.07, 0.197), (" akin,", 0.168, 0.69), (" ohhhhh", 0.29, 0.35)],
        [("S'yempre,", 0.1, 0.8), (" ikaw lang", 0.10, 1)], 
        [("Ang aking", 0.1, 0), (" iisipin,", 0.187, 0.11), (" ang aking", 0.1, 0 ), (" tatawagin", 0.187, 0.35)],
        [("Ang nais kong", 0.07, 0.189), (" kapiling", 0.08, 0.1 ), (" 'pag may", 0.07, 0.09), (" paglalambing,", 0.123, 0.69), (" ohhhhh", 0.29, 0.35)],
        [("S'yempre,", 0.1, 1), (" ikaw lamang para", 0.12, 0.245),(" sa", 0.10, 0), (" akin", 0.29, 2)], 
    ]

    for line in lines:
        for text, char_delay, pause_after in line:
            type_out(text, char_delay, pause_after)
        print()

syempre()