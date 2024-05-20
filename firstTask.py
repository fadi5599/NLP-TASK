# This program takes input text from the user and then asks the user to choose one of three options. Depending on the user's choice, it either prints tokenized words, tokenized sentences, or output using the split function.

import nltk

# Getting text input from the user ("multiple lines allowed")
text = []
print("Enter your text. Type 'end' on a separate line to finish.")
while True:
    line = input()
    if line == "end":
        break
    text.append(line)

text = " ".join(text)  # Join the lines into a single string

# Asking the user to choose an option
choice = int(input("Choose an option:\n1. Print tokenized words\n2. Print tokenized sentences\n3. Print output using split function\n"))

# Tokenizing the text based on the user's choice
if choice == 1:
    words = nltk.word_tokenize(text)
    print("Tokenized words: ", words)
elif choice == 2:
    sentences = nltk.sent_tokenize(text)
    print("Tokenized sentences: ", sentences)
elif choice == 3:
    words = text.split()
    print("Output using split function: ", words)
else:
    print("Invalid choice. Please choose 1, 2, or 3.")


"""NLTK is a leading platform for building Python programs to work with human
language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all,
NLTK is a free, open source, community-driven project."""