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
        sys.exit("ERROR: tuning.csv not found")

    samples = load_audio(filepath)
    # analyzed_data = analyze_audio(samples)
    # scores = calculate_accuracy(analyzed_data)
    # print(scores)


def load_audio(filepath):
    """
    # Load audio file from disk and return as numpy array.
    """

    try:
        sound = AudioSegment.from_wav(filepath)
        samples = sound.get_array_of_samples()
        samples = np.array(samples)
    except FileNotFoundError:
        sys.exit(f"ERROR: input.wav not found")

    A4_samples = samples[int(sound.duration_seconds / 2) * sound.frame_rate : int(sound.duration_seconds / 2) * sound.frame_rate + sound.frame_rate]
    A4_rms = np.sqrt(np.mean(np.square(A4_samples)))
    A4_pitch = tuning['A4'] * 2 ** ((20 * np.log10(A4_rms / (2 ** 15))) / 60)

    # Compare the two arrays and print the pitch of A4 in the chromatic scale
    if np.allclose(A4_samples, sound[int(sound.duration_seconds / 2) * sound.frame_rate : int(sound.duration_seconds / 2) * sound.frame_rate + sound.frame_rate].get_array_of_samples()):
        print(f"The pitch of A4 in the chromatic scale is {A4_pitch:.2f} Hz")
    else:
        print("The chromatic scale does not contain the note A4")


    return samples


main()