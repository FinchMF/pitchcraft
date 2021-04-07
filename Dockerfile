FROM ubuntu

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.7 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

LABEL org.opencontainers.image.title="PitchCraft Synthesis" \
      org.opencontainers.image.description="Pitch System Generator" \
      org.opencontainers.image.authors="@matthewfinch"

RUN mkdir -p pitchcraft

COPY . pitchcraft

WORKDIR /pitchcraft

RUN pip3 install -r requirements.txt 

ENTRYPOINT ["gunicorn", "app:server"] 