import streamlit as st
# import pyperclip
from scripts import NewsClassifier


# creating an instance of News Classifier
model = NewsClassifier()


# creating UI
st.set_page_config(
    page_title = "News Classifier",
    page_icon = "📰"
)

# ------------------ Sidebar -------------------------- #

st.sidebar.title("About the developer")
st.sidebar.divider()
st.sidebar.write("I am creating this web application with \
**Streamlit** and build an **Classifier Machine Learning Model**.\
with **Text Vectorization** technique. ")
# st.sidebar.button(
#     "Copy src code url",
#     on_click=pyperclip.copy("https://www.github.com/a4archit/news-classifier")
# )

st.sidebar.write("You can check my social media accounts: ")
st.sidebar.write("[Kaggle](https://www.kaggle.com/architty108)")
st.sidebar.write("[Github](https://www.github.com/a4archit)")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/archit-tyagi-191323296)")

# title
st.title("News Classifier") 
# short description
short_description = """
**News Classifier** is a web application that classifies the news headline into different categories.
The categories are:
- Business
- Entertainment
- Politics
- Sports
- Travel
- Style & Beauty
- Others
"""





st.markdown(short_description)

st.divider()
sub_col1, sub_col2 = st.columns([1, 1])
with sub_col1:
    # news headline input
    news_headline = st.text_input(
        "Get category of your news headline now!",
        key = "news_headline_key",
        placeholder = "Enter news headline here",
    )

    # button 
    classify_btn = st.button(
        "Classify",
        key = "classify_btn_key",
        use_container_width=True
    )

with sub_col2:
    # reserve space for the output
    output_space = st.empty()

    # if `classify` button clicked
    if st.session_state.classify_btn_key == True:
        news_category = model.classify_news(news_headline)
        output_space.info(f"**Category:** {news_category.capitalize()}")


