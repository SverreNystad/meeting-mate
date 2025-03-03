import wave
import sys
import pyaudio
import threading
from time import time

# Audio settings
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == "darwin" else 2
RATE = 44100


DATA_FOLDER = "data/"


class Recorder:
    def __init__(self):
        self.frames = []
        self.recording = False
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.record_thread = None

    def start_recording(self):
        """Start the audio stream and record in a separate thread."""
        self.frames = []
        self.recording = True
        self.stream = self.p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK_SIZE,
        )
        self.record_thread = threading.Thread(target=self.record)
        self.record_thread.start()
        print("Recording started...")

    def record(self):
        """Continuously read audio chunks until stopped."""
        while self.recording:
            data = self.stream.read(CHUNK_SIZE)
            self.frames.append(data)

    def stop_recording(self):
        """Stop recording, close the stream, and save the audio to a file."""
        if self.recording:
            self.recording = False
            self.record_thread.join()
            self.stream.stop_stream()
            self.stream.close()
            file_name = self.save_file()
            print("Recording stopped and saved as", file_name)
            return file_name
        return None

    def save_file(self):
        """Save the recorded frames to a WAV file."""
        start_time = time()
        file_name = DATA_FOLDER + f"recording_at_{int(start_time)}.wav"
        wf = wave.open(file_name, "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(self.frames))
        wf.close()
        return file_name

    def close(self):
        self.p.terminate()
