from data_prep import *
from architecture import *
from bigram import *
from min_edit_distance import *


# Very Basic Auto-correct


def autocorrect(sentence, vocab, probs):
    print("Input sentence : ", sentence)
    wrong_words = find_wrong_word(sentence, vocab)
    print("Wrong words : ", wrong_words)
    #print(wrong_words)
    correct_words = []
    for word in sentence.strip().lower().split(" "):
        if word in wrong_words:
            correct_word = get_correct_word(word, vocab, probs, 15)
            #print(word, correct_word)
            word = correct_word
        correct_words.append(word)
    print("Output Sentence : ", " ".join(correct_words).capitalize())


# Improving this auto-correct by introducing bigram probabilities
# to get context from previous word

def autocorrect_bigram(sentence, vocab, probs, bigram_counts):
    print("Input sentence : ", sentence)
    wrong_words = find_wrong_word(sentence, vocab)
    print("Wrong words : ", wrong_words)
    # print(wrong_words)
    correct_words = []
    word_list = sentence.strip().lower().split(" ")
    for i, word in enumerate(word_list):
        # print(i, word)

        #### Previous word
        if i == 0:
            prev_word = '<s>'
        else:
            prev_word = word_list[i - 1]

        if word in wrong_words:
            correct_word = get_correct_word_bigram(word, prev_word, probs, vocab, bigram_counts, 0.3, 0.7, 10)
            # print(word, correct_word)
            word = correct_word
        correct_words.append(word)
    print("Output Sentence : ", " ".join(correct_words).capitalize())


# Improving further by introducing min edit distance functionality


def autocorrect_bigram_min_edit(sentence, vocab, probs, bigram_probability_df, scale_dist=0.001):
    print("Input sentence : ", sentence)
    wrong_words = find_wrong_word(sentence, vocab)
    print("Wrong words : ", wrong_words)
    # print(wrong_words)
    correct_words = []
    word_list = sentence.strip().lower().split(" ")
    for i, word in enumerate(word_list):
        # print(i, word)

        # Previous word
        if i == 0:
            prev_word = '<s>'
        else:
            prev_word = word_list[i - 1]

        if word in wrong_words:
            correct_word = get_correct_word_bigram_min_edit(word, prev_word, probs, vocab, bigram_probability_df, 0.3,
                                                            0.7, 25, scale_dist)
            # print(word, correct_word)
            word = correct_word
        correct_words.append(word)
    print("Output Sentence : ", " ".join(correct_words).capitalize())


# EOF
