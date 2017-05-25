import utils
from collections import Counter
import helper

data_dir = 'data/text_data'
text = helper.load_data(data_dir)
# Ignore notice, since we don't use it for analysing the data
text = text[81:]

def create_lookup_tables(text):
    """
    Create lookup tables for vocabulary
    :param text: The text of tv scripts split into words
    :return: A tuple of dicts (vocab_to_int, int_to_vocab)
    """

    vocab_to_int, int_to_vocab = utils.create_lookup_tables(text)
    return (vocab_to_int, int_to_vocab)


def preprocess(text):
    # Replace punctuation with tokens so we can use them in our model
    text = text.lower()
    """
    text = text.replace('.', ' <PERIOD> ')
    text = text.replace(',', ' <COMMA> ')
    text = text.replace('"', ' <QUOTATION_MARK> ')
    text = text.replace(';', ' <SEMICOLON> ')
    text = text.replace('!', ' <EXCLAMATION_MARK> ')
    text = text.replace('?', ' <QUESTION_MARK> ')
    text = text.replace('(', ' <LEFT_PAREN> ')
    text = text.replace(')', ' <RIGHT_PAREN> ')
    text = text.replace('--', ' <HYPHENS> ')
    text = text.replace('?', ' <QUESTION_MARK> ')
    # text = text.replace('\n', ' <NEW_LINE> ')
    text = text.replace(':', ' <COLON> ')
    """
    words = text.split()

    word_counts = Counter(words)

    return word_counts

vocab = preprocess(text)

f = open('data/vocab2', 'w')
for (word, n) in vocab.most_common():
    f.write("{} {}\n".format(word,n))