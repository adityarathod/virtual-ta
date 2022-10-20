# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#
class ActionAlgoTimeComplexity(Action):

    def name(self) -> Text:
        return "action_time_complexity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        algo = tracker.get_slot('algorithm')

        # to do: set up more robust data lookup (perhaps json)
        algoToTime = {
            "bfs": "O(V + E) where V == number of verticies and E == number of edges", 
            "breadth first search": "O(V + E) where V == number of verticies and E == number of edges", 
            "dfs": "O(V + E) where V == number of verticies and E == number of edges", 
            "depth first search": "O(V + E) where V == number of verticies and E == number of edges", 
            "binary search": "O(log(n))", 
            "merge sort": "O(n * log(n))"
            }

        if algo in algoToTime: 
            dispatcher.utter_message(text="The time complexity of " + algo + " is " + algoToTime[algo])
        else: 
            dispatcher.utter_message(text="I can't find that algorithm, please try a different spelling.")

        return []
