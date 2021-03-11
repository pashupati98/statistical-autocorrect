from autocorrect import *

print("+++++ Basic Auto-correct System +++++\n")
autocorrect("I was on hime", vocab, probs)
autocorrect("Lerning is tha best", vocab, probs)
autocorrect("life iis a drink annd lave is a drung", vocab, probs)

print("+++++ Bi-gram based Auto-correct System +++++\n")
autocorrect_bigram('I was on hime', vocab, probs, bigram_probability_df)

print("+++++ Bi-gram & min edit distance based Auto-correct System +++++\n")
autocorrect_bigram_min_edit('I was on hime', vocab, probs, bigram_probability_df)

