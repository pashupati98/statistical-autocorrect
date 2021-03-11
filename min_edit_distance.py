from data_prep import *


def min_edit_distance(source, target, ins_cost=1, del_cost=1, rep_cost=2):
    '''
    Input:
        source: a string corresponding to the string you are starting with
        target: a string corresponding to the string you want to end with
        ins_cost: an integer setting the insert cost
        del_cost: an integer setting the delete cost
        rep_cost: an integer setting the replace cost
    Output:
        D: a matrix of len(source)+1 by len(target)+1 containing minimum edit distances
        med: the minimum edit distance (med) required to convert the source string to the target
    '''

    m = len(source)
    n = len(target)
    # initialize cost matrix with zeros and dimensions (m+1,n+1)
    D = np.zeros((m + 1, n + 1), dtype=int)

    for row in range(1, m + 1):
        D[row, 0] = D[row - 1, 0] + del_cost

    for col in range(1, n + 1):
        D[0, col] = D[0, col - 1] + ins_cost

    # Loop through row 1 to row m
    for row in range(1, m + 1):
        # Loop through column 1 to column n
        for col in range(1, n + 1):
            # Intialize r_cost to the 'replace' cost
            r_cost = rep_cost
            # Check to see if source character at the previous row
            # matches the target character at the previous column,
            if source[row - 1] == target[col - 1]:
                # Update the replacement cost to 0 if source and target are the same
                r_cost = 0
            # Update the cost at row, col based on previous entries in the cost matrix
            D[row, col] = D[row - 1][col - 1] + r_cost

    # Set the minimum edit distance with the cost found at row m, column n
    med = D[m][n]

    return D, med


# Get correction based on this

def get_correct_word_bigram_min_edit(word, prev_word, probs, vocab, bigram_probability_df, unigram_weight,
                                     bigram_weight, n, scale_dist):
    corrections = get_corrections_bigram(word, prev_word, probs, vocab,
                                         bigram_probability_df, unigram_weight, bigram_weight, n, verbose=False)
    # print(corrections)
    if len(corrections) == 0:
        return word

    # Make a dataframe of suggestions
    words = []
    probabs = []
    dist = []
    for pair in corrections:
        words.append(pair[0])
        probabs.append(pair[1])
        _, distance = min_edit_distance(word, pair[0], 1, 1, 2)
        dist.append(distance)

    df = pd.DataFrame({'suggestion': words, 'distance': dist, 'probability': probabs})
    df['inv_dist'] = df['distance'].apply(lambda x: (1 / x) * scale_dist)
    df['score'] = df['inv_dist'] + df['probability']
    df = df.sort_values(by='score', ascending=False)
    # df = df.sort_values(by=['distance', 'probability'], ascending=[True, False])
    # display(df)

    final_word = df.iloc[0, 0]

    return final_word