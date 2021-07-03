import os
import random
import time
import adafruit_mpr121
import board
import busio
from pydub import AudioSegment
from pydub.playback import play


def play_phrase_from_category(phrase_category):
    # Choose random phrase from category
    phrase = phrase_categories[category][
        random.randint(0, len(phrase_categories[category]) - 1)
    ]    
    play(AudioSegment.from_file(phrase))


phase_path = "/share/chippy-buttons/phrases/"
phrase_categories = {
    "attention": [],
    "food": [],
    "walk": [],
    "water": [],
}
# Populate phrase categories
for phrase_category in phrase_categories:
    for phrase_file in os.listdir(phase_path + phrase_category):
        phrase_file = phase_path + phrase_category + "/" + phrase_file
        phrase_categories[phrase_category].append(phrase_file)

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
# Loop forever testing each input and printing when they're touched.
while True:
    # Loop through all 12 inputs (0-11).
    for i in range(12):
        # Call is_touched and pass it then number of the input.  If it's touched
        # it will return True, otherwise it will return False.
        if mpr121[i].value:
            print("Input {} touched!".format(i))
            if i == 0:
                category = "attention"
                play_phrase_from_category(category)
            elif i == 1:
                category = "food"
                play_phrase_from_category(category)
            elif i == 2:
                category = "walk"
                play_phrase_from_category(category)
            elif i == 3:
                category = "water"
                play_phrase_from_category(category)
    time.sleep(0.25)  # Small delay to keep from spamming output messages.

