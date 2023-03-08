import numpy as np
from pydub import AudioSegment  # reference at bottom
import csv
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("USAGE: python main.py input.wav")
    filepath = sys.argv[1]

    try:
        with open("tuning.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            tuning = {row['Note']: float(row['Frequency']) for row in reader} # create dictionary for all correct note values.. {"Note name": frequency}
    except FileNotFoundError:
        sys.exit("tuning.csv not found")
    samples = load_audio(filepath)
    print(samples)
    # analyzed_data = analyze_audio(samples)
    # scores = calculate_accuracy(analyzed_data)
    # print(scores)


def load_audio(filepath):
    """
    # Load audio file from disk and return as numpy array.
    """
    sound = AudioSegment.from_wav(filepath)
    samples = sound.get_array_of_samples()
    samples = np.array(samples)
    return samples


main()