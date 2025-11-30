# **Fake News Detection using LSTM (Deep Learning)**

This project builds a Fake News Classification Model using Recurrent Neural Networks (RNN) with LSTM layers.
The model classifies news as Real (0) or Fake (1) based on the article title + text.

# **Project Features**

* Uses RNN (LSTM) — Week 10 Deep Learning requirement

* Text preprocessing: cleaning, tokenizing, padding

* Trained on merged dataset:

   * Fake.csv

   * True.csv

* Achieved 98% accuracy on test data

* End-to-end pipeline using TensorFlow/Keras

# **Assignment Task (Based on My Project Dataset)**

My project dataset is text-based fake news classification, which makes RNN/LSTM a perfect choice because the data is sequential and language-based.

Therefore, for Week 10:

* CNN was only explored conceptually (since CNNs are mainly for image data).

* RNN/LSTM was **directly applied** to my project dataset because it fits text classification.

* I performed full preprocessing: tokenization, padding, label creation, and sequence preparation.

* Implemented an **LSTM model** to classify fake vs real news.

* Achieved high **accuracy (≈98%)**, proving RNN/LSTM is suitable for this task.

# **Key Insights (Fake News Detection – Week 10)**

* CNN is great for image pattern learning — not suitable for my text-based dataset.

* RNN/LSTM is ideal for handling sequences, language, and long-term dependencies, which are essential for understanding fake vs real news articles.

* Text preprocessing (tokenization, padding, sequence modeling) is critical for deep learning NLP tasks.

* LSTM networks outperform traditional ML models when the text is long, contextual, or requires understanding of sentence structure.

* For fake news detection, embedding layers + LSTM significantly improve accuracy over simple bag-of-words methods.

* Deep learning allows the model to automatically learn semantic patterns that indicate deception or credibility.

# **Conclusion:**
In Week 10, I applied advanced deep learning to my Fake News Detection project. CNNs were only studied conceptually, but LSTM was implemented because my dataset is text-based. After cleaning, tokenizing, and padding the data, the LSTM model achieved high accuracy (~98%), showing it can effectively detect fake vs real news. This week improved my understanding of deep learning for NLP tasks.
