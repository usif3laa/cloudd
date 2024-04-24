import nltk
import collections
from collections import Counter
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')
stop_words=stopwords.words('english')
file=open('paragraphs.txt','r')
data=file.read()
words =data.split()
filteredText = [word for word in words if not word.lower() in stop_words]
wordcount=Counter(filteredText)
for word,freq in wordcount.items():
    print(f"{word}:{freq}")


 


    