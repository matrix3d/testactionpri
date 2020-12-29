import os
import json
print(111111)
env_dist = os.environ
env_dist["asclassname"]="myclassname"
#print(env_dist)
with open(env_dist.get("GITHUB_EVENT_PATH")) as json_file:
    data = json.load(json_file)
    print(data)
