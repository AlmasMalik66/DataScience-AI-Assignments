from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load saved ML model and TF-IDF vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

@app.route("/", methods=["GET"])
def home():
    return "Fake News Detection API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]

    # Convert text to vector
    text_vector = vectorizer.transform([text])

    # Make prediction
    prediction = model.predict(text_vector)[0]

    # Map prediction to text
    result = "Fake News" if prediction == 1 else "Real News"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)