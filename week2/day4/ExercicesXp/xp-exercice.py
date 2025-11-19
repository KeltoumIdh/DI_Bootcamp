#Exercise  Random sentence generator
print('Execise 1 :')

import random

def get_words_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()
        words = content.split()
        return words
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def get_random_sentence(length, file_path="words.txt"):
    words = get_words_from_file(file_path)
    if not words:
        return "No words available."

    sentence = " ".join(random.choice(words) for _ in range(length))
    return sentence.lower()

def main():
    print("This program generates a random sentence from a word list.")
    try:
        length = int(input("Enter sentence length (2–20): "))
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print("Generated sentence:", sentence)
        else:
            print("Error: Length must be between 2 and 20.")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()

#Exercise 2 working with json
print("Exeecise 2 : ")
import json

sampleJson = """{
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}"""

# Step 1: Load JSON string
data = json.loads(sampleJson)

# Step 2: Access nested key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Step 3: Add new key
data["company"]["employee"]["birth_date"] = "2002-05-15"

# Step 4: Save modified JSON to a file
with open("modified.json", "w") as f:
    json.dump(data, f, indent=4)