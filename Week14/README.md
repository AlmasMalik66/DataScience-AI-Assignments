# Week 14 – Ethics & Explainability
**Fake News Detection Project**

# Overview

This week focuses on Ethics and Explainable AI. The goal is to understand why the Fake News Detection model makes a prediction instead of treating it as a black box.

Explainability is added using **LIME (Local Interpretable Model-Agnostic Explanations).**

# **Objectives**

* Explain model predictions (why X → Y)
* Improve transparency and trust
* Add an Explainability section to the project
* Follow ethical AI principles

# **Explainability Method (LIME)**

LIME explains individual predictions by:
* Slightly modifying the input text
* Observing prediction changes
* Highlighting important words influencing the decision

This approach is model-agnostic and works well for text classification tasks.

**Example Explanation**

**Input Text:**

“Breaking news: Scientists confirm alien life on Mars”

**Model Prediction:**

Fake News

**LIME Explanation:**

* Words like “Breaking”, “confirm”, and “alien life” contributed positively toward the Fake News prediction.
* These words are commonly associated with sensational or misleading news patterns learned by the model.

# Why Explainability Matters

* Helps users understand model decisions
* Reduces black-box behavior
* Improves ethical AI usage
* Supports fairness and accountability
* Builds trust in machine learning systems

# Workflow

* Load trained Fake News model and TF-IDF vectorizer
* Provide a sample news text
* Use LIME to explain the prediction
* Identify words contributing to Fake News or Real News

# Conclusion

By integrating LIME, the Fake News Detection model now provides interpretable and ethical predictions, helping users understand why a prediction was made.This completes Week 14 – Ethics & Explainability successfully.
