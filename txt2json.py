import json
import re


全部資料 = {}
with open('minnan900.txt') as ff:
    倒爿 = None
    正爿 = None
    for ll in ff:
        gg = re.search('(^\d\d\d) ([^ ]*) (.*) (\d\d\d) ([^ ]*) (.*)', ll)
        if gg:
            if 倒爿 is not None:
                全部資料[倒爿['編號']] = 倒爿
                全部資料[正爿['編號']] = 正爿
            倒爿 = {
                '編號': gg.group(1),
                '詞條漢字': gg.group(2),
                '詞條臺羅': gg.group(3),
                '例句漢字': '',
                '例句臺羅': '',
            }
            正爿 = {
                '編號': gg.group(4),
                '詞條漢字': gg.group(5),
                '詞條臺羅': gg.group(6),
                '例句漢字': '',
                '例句臺羅': '',
            }
        elif 倒爿 is None:
            continue
        elif re.search('[a-z]', ll):
            if 正爿['例句漢字'] == '':
                倒爿['例句臺羅'] += ' ' + ll.strip()
            else:
                正爿['例句臺羅'] += ' ' + ll.strip()
        else:
            if 倒爿['例句臺羅'] == '':
                倒爿['例句漢字'] += ' ' + ll.strip()
            else:
                正爿['例句漢字'] += ' ' + ll.strip()
with open('minnan900.json', 'w') as jff:
    json.dump(全部資料, jff, sort_keys=True, ensure_ascii=False, indent=2)
