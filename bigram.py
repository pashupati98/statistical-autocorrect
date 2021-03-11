from data_prep import *
from architecture import  *

# A function to count n-grams


def count_n_grams(data, n, start_token='<s>', end_token='<e>'):
    # Initialize dictionary of n-grams and their counts
    n_grams = {}

    for sentence in data:

        # prepend start token n times, and  append <e> one time
        sentence = [start_token] * n + sentence + [end_token]
        sentence = tuple(sentence)

        for i in range(len(sentence) - n):
            n_gram = sentence[i:i + n]
            if n_gram in n_grams.keys():
                n_grams[n_gram] += 1
            else:
                n_grams[n_gram] = 1
    return n_grams

# A function to make the count matrix


def make_count_matrix(n_plus1_gram_counts, vocabulary):
    # add <e> <unk> to the vocabulary
    # <s> is omitted since it should not appear as the next word
    vocabulary = vocabulary + ["<e>", "<unk>"]

    # obtain unique n-grams
    n_grams = []
    for n_plus1_gram in n_plus1_gram_counts.keys():
        n_gram = n_plus1_gram[0:-1]
        n_grams.append(n_gram)
    n_grams = list(set(n_grams))

    # mapping from n-gram to row
    row_index = {n_gram: i for i, n_gram in enumerate(n_grams)}
    # mapping from next word to column
    col_index = {word: j for j, word in enumerate(vocabulary)}

    nrow = len(n_grams)
    ncol = len(vocabulary)
    count_matrix = np.zeros((nrow, ncol))
    for n_plus1_gram, count in n_plus1_gram_counts.items():
        n_gram = n_plus1_gram[0:-1]
        word = n_plus1_gram[-1]
        if word not in vocabulary:
            continue
        i = row_index[n_gram]
        j = col_index[word]
        count_matrix[i, j] = count

    count_matrix = pd.DataFrame(count_matrix, index=n_grams, columns=vocabulary)
    return count_matrix

# A function to make probability matrix

def make_probability_matrix(n_plus1_gram_counts, unique_words, k):
    count_matrix = make_count_matrix(n_plus1_gram_counts, unique_words)
    count_matrix += k
    prob_matrix = count_matrix.div(count_matrix.sum(axis=1), axis=0)
    return prob_matrix

# Function check


bigram_counts = count_n_grams(tokenized_data, 2)
vocab = list(set(vocab))
bigram_probability_df = make_probability_matrix(bigram_counts, vocab, k=1)
# print(bigram_probability_df.head())

# Getting correction based on bigrams


def get_corrections_bigram(word, prev_word, probs, vocab, bigram_probability_df, unigram_weight=0.3, bigram_weight=0.7,
                           n=5, verbose=False):
    '''
    Input:
        word: a user entered string to check for suggestions
        probs: a dictionary that maps each word to its probability in the corpus
        vocab: a set containing all the vocabulary
        n: number of possible word corrections you want returned in the dictionary
    Output:
        n_best: a list of tuples with the most probable n corrected words and their probabilities.
    '''

    suggestions = []
    n_best = []

    if word in probs.keys():
        suggestions.append(word)
    for w in edit_one_letter(word):
        if len(suggestions) == n:
            break
        if w in probs.keys():
            suggestions.append(w)
    for w in edit_two_letters(word):
        if len(suggestions) == n:
            break
        if w in probs.keys():
            suggestions.append(w)

    ##### Probabilities for suggestions
    try:
        bigram_df_row_index = bigram_probability_df.index.tolist().index(tuple([prev_word]))
        bigram_df_row = bigram_probability_df.iloc[bigram_df_row_index]
    except:
        bigram_df_row = []
    # print(bigram_df_row)

    best_words = {}

    for s in suggestions:
        # best_words[s] = probs[s]
        unigram_prob = probs[s]
        # print(s)
        if s in bigram_df_row:
            bigram_prob = bigram_df_row[s]
        else:
            bigram_prob = 0

        final_score = unigram_weight * unigram_prob + bigram_weight * bigram_prob

        best_words[s] = final_score

    best_words = sorted(best_words.items(), key=lambda x: x[1], reverse=True)

    n_best = best_words

    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best


def get_correct_word_bigram(word, prev_word, probs, vocab, bigram_probability_df, unigram_weight, bigram_weight, n):
    corrections = get_corrections_bigram(word, prev_word, probs, vocab,
                                         bigram_probability_df, unigram_weight, bigram_weight, n, verbose=False)
    # print(corrections)
    if len(corrections) == 0:
        return word

    final_word = corrections[0][0]
    final_prob = corrections[0][1]
    for i, word_prob in enumerate(corrections):
        # print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")
        if word_prob[1] > final_prob:
            final_word = word_prob[0]
            final_prob = word_prob[1]
    return final_word


