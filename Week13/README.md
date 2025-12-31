# Week 13 – Model Deployment
**Project: Fake News Detection**

This week focuses on deploying the trained Fake News Detection model as a web API so that it can be used outside the notebook environment.

# **Objective**

* Convert the trained ML model into a reusable service
* Deploy the model using Flask
* Accept text input and return predictions in JSON format
* Build an end-to-end pipeline from input → model → output

# Model Used

* TF-IDF Vectorizer
* Trained Fake News Classification Model

# Deployment Tools

* Backend Framework: Flask
* Platform: Localhost (Windows PC)

**Model Files:**
* fake_news_model.pkl
* tfidf_vectorizer.pkl

# End-to-End Pipeline

User Text → API → Vectorizer → Model → Prediction → JSON

**API Example**

**Input (JSON):**
{ "text": "Breaking news: Scientists confirm alien life" }

**Input (JSON):**
{ "prediction": "Fake News" }

# Learning Outcome

* Learned how to deploy ML models using Flask
* Understood how APIs handle requests and responses
* Gained experience in serving predictions via JSON
* Completed end-to-end pipeline from training to deployment

# Conclusion

This week completes the Fake News Detection project by successfully deploying the trained model as a Flask API. The project now supports real-time predictions through a simple and reusable interface, demonstrating practical, real-world application of machine learning.
