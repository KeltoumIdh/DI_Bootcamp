#Daily Challenge
import string
import re

# Step 1: Create the Text class
class Text:
    def __init__(self, text):
        # Store the text in an attribute
        self.text = text

    # Step 2: word_frequency method
    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        return count if count > 0 else None

    # Step 3: most_common_word method
    def most_common_word(self):
        words = self.text.split()
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        return max(freq, key=freq.get)

    # Step 4: unique_words method
    def unique_words(self):
        words = self.text.split()
        return list(set(words))

    # Step 5: from_file class method
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as f:
            content = f.read()
        return cls(content)


# Step 6: Bonus - TextModification class
class TextModification(Text):
    # Remove punctuation
    def remove_punctuation(self):
        return self.text.translate(str.maketrans("", "", string.punctuation))

    # Remove stop words
    def remove_stop_words(self, stop_words=None):
        if stop_words is None:
            stop_words = ["a", "the", "is", "and", "in", "to", "of"]
        words = self.text.split()
        filtered = [w for w in words if w.lower() not in stop_words]
        return " ".join(filtered)

    # Remove special characters
    def remove_special_characters(self):
        return re.sub(r"[^A-Za-z0-9\s]", "", self.text)


# Step 7: Testing the classes
if __name__ == "__main__":
    sample_text = "Python is great, and Python is fun!"

    # Using Text class
    t = Text(sample_text)
    print("Word frequency of 'Python':", t.word_frequency("Python"))   # 2
    print("Most common word:", t.most_common_word())                   # Python
    print("Unique words:", t.unique_words())                           # ['Python', 'is', 'great,', 'and', 'fun!']

    # Using TextModification class
    tm = TextModification(sample_text)
    print("Without punctuation:", tm.remove_punctuation())             # Python is great and Python is fun
    print("Without stop words:", tm.remove_stop_words())               # Python great, Python fun!
    print("Without special characters:", tm.remove_special_characters()) # Python is great and Python is fun