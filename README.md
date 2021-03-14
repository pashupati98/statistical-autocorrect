# Statistical Auto-correct System
<div>
<p>The task of an auto-correct system is finding out which words in a document are misspelled. These mispelled words might be presented to a user by underlining that words. Correction is the task of substituting the well-spelled word for misspellings.
</p>
<img style="align:center", src="https://github.com/pashupati98/kaggle-archives/blob/main/img/img2.PNG?raw=true">
    <hr>
    <p>The very first requirement of auto-correct system is data. We need a trusted text corpus that we'll use to build the auto-correct system. There are many public domain text corpus. Since it's a unsupervised type of problem here what we need is just text. One can use any competition data or any other public dataset that has text field column. In the currect version I have used small fraction of wiki corpus.</p>
</div>

## Architecture

<div>
<img style="align:center", src="https://github.com/pashupati98/kaggle-archives/blob/main/img/architecture.png?raw=true">
    <hr>
</div>

This auto-correct architecture has 4 components -
- 1) Filtering Mispells : One simple approach could be checking if a word is there in the vocabulary or not. 
- 2) Word Suggestion Mechanism : This mechnism suggests candidate words based on deletion, insertion, switch or replace of one/two characters in the original word.
- 3) Probability Distribution Mechanism : The probability distribution {key(word) : value(probability)} is created calculated using a large text corpus. Probability of each candidate is found using this distribution and the most probable candidate is the final one.
- 4) Replace Mispells : Simple replace the mispelled word with the most probable suggestion.

Note - Refer the architecture.py file to see the implementation of the architecture.

### This is very simplified architecture compared to what is used in reality. Hernce it's performance will be not be very good. But we can make some improvemts in this architecture to get better results.

#### Drawbacks 
- It has fixed outcome. i.e. 'hime' will be converted to 'time' only (because 'time' is more frequent word hence more probable one) not 'home' or anything else.
- It is solely based on frequency of words in the corpus.
- Doesn't care about the contex.
- Doesn't care about part of speech, grammer or punctuations.
- Can't suggest something which is not in the vocabulary

#### Improvements
1) It can be further improved by introducing bi-gram probabilities. Hence, it will get some inference from previous words.
2) The suggestions that are less distance away from the misspelled word are more likely. Hence, the system can be further improved by introducing dynamic programming based min edit distance functionality.

#### Details of the improvements

### Improvement 1 : Introducing n-gram probabilities to get context from previous words

This idea is taken from the n-grams language models. In a n-gram language model
- Assume the probability of the next word depends only on the previous n-gram.
- The previous n-gram is the series of the previous 'n' words.

The conditional probability for the word at position 't' in the sentence, given that the words preceding it are $w_{t-1}, w_{t-2} \cdots w_{t-n}$ is:

$$ P(w_t | w_{t-1}\dots w_{t-n}) \tag{1}$$

This probability cab be estimated by counting the occurrences of these series of words in the training data.
- The probability can be estimated as a ratio, where
- The numerator is the number of times word 't' appears after words t-1 through t-n appear in the training data.
- The denominator is the number of times word t-1 through t-n appears in the training data.

<img src="https://github.com/pashupati98/statistical-autocorrect/blob/master/img/prob.PNG?raw=true">

In other words, to estimate probabilities based on n-grams, first find the counts of n-grams (for denominator) then divide it by the count of (n+1)-grams (for numerator).

- The function $C(\cdots)$ denotes the number of occurence of the given sequence. 
- $\hat{P}$ means the estimation of $P$. 
- The denominator of the above equation is the number of occurence of the previous $n$ words, and the numerator is the same sequence followed by the word $w_t$.

Now the issue with above formula is that it doesn't work when a count of an n-gram is zero..
- Suppose we encounter an n-gram that did not occur in the training data.  
- Then, the equation (2) cannot be evaluated (it becomes zero divided by zero).

A way to handle zero counts is to add k-smoothing.  
- K-smoothing adds a positive constant $k$ to each numerator and $k \times |V|$ in the denominator, where $|V|$ is the number of words in the vocabulary.

<img src="https://github.com/pashupati98/statistical-autocorrect/blob/master/img/smoothing.PNG?raw=true">


For n-grams that have a zero count, the equation (3) becomes $\frac{1}{|V|}$.
- This means that any n-gram with zero count has the same probability of $\frac{1}{|V|}$.

Now, let's define a function that computes the probability estimate (3) from n-gram counts and a constant $k$.

### Improvement 2 : Introducing min_edit_diatsnce functionality

The idea is derived from the intution that the suggestions that are less distance away from the misspelled word are more likely. Hence, the system can be further improved by introducing dynamic programming based min edit distance functionality.

So, given a string source[0..i] and a string target[0..j], we will compute all the combinations of substrings[i, j] and calculate their edit distance. To do this efficiently, we will use a table to maintain the previously computed substrings and use those to calculate larger substrings.

We'll first create a matrix and update each element in the matrix as follows:

<img src="https://github.com/pashupati98/statistical-autocorrect/blob/master/img/dp.PNG?raw=true">
