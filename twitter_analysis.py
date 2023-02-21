
import snscrape.modules.twitter as snt
import string
from collections import Counter
import matplotlib.pyplot as plt

def get_tweet():
    query="Corona Virus until:2021-01-01 since:2019-10-01"
    tweet_list=[]
    size=5000 

    for tweet in snt.TwitterSearchScraper(query).get_items():
        if len(tweet_list)==size:
            break
        else:
            tweet_list.append([tweet.content])
    return tweet_list;


text=""
tweet_ls=get_tweet()
length=len(tweet_ls)

for i in range(0,length):
    text=text+" "+tweet_ls[i][0]


lower_text=text.lower()
cleaned_text=lower_text.translate(str.maketrans("","",string.punctuation))


tokenised_words = cleaned_text.split()
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words=[]
for i in tokenised_words:
    if i not in stop_words:
        final_words.append(i)


emotion_list=[]
with open("C:\\Users\\asus\\OneDrive\\Desktop\\PROJECTS\\Sentiment-Analyser-ML-project\\emotion.txt","r") as file:
    for line in file:
        clear_line=line.replace("/n","").replace(",","").replace("'","").strip()
        word,emotion=clear_line.split(":")
        
        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w=Counter(emotion_list)
print(w)

fig,ax=plt.subplots()
ax.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig("bar_graph.png")
plt.show()