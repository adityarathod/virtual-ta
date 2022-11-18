
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

from thefuzz import process

import json 
#
class ActionDefinitions(Action):

    CONFIDENCE_THRESHOLD = 85
    SIMILAR_THRESHOLD = 40

    def name(self) -> Text:
        return "action_definitions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        topic = tracker.get_slot('topic')
        print(topic)
        f = open('./definitions/data.json')
        topicToDefine = json.load(f)
        if topic in topicToDefine: 
            dispatcher.utter_message(text="The definition of " + topic + " is " + topicToDefine[topic])
        elif not topic: 
            dispatcher.utter_message(text="I don't understand, please try a different spelling or wording")
        else: 
            fuzzy_match = process.extract(topic, topicToDefine.keys(), limit=3)
            print(fuzzy_match) # debug
            if isinstance(fuzzy_match[0][1], int):
                if fuzzy_match[0][1] > self.CONFIDENCE_THRESHOLD:
                    dispatcher.utter_message(text="The definition of " + fuzzy_match[0][0] + " is " + topicToDefine[fuzzy_match[0][0]])
                else:
                    close_matches = [fuzzy_match[i][0] for i in range(len(fuzzy_match)) if fuzzy_match[i][1] > self.SIMILAR_THRESHOLD]
                    dispatcher.utter_message(text="I believe " + topic + " may be misspelled, did you perhaps mean one of these? " + ', '.join(close_matches) + "?")
            else: 
                dispatcher.utter_message(text="I can't find a definition for " + topic + ", please try a different spelling or wording.")
        AllSlotsReset()
        return []