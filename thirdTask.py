import spacy
import nltk

# Question 1: Tokenization for Languages Other Than English

def tokenize_text(text, language):
  """Tokenizes text into sentences using spaCy for a specified language.

  Args:
    text: The input text to tokenize.
    language: The language code (e.g., 'fr' for French, 'de' for German).

  Returns:
    A list of sentences.
  """
  nlp = spacy.load(language)
  doc = nlp(text)
  sentences = [sent.text for sent in doc.sents]
  return sentences

# Get user input
user_text = input("Enter your text: ")
language = input("Enter language code (e.g., 'fr' for French, 'de' for German): ")

# Tokenize the text
sentences = tokenize_text(user_text, language)

# Print the sentences
print("Tokenized sentences:")
for sentence in sentences:
  print(sentence)

# Question 2: Part-of-Speech Tagging with Two Tagsets

def pos_tag_text(text, tagset):
  """Performs part-of-speech tagging using NLTK with a specified tagset.

  Args:
    text: The input text to tag.
    tagset: The tagset to use (e.g., 'universal', 'wsj').

  Returns:
    A list of tuples, where each tuple contains a word and its POS tag.
  """
  tokens = nltk.word_tokenize(text)
  tagged_tokens = nltk.pos_tag(tokens, tagset=tagset)
  return tagged_tokens

# Get user input
user_text = input("Enter your text: ")

# Tag with 'universal' tagset
universal_tags = pos_tag_text(user_text, 'universal')
print("\nPart-of-Speech Tags (Universal Tagset):")
for word, tag in universal_tags:
  print(f"{word}: {tag}")

# Tag with 'wsj' tagset
wsj_tags = pos_tag_text(user_text, 'wsj')
print("\nPart-of-Speech Tags (WSJ Tagset):")
for word, tag in wsj_tags:
  print(f"{word}: {tag}")

# Question 3: Get Common Stop Words in Various Languages

def get_stop_words(language):
  """Returns a list of common stop words for a given language.

  Args:
    language: The language code (e.g., 'english', 'french', 'spanish').

  Returns:
    A list of stop words.
  """
  return nltk.corpus.stopwords.words(language)

# Get user input
language = input("Enter language code (e.g., 'english', 'french', 'spanish'): ")

# Get stop words
stop_words = get_stop_words(language)
print(f"\nCommon Stop Words in {language.title()}:")
print(stop_words)