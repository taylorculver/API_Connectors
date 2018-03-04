"""Shows keys for tweet"""
import json
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns


tweets_data_path = 'tweets.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()
print(tweets_data[0].keys())


"""Build data frame"""
data_frame = pd.DataFrame(tweets_data, columns=['user'])  # filters for columns on data
print(data_frame.iteritems())
print(data_frame.get_values())

"""Tweet counts by text"""
def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False


"""Visualize tweet counts"""
# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]


# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in data_frame.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

print([clinton, trump, sanders, cruz])


"""Build Histogram of Tweet Results"""
# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
