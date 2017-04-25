from csv import DictReader
import json
from os.path import join, dirname, abspath


例句資料 = {}

with open(join(dirname(abspath(__file__)), '例句.csv')) as 檔:
        讀檔 = DictReader(檔)
        for row in 讀檔:
            漢字 = row['例句'].strip()
            音標 = row['例句標音'].strip()
            例句資料[漢字]=音標

print('055 160 169 177 184 佮例句表無仝，愛人工檢查！')

with open('minnan900.json') as jff:
    全部資料=json.load( jff)
    for 編號 in sorted(全部資料.keys()):
#         if 全部資料[編號]['例句漢字'] in 例句資料:
        try:
            全部資料[編號]['例句臺羅']=例句資料[全部資料[編號]['例句漢字']]
        except:
            print(編號)
        
with open('minnan900.json', 'w') as jff:
    json.dump(全部資料, jff, sort_keys=True, ensure_ascii=False, indent=2)
