import json
import re

char_limit = 64 # max no of char in one line

def optimize_str(str_list, chunk_size, start):
    count = 0
    if chunk_size == 1 or start + chunk_size > len(str_list):
        return str_list

    for i in range(chunk_size):
        count += len(str_list[start+i].strip(' '))

    if count <= char_limit:
        str_list[start:start+chunk_size] = [''.join(str_list[start:start+chunk_size])]
    if start + chunk_size >= len(str_list):
        return optimize_str(str_list, chunk_size - 1, 0)
    else:
        return optimize_str(str_list, chunk_size, start + 1)

with open('telegram.json','r', encoding="utf8") as json_file:
    data = json.load(json_file)
    for p in data['chats']['list']:
        with open("output.txt", "w", encoding="utf8") as output:
            for q in p['messages']:
                if q['text'] != '' and q['from'] is not None:
                    if type(q['text']) is list: # mentions included
                        for r in q['text']:
                            try:
                                txt += r
                            except:
                                try:
                                    txt += r['text']
                                except:
                                    print(q['id'])
                    else:
                        txt = q['text']
                    txt = re.sub(' +', ' ', txt)
                    txt = re.sub(r'\n\s*\n', '\n', txt) # white spaces and break
                    if not len(txt) > char_limit:
                        txt = txt.replace('\n', ' ').strip(' ').strip(',')
                        output.write(q['from'] + ': ' + txt + '\n')
                    else:
                        char_split = ['\n', ','] # try to fit chat messages into one line, see also optimize_str
                        for cs in char_split:
                            txt_split = txt.split(cs)
                            try:
                                for ts in txt_split:
                                    txt = ts.replace('\n', ' ').strip(' ').strip(',')
                                    output.write(q['from'] + ': ' + txt + '\n')
                                break
                            except RecursionError: # messages may be too long, ignore
                                continue
                            except:
                                raise
