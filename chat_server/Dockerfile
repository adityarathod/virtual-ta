FROM python:3.9.15-bullseye
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
CMD python3 app.py
EXPOSE 5000
