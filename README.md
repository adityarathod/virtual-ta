# virtual-ta
cs 4485 virtual ta project


## deployment

> **Note** Since we do use ngrok tunneling for dev, there may be a need to [modify the client code](https://github.com/adityarathod/virtual-ta/blob/main/student-client/pages/index.tsx#L20) to make requests to local API server and not the tunneled version.

a version is already deployed with ngrok tunneling + vercel frontend deploys for ease of development! located on `/home/generic/virtual-ta` on the VM.

### dockerized ([wip](https://github.com/adityarathod/virtual-ta/pull/35)) (requires docker-compose/podman-compose)
- Clone repo
- `podman-compose up -d`

### non-dockerized (complex!)
(needs [Python version supported by Rasa](https://rasa.com/docs/rasa/installation/installing-rasa-open-source/), NodeJS 19.x installed)
- Install deps for chat server by `cd`ing into `chat_server` and running `pip3 install -r requirements.txt` and `pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu`
- Install Rasa [as per instructions](https://github.com/adityarathod/virtual-ta/tree/main/rasa-model)
- Install deps for frontend by running `yarn` in `student-client` folder
- Run the following in separate terminals:
  - Run Rasa server (`cd` to rasa-model folder): `rasa run`
  - Run Rasa action server (`cd` to rasa-model/actions folder): `rasa run actions`
  - Run API server (`cd` to chat_server folder): `python3 app.py`
  - Run student client (`cd` to student-client folder): `yarn start`
  
