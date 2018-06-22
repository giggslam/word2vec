# word2vec by Gensim

2018-05-06

## Package Requirement

* jieba

``` bash
pip install jieba
```

* gensim

``` python
pip install -U gensim
```

* [OpenCC](https://github.com/BYVoid/OpenCC) (繁簡轉換)

## Pipeline

(1) Download [zh wiki_data](https://dumps.wikimedia.org/zhwiki/) (zhwiki-20180428-pages-articles.xml.bz2, 1.46GB, suffex: `pages-articles.xml.bz2`)([維基百科：數據庫下載](https://zh.wikipedia.org/wiki/Wikipedia:数据库下载)),
saved to sub-folder `Data`
<br>[en wiki_data](https://dumps.wikimedia.org/enwiki/)(enwiki-20180601-pages-articles.xml.bz2, 14GB)([Wikipedia:Database_download](https://en.wikipedia.org/wiki/Wikipedia:Database_download))

(2) Extract text from xml by `wiki_to_txt.py` (zh ~50mins; en 18,525,288 articles ~303mins; i7-860)

``` bash
#!/bin/bash
python wiki_to_txt.py Data\zhwiki-20160820-pages-articles.xml.bz2
```

(3) Convert ST to TW by OpenCC (~10mins, i7-860)

``` bash
.\opencc\opencc.exe -i Data\wiki_texts.txt -o Data\wiki_zh_tw.txt -c opencc\s2tw.json
```

(4) word segmentation (delete stop word) by jieba (~xxmins, i7-860)

``` bash
python segment.py
```

(5) train word2vec by gensim (~30mings, i7-860)
``` python
# gensim Default
class gensim.models.word2vec.Word2Vec(sentences=None, size=100, alpha=0.025, window=5, min_count=5, max_vocab_size=None, sample=0.001, seed=1, workers=3, min_alpha=0.0001, sg=0, hs=0, negative=5, cbow_mean=1, hashfxn=<built-in function hash>, iter=5, null_word=0, trim_rule=None, sorted_vocab=1, batch_words=10000)

# Current running
model = word2vec.Word2Vec(sentences, size=250)
```

``` bash
python train.py
```

(6) Test

``` bash
python demo.py
```