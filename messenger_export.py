import os
import json

path = 'fb'

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

with open("output.txt", "w", encoding="utf8") as output:
    for f in files:
        with open(f,'r') as json_file:
            data = json.load(json_file)
            for msg in data['messages']:
                try:
                    output.write(msg['sender_name'].encode('latin1').decode('utf8') + ': ' + msg['content'].replace('\n', ' ').encode('latin1').decode('utf8') + '\n')
                except:
                    pass