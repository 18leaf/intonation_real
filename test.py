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
    note_scores, overall_score = calculate_accuracy(analyzed_data)
    print("Per-note accuracy scores:")
    print(note_scores)
    print("Overall accuracy score:")
    print(overall_score)


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
    min_distance = float("inf") # set min distance to infinity, so all distance are less
    for Note, Frequency in tuning.items(): # itereate of each item in the tuning dict created from csv
         distance = abs(freq - Frequency) # distance is given pitch(found later in analyze audio) from csv tunign
         if distance < min_distance: # pseudo sort to find closest note to actual pitch
              min_distance = distance
              closest_note = Note
    return closest_note


def analyze_audio(samples):
    """
    # Given a numpy array of audio samples, analyzes the pitch of each note and returns a
    list of dicts with the analyzed data for each note.
    """
    """sample_rate = AudioSegment.from_wav(sys.argv[1]).frame_rate    # following uses autocorrelation for audio
    print(sample_rate)
    window_size = 2048
    hop_size = 512
    analyzed_data = []
    for i in range(0, len(samples) - window_size, hop_size):
        window = samples[i:i+window_size] * np.hamming(window_size)
        autocorr = np.correlate(window, window, mode='full')
        autocorr = autocorr[len(autocorr)//2:]
        freqs = np.arange(0, sample_rate/2, sample_rate/len(autocorr))
        pitch = freqs[np.argmax(autocorr)]
        note = get_closest_pitch(pitch)
        start_time = i / sample_rate
        duration = window_size / sample_rate
        analyzed_data.append({
            "note": note,
            "start_time": start_time,
            "duration": duration,
            "pitch": pitch
        })"""


    sample_rate = AudioSegment.from_wav(sys.argv[1]).frame_rate
    window_size = 2048
    hop_size = 256
    analyzed_data = []

    for i in range(0, len(samples) - window_size, hop_size):
        window = samples[i:i+window_size] * np.hamming(window_size)
        # Apply FFT to the window
        spectrum = np.abs(np.fft.fft(window))
        # Get the frequency values of the spectrum
        freqs = np.fft.fftfreq(window_size, d=1/sample_rate)[:window_size//2]
        # Find the index of the peak frequency
        peak_index = np.argmax(spectrum[:window_size//2])
        # Convert the index to a pitch value in Hz
        pitch = freqs[peak_index]
        # Find the closest pitch name to the calculated pitch value
        note = get_closest_pitch(pitch)
        start_time = i / sample_rate
        duration = window_size / sample_rate
        analyzed_data.append({
            "note": note,
            "start_time": start_time,
            "duration": duration,
            "pitch": pitch
        })


    # print(analyzed_data)
    return analyzed_data


def calculate_accuracy(analyzed_data):
    """
    # Given a list of analyzed data for each note, calculates the accuracy of intonation for each note and returns a dict with the scores for each note.
    """
    scores = {}
    total_accuracy = 0.0
    num_notes = 0
    for note, freq in tuning.items():
        # Filter the analyzed data to only include the current note
        notes_data = [d for d in analyzed_data if d["note"] == note]
        if len(notes_data) == 0:
            continue
        # Compute the mean pitch deviation from the correct frequency
        deviations = [abs(d["pitch"] - freq) for d in notes_data]
        mean_deviation = np.mean(deviations)
        # Compute the accuracy score as a percentage
        accuracy = max(0, 1 - mean_deviation / (freq * 0.01))
        scores[note] = accuracy
        total_accuracy += accuracy
        num_notes += 1
    overall_accuracy = total_accuracy / num_notes

    return scores, overall_accuracy


if __name__ == "__main__":
    main()