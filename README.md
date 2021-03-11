# Statistical Auto-correct System
<div>
<p>The task of an auto-correct system is finding out which words in a document are misspelled. These mispelled words might be presented to a user by underlining that words. Correction is the task of substituting the well-spelled word for misspellings.
</p>
<img style="align:center", src="https://github.com/pashupati98/kaggle-archives/blob/main/img/img2.PNG?raw=true">
    <hr>
    <p>The very first requirement of auto-correct system is data. I have checked multiple data sources and will be using one of them.</p>
    <p>We need a trusted text corpus that we'll use to build the auto-correct system. There are many public domain text corpus. Since it's a unsupervised type of problem here what we need is just text. You can use any competition data or any other public dataset that has text field column. In the currect version I have used shakespeare corpus. Since. it's a very small corpus we need to compromise on word probabilities.</p>
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

We'll impliment each part separetely.
