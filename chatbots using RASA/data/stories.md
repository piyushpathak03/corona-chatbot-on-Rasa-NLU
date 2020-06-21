## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## hello_world path
* hello_world
  - action_hello_world

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## search_restaurant path
* search_restaurant
  - action_search_restaurant
  
## corona_state path
* corona_state
  - action_corona_state
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
