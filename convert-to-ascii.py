import sys
file = sys.argv[1] # pass a file through cmd

import emoji
import pinyin
import re

def simplify(file):
    with open(file,'r',encoding='utf8') as input_txt:
        output = re.sub(r'[^\x00-\x7F]+',' ', pinyin.get(emoji.demojize(input_txt.read()),format="numerical")
            .replace('。','.').replace('，',',').replace('？','?').replace('！','!')) # chinese char to pinyin (with common chinese punctuation)
    with open(file,'w') as output_txt:
        output_txt.write(output)

simplify(file)
