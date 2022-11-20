FROM rasa/rasa
COPY . /app
WORKDIR /app
USER root
RUN pip3 install -r requirements.txt
ENTRYPOINT ["rasa", "run", "actions"]
EXPOSE 5055
