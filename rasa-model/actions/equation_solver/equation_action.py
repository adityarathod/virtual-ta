# work in progress
# i think you have to do `pip install antlr4-tools` outside the venv (but maybe try without it)
# import process_latex
import sympy.integrals.integrals
from equation_solver.process_latex import *
from sympy.solvers import solve


# v = process_latex.process_sympy("\sum_{i = 1}^{10} i")
# print(v)
# print(type(v))
# print(v.doit())
# print()
#
# v = process_latex.process_sympy("x * 5 + 1 = 6")
# print(v)
# print(type(v))
# print(solve(v))
# print()
#
# v = process_latex.process_sympy("5 ^ 7")
# print(v)
# print(type(v))
# print(v.doit())
# print()
#
# v = process_latex.process_sympy("\int_{0}^{5} x")
# print(v)
# print(type(v))
# print(v.doit())
# print()
#
# # can't process this
# # v = process_latex.process_sympy("\lim_{n \to \infty}{1/x}")
# # print(v)
# # print(type(v))
# # print(v.doit())
#


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

import json
#
class ActionSolveEquation(Action):

    def name(self) -> Text:
        return "solve_equation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            equation = tracker.get_slot('equation')
            equation = equation[1:-1]

            sympy_eq = process_sympy(equation)

            if type(sympy_eq) == sympy.core.relational.Eq:
                result = solve(sympy_eq)
            else:
                result = sympy_eq.doit()

            if type(result) == list:
                if result:
                    result = result[0]
                else:
                    raise Exception("No Equation Solution")
            dispatcher.utter_message(text="The result is " + str(result))
        except:
            dispatcher.utter_message(text="The equation failed, please check your input")
        AllSlotsReset()
        return []