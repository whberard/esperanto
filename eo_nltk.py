
import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import udhr

# Put the raw text of the Universal Declaration of Human Rights
# in Esperanto into raw_text.
raw_text = udhr.raw(u'Esperanto-UTF8')

# Show plot of letter frequency.
#nltk.FreqDist(raw_text).plot()

from bs4 import BeautifulSoup

raw = BeautifulSoup(raw_text, "html.parser").get_text()

print type(raw)
tokens = word_tokenize(raw)

print "Num tokens = ", len(tokens)
