# Text Counter & Word Cloud Generator

This project analyzes a text file, counts word frequencies, and generates a word cloud visualization.

## Files

- [`word_counter.py`](c:/Users/anoop/OneDrive/Desktop/py/word_counter.py): Main script for counting words and generating visualizations.
- [`sample_text.txt`](c:/Users/anoop/OneDrive/Desktop/py/sample_text.txt): Example input text file.
- `top_words.csv`: Output CSV file with top word frequencies.
- `wordcloud.png`: Output image file of the word cloud.

## Usage

1. **Install dependencies:**

   ```sh
   pip install matplotlib nltk wordcloud
   ```

2. **Run the script:**

   ```sh
   python word_counter.py
   ```

3. **Results:**
   - Top words are printed in the terminal.
   - Top words and their frequencies are saved to `top_words.csv`.
   - A word cloud image is saved as `wordcloud.png`.

## Customization

- To analyze a different text file, change the filename in [`count_top_words`](c:/Users/anoop/OneDrive/Desktop/py/word_counter.py).
- Adjust the number of top words by modifying the `top_n` parameter.

## License

This project is for educational purposes.
