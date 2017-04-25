import json
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
import re

校對到 = 150


def 切詞條腔口(詞條臺羅):
    上濟腔口 = 0
    切臺羅結果 = re.split('(-| )', 詞條臺羅)
    for 臺羅 in 切臺羅結果[::2]:
        數量 = len(臺羅.split('/'))
        if 數量 > 上濟腔口:
            上濟腔口 = 數量
    for 唸第幾擺 in range(上濟腔口):
        這擺臺羅 = []
        for 第幾个, 這个 in enumerate(切臺羅結果):
            if 第幾个 % 2 == 1:
                這擺臺羅.append(這个)
            else:
                這格有 = 這个.split('/')
                這擺臺羅.append(這格有[唸第幾擺 % len(這格有)])
        yield ''.join(這擺臺羅)


def main():
    with open('minnan900.json') as jff:
        全部資料 = json.load(jff)
    with open('minnan900.分詞', 'w') as 分詞檔案:
        for 編號, 內容 in sorted(全部資料.items()):
            if int(編號) > 校對到:
                break
            詞條 = []
            for 詞條臺羅 in 切詞條腔口(內容[ '詞條臺羅']):
                詞條.append(
                    拆文分析器.對齊組物件(
                        內容['詞條漢字'],
                        文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 詞條臺羅)
                    ).轉音(臺灣閩南語羅馬字拼音).看分詞()
                )
            print(' '.join(詞條), file=分詞檔案)
            章物件 = 拆文分析器.對齊章物件(
                內容['例句漢字'],
                文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 內容['例句臺羅'])
            ).轉音(臺灣閩南語羅馬字拼音)
            print(章物件.看分詞(), file=分詞檔案)


main()
