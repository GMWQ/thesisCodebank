# Vader Sentiments

from VaderSentiment.VaderSentiment import SentimentIntensityAnalyzer as sia

analyser = sia()

pos = 0
neu = 0
neg = 0
total = 0

file = open(r"C:\Users\u180530\Desktop\FYP\Data\Final\Accuracy\MexicoAccuracyPos2.txt", "w+")

file_object = open(r"C:\Users\u180530\Desktop\FYP\Data\Final\Annotations\Positives.txt", encoding = 'ansi')

for line in file_object:
    vs = analyser.polarity_scores(line)
    print("{:-<65} {}".format(line, str(vs)) + '\n')
    if vs['compound'] > 0:
        pos += 1
        total += 1
    elif vs['compound'] < 0:
        neg += 1
        total += 1
    else:
        neu +=1
        total += 1
        
    file.write("{:-<65} {}".format(line, str(vs)) + '\n\n')
 
print("Percentage of positive tweets: {}%".format(pos*100/total))
print("Percentage of neutral: {}%".format(neu*100/total))
print("Percentage of negative tweets: {}%".format(neg*100/total)) 

with open(r"C:\Users\u180530\Desktop\FYP\Data\Final\Accuracy\MexicoAccuracyPos2.txt", "a") as polapp:
    polapp.write('\n\n' + "Percentage of positive tweets: {}%".format(pos*100/total) + '\n') 
    polapp.write("Percentage of neutral: {}%".format(neu*100/total) + '\n') 
    polapp.write("Percentage of negative tweets: {}%".format(neg*100/total) + '\n')
    