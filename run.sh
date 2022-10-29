#!/bin/bash

cd rasa-model
conda env update -f env.yml -n rasa-env

tmux new -s run

tmux send-keys "cd chat_server" Enter
tmux send-keys "source venv/bin/activate" Enter
tmux send-keys "python3 app.py" Enter

tmux split-window -v
tmux send-keys "cd rasa-model" Enter
tmux send-keys "conda activate rasa-env" Enter
tmux send-keys "rasa run" Enter

tmux split-window -h -p 50
tmux send-keys "cd rasa-model" Enter
tmux send-keys "conda activate rasa-env" Enter
tmux send-keys "rasa run actions" Enter

