To setup Rasa:

# Setup
cd to this folder and run `pip3 install -U --user pip && pip3 install rasa`

## Setup on Apple Silicon 
Prereq: Homebrew and Python installed

https://github.com/gerasimos/doc-rasa-on-m1
# Training
`rasa train`

Apple Silicon: `python -m rasa train` 

# Testing bot in commandline
`rasa shell`

Apple Silicon: `python -m rasa shell`
## Docs
https://rasa.com/docs/rasa/