
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

import json 
#
class ActionAlgoTimeComplexity(Action):

    def name(self) -> Text:
        return "action_time_complexity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        algo = tracker.get_slot('algorithm')

        f = open('./time_complexity/data.json')
        algoToTime = json.load(f)

        if algo in algoToTime: 
            dispatcher.utter_message(text="The time complexity of " + algo + " is " + algoToTime[algo])
        else: 
            dispatcher.utter_message(text="I can't find that algorithm, please try a different spelling.")
        AllSlotsReset()
        return []