import os
import random
import time
import adafruit_mpr121
import board
import busio
from pydub import AudioSegment
from pydub.playback import play

phase_path = "/share/chippy-buttons/phrases/"
phrase_categories = [
    "attention",
    "food",
    "walk",
    "water",
]
phrase_files = {}

# Startup sound
play(AudioSegment.from_file("/share/chippy-buttons/startup.m4a"))


def play_phrase_from_category(phrase_category):
    # Choose random phrase from category
    phrase_file = phrase_files[category][
        random.randint(0, len(phrase_files[category]) - 1)
    ]
    print("Playing phrase file: " + phrase_file)
    play(AudioSegment.from_file(phrase_file))


def populate_phrase_files():
    # Populate phrase_files with phrases
    print("Populating phrase files...")
    for phrase_category in phrase_categories:
        phrase_files[phrase_category] = []
        for phrase_file in os.listdir(phase_path + phrase_category):
            phrase_file = phase_path + phrase_category + "/" + phrase_file
            phrase_files[phrase_category].append(phrase_file)

populate_phrase_files()
phrase_population_counter = 0

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
# Loop forever testing each input and printing when they're touched.
while True:
    # Loop through all 12 inputs (0-11).
    for i in range(12):
        # Call is_touched and pass it then number of the input.  If it's touched
        # it will return True, otherwise it will return False.
        if mpr121[i].value:
            category = "unassigned"
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
            print("Detected input {} \"{}\"".format(i, category))

    # Small delay to keep from spamming output messages.
    seconds_increment = 0.1

    # Check for new phrases every 60 seconds
    phrase_population_counter += seconds_increment
    if phrase_population_counter >= 60:
        phrase_population_counter = 0
        populate_phrase_files()

    time.sleep(seconds_increment)

