# intonation_real
scores user intonation

USAGE - python main.py input.wav




1.   load_audio_file(filepath):
        Use the pydub.AudioSegment.from_wav() function to load the audio file from disk and convert it to an AudioSegment object.
        Return the AudioSegment object.

2.   detect_pitch(audio, window_size, overlap):
        Convert the AudioSegment object to a raw audio array using the audio.get_array_of_samples() method.
        Divide the raw audio array into overlapping windows of size window_size and with an overlap of overlap.
        For each window of audio, calculate the pitch using a pitch detection algorithm such as the YIN algorithm or autocorrelation.
        Store the pitch values for each window in a list.
        Return the list of pitch values.

3.   map_pitch_to_note_frequency(pitch, note_freqs):
        Find the closest note in the note_freqs dictionary to the given pitch value by calculating the absolute difference between the pitch value and each frequency in the dictionary.
        Return the name of the closest note (i.e. the key in the note_freqs dictionary) and its frequency.

4.   process_audio_file(filepath, window_size, overlap, note_freqs):
        Load the audio file using the load_audio_file() function.
        Detect the pitch values using the detect_pitch() function.
        Map each pitch value to the closest note in the note_freqs dictionary using the map_pitch_to_note_frequency() function.
        Store the resulting note names in a list or dictionary.
        Calculate the accuracy of intonation for each note in the melody, e.g. by comparing the detected frequency to the correct frequency in the note_freqs dictionary.
        Return the results as a list or dictionary.