import sys
import warnings
from gensim.corpora import WikiCorpus
warnings.filterwarnings('ignore')


def make_corpus(in_f, out_f):
    """Convert Wikipedia xml dump file to text corpus"""

    output = open(out_f, 'w')
    wiki = WikiCorpus(in_f)

    i = 0

    for text in wiki.get_texts():
        try:
            output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
        except Exception:
            print("Failed article number : {}".format(i))
        i = i + 1
        if i % 100 == 0:
            print('##### Processed ' + str(i) + ' articles')

    output.close()
    print('Processing complete!')


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: python make_wiki_corpus.py <wikipedia_dump_file> <processed_text_file>')
        sys.exit(1)
    print("Running...")
    in_f = sys.argv[1]
    out_f = sys.argv[2]
    make_corpus(in_f, out_f)


