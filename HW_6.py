import requests
from collections import Counter
import matplotlib.pyplot as plt
import threading
from concurrent.futures import ThreadPoolExecutor
import re
from functools import reduce

# Get text from URL
def fetch_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching text from {url}: {e}")
        return ""

# text to words
def tokenize(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# Words frequency counter
def visualize_top_words(word_freq, top_n=10):
    top_words = word_freq.most_common(top_n)
    words, counts = zip(*top_words)

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} most frequent words')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# MapReduce
# Map
def map_function(text_chunk):
    words = tokenize(text_chunk)
    return Counter(words)

# Reduce
def reduce_function(counter1, counter2):
    return counter1 + counter2

# text to chunks
def split_text(text, num_chunks):
    chunk_size = len(text) // num_chunks
    return [text[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]

def analyze_word_frequency(url, num_threads=4, top_n=10):
    text = fetch_text(url)
    if not text:
        return

    text_chunks = split_text(text, num_threads)

    # ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        map_results = list(executor.map(map_function, text_chunks))

    total_word_count = reduce(reduce_function, map_results)

    visualize_top_words(total_word_count, top_n)

if __name__ == "__main__":

    url = "https://www.gutenberg.org/files/2600/2600-0.txt"  # "Війна і мир" Льва Толстого
    analyze_word_frequency(url, num_threads=4, top_n=10)
