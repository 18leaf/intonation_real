import numpy as np
from pydub import AudioSegment

def load_audio_file(filepath):
    """
    Load audio file from disk and return as numpy array.
    """
    sound = AudioSegment.from_wav(filepath)
    samples = sound.get_array_of_samples()
    samples = np.array(samples)
    return samples

def get_closest_pitch(freq):
    """
    Given a frequency, returns the closest note in the key by frequency.
    """
    # Implement your code to find the closest note here
    # You may want to store the frequencies of the notes in the key as a dictionary

def analyze_audio_file(samples):
    """
    Given a numpy array of audio samples, analyzes the pitch of each note and returns
    a list of dicts with the analyzed data for each note.
    """
    analyzed_data = []
    # Implement your code to analyze the pitch of each note here
    # You may want to use the get_closest_pitch function here

    return analyzed_data

def calculate_accuracy(analyzed_data):
    """
    Given a list of analyzed data for each note, calculates the accuracy of intonation for each note
    and returns a dict with the scores for each note.
    """
    scores = {}
    # Implement your code to calculate the accuracy of intonation for each note here

    return scores

def main():
    filepath = input("Please enter the path to your audio file: ")
    samples = load_audio_file(filepath)
    analyzed_data = analyze_audio_file(samples)
    scores = calculate_accuracy(analyzed_data)
    print(scores)

if __name__ == "__main__":
    main()