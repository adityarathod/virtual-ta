To setup Rasa:

# Setup
cd to this folder and run `pip3 install -U --user pip && pip3 install rasa`

Also do `pip install thefuzz[speedup]`

## Setup on Apple Silicon 
Prereq: Homebrew and Python installed

https://github.com/gerasimos/doc-rasa-on-m1
# Training
`rasa train`

Apple Silicon: `python -m rasa train` 

# Testing bot in commandline
`rasa run actions` -- run this in a separate terminal window, it starts the custom actions server 

`rasa shell`

Apple Silicon: 

`python -m rasa run actions`

`python -m rasa shell`
## Docs
https://rasa.com/docs/rasa/