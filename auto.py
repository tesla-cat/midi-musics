from glob import glob
import json

with open('index.json','w',encoding='utf8') as f:
    json.dump([path[2:] for path in glob('./*.mid')], f, indent=2, ensure_ascii=False)
