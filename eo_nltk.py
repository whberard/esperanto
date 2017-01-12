
import nltk
from nltk import word_tokenize
from nltk.corpus import udhr

# Put the raw text of the Universal Declaration of Human Rights
# in Esperanto into raw_text.
# raw_text = udhr.raw(u'Esperanto-UTF8')

# Show plot of letter frequency.
#nltk.FreqDist(raw_text).plot()

from bs4 import BeautifulSoup

myfile = open("./tekstaro-de-esperanto/tekstoj-xml/la-faraono.xml")
raw_text = myfile.read()
#print raw_text[0:200]
raw = BeautifulSoup(raw_text, "html.parser").get_text()


# print type(raw)
tokens = word_tokenize(raw)

print "Num tokens = ", len(tokens)
print "First few tokens: ", tokens[0:100]

# print raw.concordance(u'Tiu')

text = nltk.Text(tokens)
print type(text)

text.collocations()
#text.concordance(u'sankteco')
text.similar(u'soldato')

sortwds = sorted(set(text))
print sortwds[0:20]


