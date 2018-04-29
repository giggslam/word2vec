# word2vec by Gensim

## Package Requirement

* jieba
```
pip3 install jieba
```
* gensim
```
pip3 install -U gensim
```
* [OpenCC](https://github.com/BYVoid/OpenCC) (繁簡轉換)

## Pipline

1. Download [wiki_data](https://dumps.wikimedia.org/zhwiki/) (zhwiki-20180428-pages-articles.xml.bz2, 1.46GB, suffex: `pages-articles.xml.bz2`),
saved to sub-folder "Data"

2. Extract text from xml by `wiki_to_txt.py` (~50mins, i7-860)
```
python wiki_to_txt.py Data\zhwiki-20160820-pages-articles.xml.bz2
```

3. Convert ST to TW by OpenCC (~10mins, i7-860)
```
.\opencc\opencc.exe -i Data\wiki_texts.txt -o Data\wiki_zh_tw.txt -c opencc\s2tw.json
```

4. word segmentation (delete stop word) by jieba (~xxmins, i7-860)
```
python segment.py
```

5. train word2vec by gensim (~xxmings, i7-860)
```
python train.py
```

6. Test
```
python demo.py
```