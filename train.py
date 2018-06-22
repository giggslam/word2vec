# -*- coding: utf-8 -*-
# 2018-06-22, allow Input/Output argurments passing by command

import logging
import sys

from gensim.models import word2vec

def main():
    Input = sys.argv[1] if sys.argv[1:] else 'Data/wiki_seg.txt'
    Output = sys.argv[2] if sys.argv[2:] else 'Model/word2vec.model'
    train(Input, Output)

def train(Input='Data/wiki_seg.txt',Output='Model/word2vec.model'):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    sentences = word2vec.LineSentence(Input)
    #class gensim.models.word2vec.Word2Vec(sentences=None, size=100, alpha=0.025, window=5, min_count=5, max_vocab_size=None, sample=0.001, seed=1, workers=3, min_alpha=0.0001, sg=0, hs=0, negative=5, cbow_mean=1, hashfxn=<built-in function hash>, iter=5, null_word=0, trim_rule=None, sorted_vocab=1, batch_words=10000)
    #model = word2vec.Word2Vec(sentences, size=250)
    model = word2vec.Word2Vec(sentences, size=250, workers=4)

    #保存模型，供日後使用
    model.save(Output)

    #模型讀取方式
    # model = word2vec.Word2Vec.load("your_model_name")


if __name__ == "__main__":
    main()