# **Week 11 – Natural Language Processing (NLP)**

This week focuses on applying core Natural Language Processing techniques to the Fake News Detection project, which is a text-based classification problem. Both traditional NLP methods and deep learning approaches were explored to understand how machines process and classify textual information.

# Tasks Completed
**Class Task – Tokenization & Word Embeddings (Deep Learning)**

* Loaded the Fake News dataset containing news articles labeled as Real or Fake

* Cleaned and preprocessed text data

* Tokenized news articles and converted them into sequences

* Applied sequence padding to ensure uniform input length

* Built a deep learning model using:

   * Embedding Layer

   * LSTM Layer

   * Dense Output Layer

   * Trained the model for fake news classification

   * Evaluated model performance using accuracy and classification metrics

**Assignment 11 – NLP Preprocessing (TF-IDF Pipeline)**

Applied text cleaning:

* Lowercasing

* Removing punctuation and noise

* Performed tokenization

* Removed English stopwords

* Applied lemmatization using WordNet

* Converted processed text into numerical features using TF-IDF

* Trained a Logistic Regression classifier on TF-IDF vectors

* Evaluated classification accuracy and performance

# Key Insights

* Tokenization converts raw news text into machine-readable form

* TF-IDF highlights important and discriminative words in fake vs real news

* Word embeddings capture semantic relationships between words

* LSTM models effectively learn sequential patterns and context in news articles

* Traditional NLP pipelines remain highly effective for text classification tasks

# Why NLP Is Essential for This Project

The Fake News Detection dataset consists entirely of textual news content, making NLP a core requirement:

* News articles contain unstructured text

* Tokenization, TF-IDF, and embeddings are necessary

* RNN/LSTM models significantly improve performance by learning context and sequence

* NLP directly contributes to accurate fake news classification

# Conclusion

Week 11 strengthened the understanding of text preprocessing, feature extraction, and deep learning for NLP. By applying both traditional and deep learning-based NLP techniques, the Fake News Detection system achieved high accuracy and demonstrated the effectiveness of NLP in solving real-world text classification problems.
