from autocorrect import *

print("\n+++++ Basic Auto-correct System +++++\n")
autocorrect("he is goinng home", vocab, probs)
autocorrect("honsty is the best pooliccy", vocab, probs)
autocorrect("life is a diink annd lve is a druug", vocab, probs)


print("\n+++++ Bi-gram based Auto-correct System +++++\n")
autocorrect_bigram('she is really beutifule', vocab, probs, bigram_counts)
autocorrect_bigram('you are not alowwed here', vocab, probs, bigram_counts)
autocorrect_bigram('physics is the most amainzg subect', vocab, probs, bigram_counts)


print("+++++ Bi-gram & min edit distance based Auto-correct System +++++\n")
autocorrect_bigram_min_edit('I have acess to the lidrary', vocab, probs, bigram_counts)
autocorrect_bigram_min_edit('presnet for the meeating', vocab, probs, bigram_counts)
autocorrect_bigram_min_edit('he planed a game', vocab, probs, bigram_counts)

#EOF
