import requests
import json

curr_quiz_data = requests.get("https://www.jsonkeeper.com/b/LLQT").content

curr_quiz_data = json.loads(curr_quiz_data)

with open("../Data/Quiz_Endpoint_data.json", "w") as f:
    json.dump(curr_quiz_data,f)

sub_quiz_data = requests.get("https://api.jsonserve.com/rJvd7g").content

sub_quiz_data = json.loads(sub_quiz_data)

with open("../Data/Submission_Quiz_Endpoint_data.json", "w") as f:
    json.dump(sub_quiz_data,f)
    

historical_data = requests.get("https://api.jsonserve.com/XgAgFJ").content

historical_data = json.loads(historical_data)

with open("../Data/Historical_data.json", "w") as f:
    json.dump(historical_data,f)