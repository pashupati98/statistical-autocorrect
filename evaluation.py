from autocorrect import *
from unit_test import *

def test_autocorrect(utdata, vocab, probs, string):
    tcount = 0
    fcount = 0
    rcount = 0
    print("Running "+string+" : Basic Auto-correct system")
    for k, v in utdata.items():
        incorrect_list = v.strip().split()
        #print(incorrect_list)
        for w in incorrect_list:
            tcount = tcount + 1
            cw = get_correct_word(w, vocab, probs, 25)
            if cw==k:
                #print('correct')
                rcount = rcount + 1
            else:
                #print('wrong')
                fcount = fcount + 1
    print("Accuracy : {} %".format((rcount/tcount)*100))


def test_autocorrect_bigram(utdata, vocab, probs, string, bigram_counts):
    tcount = 0
    fcount = 0
    rcount = 0
    print("Running "+string+" : Bi-gram Auto-correct system")
    for k, v in utdata.items():
        incorrect_list = v.strip().split()
        #print(incorrect_list)
        for w in incorrect_list:
            tcount = tcount + 1
            cw = get_correct_word_bigram(w, '<s>', probs, vocab, bigram_counts, 0.3, 0.7, 25)
            if cw==k:
                #print('correct')
                rcount = rcount + 1
            else:
                #print('wrong')
                fcount = fcount + 1
    print("Accuracy : {} %".format((rcount/tcount)*100))


def test_autocorrect_bigram_min_edit(utdata, vocab, probs, string, bigram_counts):
    tcount = 0
    fcount = 0
    rcount = 0
    print("Running "+string+" : Bi-gram (min-edit) Auto-correct system")
    for k, v in utdata.items():
        incorrect_list = v.strip().split()
        #print(incorrect_list)
        for w in incorrect_list:
            tcount = tcount + 1
            cw = get_correct_word_bigram_min_edit(w, '<s>', probs, vocab, bigram_counts, 0.3, 0.7, 25, 0.000001)
            if cw==k:
                #print('correct')
                rcount = rcount + 1
            else:
                #print('wrong')
                fcount = fcount + 1
    print("Accuracy : {} %".format((rcount/tcount)*100))


# Test basic auto-correct
test_autocorrect(tests1, vocab, probs, "Unit Test 1")
test_autocorrect(tests2, vocab, probs, "Unit Test 2")

# test_autocorrect_bigram(tests1, vocab, probs, "Unit Test 1", bigram_counts)
# test_autocorrect_bigram(tests2, vocab, probs, "Unit Test 2", bigram_counts)

# test_autocorrect_bigram_min_edit(tests1, vocab, probs, "Unit Test 1", bigram_counts)
# test_autocorrect_bigram_min_edit(tests2, vocab, probs, "Unit Test 2", bigram_counts)

# EOF