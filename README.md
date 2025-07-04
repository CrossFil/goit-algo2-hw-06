# Task:  Word Frequency Analysis via MapReduce and Visualization

**Objective**  
Write a Python script that downloads text from a given URL, analyzes word frequencies using the MapReduce paradigm, and visualizes the top-N most frequent words.

**Step‑by‑Step Instructions**  
1. **Import required modules**  
   - e.g. `requests`, `re`, `collections`, `matplotlib.pyplot`, `threading`, `ThreadPoolExecutor`, `reduce`
2. **MapReduce implementation**  
   - Reuse the MapReduce code from your notes or previous assignments  
3. **Data fetching**  
   - Download the raw text content from the specified URL  
4. **Word counting**  
   - **Map**: split text into words, normalize case and strip punctuation  
   - **Reduce**: aggregate counts per word  
5. **Visualization**  
   - Implement a function `visualize_top_words(word_counts: dict, top_n: int)`  
   - Plot a bar chart of the top‑N words by frequency  
6. **Main block**  
   - Fetch text from URL  
   - Execute MapReduce to produce `word_counts`  
   - Call `visualize_top_words(word_counts, top_n=10)`

