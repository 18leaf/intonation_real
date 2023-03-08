import numpy as np
from pydub import AudioSegment  # reference at bottom
import csv
import sys

try:
        with open("tuning.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            tuning = {row['Note']: float(row['Frequency']) for row in reader} # create dictionary for all correct note values.. {"Note name": frequency}
except FileNotFoundError:
        sys.exit("ERROR: tuning.csv not found")


def main():
    if len(sys.argv) != 2:
        sys.exit("USAGE: python main.py input.wav")

    filepath = sys.argv[1]

    samples = load_audio(filepath)
    analyzed_data = analyze_audio(samples)
    # scores = calculate_accuracy(analyzed_data)
    # print(scores)


def load_audio(filepath):
    """
    # Load audio file from disk and return as numpy array.
    """

    try:
        sound = AudioSegment.from_wav(filepath)
        samples = np.array(sound.get_array_of_samples())
    except FileNotFoundError:
        sys.exit(f"ERROR: input.wav not found")

    return samples

def get_closest_pitch(freq):
    """
    # Given a frequency, returns the closest note in the key by frequency.
    """

    closest_note = ""
    min_distance = float("inf")
    for Note, Frequency in tuning.items()
    # Implement your code to find the closest note here
    # You may want to store the frequencies of the notes in the key as a dictionary


def analyze_audio(samples):
    """
    # Given a numpy array of audio samples, analyzes the pitch of each note and returns a
    list of dicts with the analyzed data for each note.
    """
    analyzed_data = []
    # Implement your code to analyze the pitch of each note here
    # You may want to use the get_closest_pitch function here

    return analyzed_data


main()