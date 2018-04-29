# -*- coding: utf-8 -*-

import logging

from gensim.models import word2vec

def main():
    train()

def train(Input='Data/wiki_seg.txt',Output='Model/word2vec.model'):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    sentences = word2vec.LineSentence(Input)
    #model = word2vec.Word2Vec(sentences, size=250)
    model = word2vec.Word2Vec(sentences, size=250, workers=4)

    #保存模型，供日後使用
    model.save(Output)

    #模型讀取方式
    # model = word2vec.Word2Vec.load("your_model_name")


if __name__ == "__main__":
    main()
