import requests
import json

root_url = 'https://api.github.com'
req = requests.get(root_url + '/users/demkonst/repos')
reps = json.loads(req.text)

rep_names = [rep['name'] for rep in reps]

print(rep_names)
