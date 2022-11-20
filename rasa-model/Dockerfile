FROM rasa/rasa
COPY . /app
WORKDIR /app
RUN python3 -m rasa train
ENTRYPOINT ["rasa", "run"]
EXPOSE 5005
