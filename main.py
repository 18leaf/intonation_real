import numpy as np
from pydub import AudioSegment  # reference at bottom
import csv
import sys

def main():
    filepath = input("Please enter the path to your audio file: ")
    try:
        with open("tuning.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            tuning = {row['Note']: float(row['Frequency']) for row in reader} # create dictionary for all correct note values.. {"Note name": frequency}
    except FileNotFoundError:
        sys.exit("tuning.csv not found")
    samples = load_audio(filepath)
    print(samples)
    analyzed_data = analyze_audio(samples)
    scores = calculate_accuracy(analyzed_data)
    print(scores)


def load_audio(filepath):
    """
    # Load audio file from disk and return as numpy array.
    """
    sound = AudioSegment.from_wav(filepath)
    samples = sound.get_array_of_samples()
    samples = np.array(samples)
    return samples


def get_closest_pitch(freq):
    """
    # Given a frequency, returns the closest note in the key by frequency.
    """
    # Implement your code to find the closest note here
    # You may want to store the frequencies of the notes in the key as a dictionary


def analyze_audio(samples):
    """
    # Given a numpy array of audio samples, analyzes the pitch of each note and returns a list of dicts with the analyzed data for each note.
    """
    analyzed_data = []
    # Implement your code to analyze the pitch of each note here
    # You may want to use the get_closest_pitch function here

    return analyzed_data


def calculate_accuracy(analyzed_data):
    """
    # Given a list of analyzed data for each note, calculates the accuracy of intonation for each note and returns a dict with the scores for each note.
    """
    scores = {}
    # Implement your code to calculate the accuracy of intonation for each note here

    return scores

if __name__ == "__main__":
    main()


"""
pydub:

    AudioSegment.from_wav(filepath): Load a WAV audio file from disk and return as an AudioSegment object.
    sound.get_array_of_samples(): Return the raw audio samples from an AudioSegment object as an array of integers.
    AudioSegment.apply_gain(): Apply a gain (amplification) to an AudioSegment object.
    AudioSegment.export(): Export an AudioSegment object to a WAV file on disk.


numpy:

    numpy.array(): Create a numpy array from a list or array-like object.
    numpy.argmax(): Find the index of the maximum value in a numpy array.
    numpy.argmin(): Find the index of the minimum value in a numpy array.
    numpy.abs(): Calculate the absolute value of a numpy array.
    numpy.sum(): Calculate the sum of the values in a numpy array.
    numpy.mean(): Calculate the mean (average) value of a numpy array.
    numpy.std(): Calculate the standard deviation of a numpy array.
"""
