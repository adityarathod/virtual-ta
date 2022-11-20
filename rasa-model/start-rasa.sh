#!/bin/bash

rasa run &
cd actions && rasa run action
