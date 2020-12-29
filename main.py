import os
import json
print(111111)
env_dist = os.environ
#print(env_dist)
text = json.loads(open(env_dist.get("GITHUB_EVENT_PATH")))
print(text)
