# 新北市104學年度閩南語字音字形900例句工作坊

## 資料流程
`minnan900.pdf`=>`minnan900.txt`=>`minnan900.json`=>`minnan900.分詞`

### minnan900.pdf（無維護）
原始CD檔案

### minnan900.txt（無維護）
```
pdftotext minnan900.pdf -raw
```

### minnan900.json（有維護）
```
python3 txt2.json.py
```
會當用`json_fixed_by_moedict.py`檢查

### minnan900.分詞（有維護）
```
python3 json2分詞.py
```

佮json無仝步的所在：
- https://github.com/Taiwanese-Corpus/Sin1pak8tshi7_2015_900-le7ku3/commit/51998221987471a90947529db8212e58c33dd6c5
