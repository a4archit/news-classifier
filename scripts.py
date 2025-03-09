import pickle
import pandas as pd 

# loading files
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
category_dict = pickle.load(open('category_dict.pkl', 'rb'))
model = pickle.load(open('lor_model.pkl', 'rb'))

class NewsClassifier:

    def __init__(self):
        self.threshold_probability = 0.6
        # loadin categories
        self.category = list(category_dict.keys())

    def classify_news(self, news_headline: str) -> str:
        """
        This function takes in a string and returns the category of the news.
        """
        # text vectorization of news headline
        news_vector = vectorizer.transform(pd.Series([news_headline.lower()])).toarray().astype('bool')
        # predicting the category, predict as nunmber
        prediction = model.predict(news_vector)
        # fetching the category
        category =  self.category[prediction[0]]
        # preedicting the probabilities for each category
        precdict_probabilities = model.predict_proba(news_vector)
        # if the probability of the prediction is less than the threshold, than the category is "Others"
        if precdict_probabilities.max() < self.threshold_probability:
            category = "Others"
        return category.lower()
    

if __name__ == "__main__":
    # testing this class
    new_classifier = NewsClassifier()
    news_headline = input("Enter news headline here: ")
    print(new_classifier.classify_news(news_headline))
