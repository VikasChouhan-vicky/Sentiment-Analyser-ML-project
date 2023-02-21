##step to clean a data 
#import the file
#first convert the whole string into lower case 
#remove all the special symbols
#create token_ised words : means break the sentence in individual words
#filter out the stop words from the tokenised words

#open emotion.txt file
#slit the lines and get read of spaces,commas and anything other than what separates word and emotion in this case ":" is the separated 
#split and store words and empotions in different variable
#if word is present --> append it to a new list for further use 
#count the emotions

import string
from collections import Counter
import matplotlib.pyplot as plt


text = open("C:\\Users\\asus\\OneDrive\\Desktop\\PROJECTS\\Sentiment-Analyser-ML-project\\cleaner_trial.txt",encoding='utf-8').read()

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