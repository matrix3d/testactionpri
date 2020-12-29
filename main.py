import os
import json
env_dist = os.environ
with open(env_dist.get("GITHUB_EVENT_PATH")) as json_file:
    data = json.load(json_file)
    code=data.comment.body
    x = re.findall("public\s+class\s+(\S+)[\s{]" , code)
    className=x[0]
    f = open(data.comment.id+"/"+className+".as", "w")
    f.write(code)
    f.close()
    
    f = open(data.comment.id+"/main.txt", "w")
    f.write(className)
    f.close()
