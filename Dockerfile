FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt app/requirements.txt

RUN pip3 install -r app/requirements.txt

COPY . /app

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_gui.py", "--server.port=8501", "--server.address=0.0.0.0"]