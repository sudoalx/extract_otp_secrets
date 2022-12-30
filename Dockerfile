FROM python:3.11-slim-bullseye

# For debugging
# docker run --entrypoint /extract/run_pytest.sh --rm -v "$(pwd)":/files:ro extract_otp_secret_keys
# docker run --entrypoint /bin/bash -it --rm -v "$(pwd)":/files:ro --device="/dev/video0:/dev/video0" --env="DISPLAY" -v /tmp/.X11-unix:/tmp/.X11-unix:ro extract_otp_secret_keys

WORKDIR /extract

COPY . .

ARG RUN_TESTS=true

RUN apt-get update && apt-get install -y libzbar0 libsm6 python3-opencv nano \
    && pip install --no-cache-dir -r requirements.txt \
    && if [ "$RUN_TESTS" = "true" ]; then /extract/run_pytest.sh; else echo "Not running tests..."; fi

WORKDIR /files

ENTRYPOINT ["python", "/extract/src/extract_otp_secret_keys.py"]

LABEL org.opencontainers.image.source https://github.com/scito/extract_otp_secret_keys
