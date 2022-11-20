FROM rasa/rasa
COPY . /app
WORKDIR /app
USER root
RUN pip3 install -r requirements.txt
# RUN python3 -m rasa train
ENTRYPOINT ["rasa", "run", "actions"]
EXPOSE 5055
