import warnings


class WordTokenizer:
    def __init__(self, tokenizer=None, flags=''):
        if tokenizer == 'KyTea':
            import Mykytea
            self.tokenizer = Mykytea.Mykytea(flags)
            self.tokenize = self._kytea_tokenize

        elif tokenizer == 'MeCab':
            import natto
            flags = '-Owakati' if not flags else flags
            self.tokenizer = natto.MeCab(flags)
            self.tokenize = self._mecab_tokenize

        else:
            warnings.warn('Return input directly')
            self.tokenizer = None
            self.tokenize = lambda x: x

    def _mecab_tokenize(self, sentence):
        return self.tokenizer.parse(sentence)

    def _kytea_tokenize(self, sentence):
        return ' '.join(self.tokenizer.getWS(sentence))


if __name__ == '__main__':
    word_tokenizer = WordTokenizer('KyTea')
    res = word_tokenizer.tokenize('我輩は猫である')
    print(res)
    word_tokenizer = WordTokenizer('MeCab')
    res = word_tokenizer.tokenize('我輩は猫である')
    print(res)
