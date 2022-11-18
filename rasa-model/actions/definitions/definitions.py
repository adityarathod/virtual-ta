
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

from thefuzz import process

import json 
#
class ActionDefinitions(Action):

    def name(self) -> Text:
        return "action_definitions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        topic = tracker.get_slot('topic')
        print(topic)
        f = open('./definitions/data.json')
        topicToDefine = json.load(f)
        # fuzzy search through keys
        cleanedKey, _ = process.extractOne(topic, topicToDefine.keys())

        if cleanedKey != topic and cleanedKey in topicToDefine:
            dispatcher.utter_message(text=f"I think you meant {cleanedKey}. The definition of {cleanedKey} is {topicToDefine[cleanedKey]}.")
        elif cleanedKey in topicToDefine: 
            dispatcher.utter_message(text="The definition of " + topic + " is " + topicToDefine[cleanedKey])
        elif not topic: 
            dispatcher.utter_message(text="I don't understand, please try a different spelling or wording :)")
        else: 
            dispatcher.utter_message(text="I can't find a definition for " + topic + ", please try a different spelling or wording :)")
        AllSlotsReset()
        return []