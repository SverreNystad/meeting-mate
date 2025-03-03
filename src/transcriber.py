from transformers import pipeline
from enum import Enum


class Model(Enum):
    base = "nb-whisper-tiny"
    tiny = "nb-whisper-base"
    small = "nb-whisper-small"
    medium = "nb-whisper-medium"
    large = "nb-whisper-large"


def transcribe(
    file_path: str,
    generate_kwargs={
        "task": "transcribe",
        "language": "no",
    },
    model_name: Model = Model.small,
):
    asr = pipeline("automatic-speech-recognition", "NbAiLabBeta/" + model_name.value)
    return asr(file_path, return_timestamps=True, generate_kwargs=generate_kwargs)
