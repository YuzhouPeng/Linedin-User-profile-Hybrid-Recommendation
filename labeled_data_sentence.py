from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from random import shuffle
class LabeledLineSentence(object):
    def __init__(self, pos_doc_list,pos_label_list):
        self.pos_doc_list = pos_doc_list
        self.pos_label_list = pos_label_list



    def __iter__(self):
        for index, doc in enumerate(self.pos_doc_list):
            yield LabeledSentence(words = doc.split(),labels = [self.pos_label_list[index]])


    def to_array(self):
        self.sentences = []
        for index, doc in enumerate(self.pos_doc_list):
            self.sentences.append(LabeledSentence(doc.split(),[self.pos_label_list[index]]))

        return self.sentences


    def sentences_perm(self):
        shuffle(self.sentences)
        return self.sentences
