
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import json 
#
class ActionDefinitions(Action):

    def name(self) -> Text:
        return "action_definitions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        topic = tracker.get_slot('topic')

        topicToDefine = json.loads('data.json')

        if topic in topicToDefine: 
            dispatcher.utter_message(text="The definition of " + topic + " is " + topicToDefine[topic])
        else: 
            dispatcher.utter_message(text="I can't find a definition for " + topic + ", please try a different spelling or wording.")

        return []