import re
import csv
import matplotlib.pyplot as plt
from collections import Counter
import nltk
nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud


lemmatizer = WordNetLemmatizer()


stop_words = set(stopwords.words("english"))

def count_top_words(file_path, top_n=20):
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().lower()

    
    words = re.findall(r"\b[a-z']+\b", text)

   
    filtered_words = [
        lemmatizer.lemmatize(w) for w in words if w not in stop_words
    ]

   
    word_counts = Counter(filtered_words)

   
    print("\nTop Words:\n")
    for word, freq in word_counts.most_common(top_n):
        print(f"{word}: {freq}")

   
    with open("top_words.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Frequency"])
        writer.writerows(word_counts.most_common(top_n))

    print("\nResults saved to top_words.csv")

   
    top_words = word_counts.most_common(top_n)
    words_, counts = zip(*top_words)
    plt.figure(figsize=(10, 5))
    plt.bar(words_, counts)
    plt.xticks(rotation=45)
    plt.title("Top Word Frequencies")
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.show()

  
    wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_counts)
    wc.to_file("wordcloud.png")
    print("Word cloud saved as wordcloud.png")


count_top_words("sample_text.txt", top_n=20)
