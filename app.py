from textblob import TextBlob
import streamlit as st

st.title("POSITIVE or NEGATIVE SENTENCE")
label=st.subheader("SENTENCE")

area=st.text_area(" ", value="", height=200, max_chars=None, key=None, help=None,placeholder="Hi Welcome Please Enter the Sentence....")


blob=TextBlob(area)
if st.button("Predict"):
    if len(area)>20:
        if blob.sentiment.polarity >0:
            # st.write(area)
            st.subheader("Positive Sentence")
        else:
            st.subheader("Negative Sentence")
    else:
        st.subheader("Enter  Max 5 words")
