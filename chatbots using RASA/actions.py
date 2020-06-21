# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("i am from action py file")

        dispatcher.utter_message(text="Hello World!from my first action python code")

        return []


class action_search_restaurant(Action):

    def name(self) -> Text:
        return "action_search_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       entities= tracker.latest_message['entities']
       print(entities)
       
       for i in entities:
           if i['entity']=='hotel':
               name = i['value']
               
           if name== 'indian':
               message ="Rajmohan , Kamalkhanna ,Taj, Oberai, Bundeli"
               
           if name== 'chinese':
               message ="chinese1 , chinese2 ,chinese3, chinese4, chinese4"
               
       dispatcher.utter_message(text=message)
       
       return []
    
    
class action_corona_state(Action):

    def name(self) -> Text:
        return "action_corona_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response =requests.get("https://api.covid19india.org/data.json").json()
        
        entities = tracker.latest_message['entities']
        print("Last message now",entities)
        state = None
        
        for e in entities:
            if e['entity']== 'state':
                state = e['value']
                
        message = 'Please enter correct state name'  
        for data in response['statewise']:
            if data['state']== state.title():
                print(data)
                message = 'Date' + data['lastupdatedtime'] + 'Active cases are  ' + data['active'] + 'Confirmed cases are  ' + data['confirmed'] + 'and Recovered cases are  ' + data['recovered']         
        print(message)
        dispatcher.utter_message(text=message)

        return []
    
    
    
    
    
    
    
