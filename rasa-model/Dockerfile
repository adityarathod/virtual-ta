FROM rasa/rasa
COPY . /app
WORKDIR /app
# RUN pip3 install -r requirements.txt
RUN python3 -m rasa train
CMD start-rasa.sh
