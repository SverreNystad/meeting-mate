import tkinter as tk
from recorder import Recorder
from transcriber import transcribe

recorder = Recorder()

app = tk.Tk()
app.title("Meeting Mate")

# Status label for feedback
status_label = tk.Label(app, text="Press 'Start Recording' to begin")
status_label.pack(pady=10)


def start_recording():
    """Callback to start recording and update status label."""
    recorder.start_recording()
    status_label.config(text="Recording...")


def stop_recording():
    """Callback to stop recording, update status, and optionally start transcription."""
    file_name = recorder.stop_recording()
    status_label.config(text=f"Recording saved as {file_name}")

    transcription = transcribe(file_name)
    transcription_label.config(text=transcription)


# Create Start and Stop buttons
start_button = tk.Button(app, text="Start Recording", command=start_recording)
start_button.pack(pady=5)

stop_button = tk.Button(app, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=5)

transcription_label = tk.Label(app, text="Transcription will appear here")

transcription_label.pack(pady=10)

# Start the GUI event loop
app.mainloop()

# Cleanup PyAudio
recorder.close()
