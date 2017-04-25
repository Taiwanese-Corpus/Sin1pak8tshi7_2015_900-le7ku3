from unittest.case import TestCase
from json2分詞 import 切詞條腔口


class 切詞條臺羅試驗(TestCase):
    def test_無腔口(self):
        結果 = 切詞條腔口("tsi̍t sian lâng")
        self.assertEqual(list(結果), ["tsi̍t sian lâng"])

    def test_有腔口(self):
        結果 = 切詞條腔口("jîn/lîn-tiong")
        self.assertEqual(list(結果), ["jîn-tiong", "lîn-tiong"])

    def test_三个腔口(self):
        結果 = 切詞條腔口("ling/ni/lin-bú/bó-tshia")
        self.assertEqual(list(結果), [
            "ling-bú-tshia",
            "ni-bó-tshia",
            "lin-bú-tshia"
        ])

    def test_輕聲(self):
        結果 = 切詞條腔口("ông--ko-liú--ko")
        self.assertEqual(list(結果), [
            "ông--ko-liú--ko",
        ])
