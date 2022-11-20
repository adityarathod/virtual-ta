FROM rasa/rasa
COPY . /app
WORKDIR /app
USER root
RUN python3 -m rasa train
ENTRYPOINT ["rasa", "run"]
EXPOSE 5005
