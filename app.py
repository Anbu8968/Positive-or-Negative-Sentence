from textblob import TextBlob
import streamlit as st

st.title("FEEDBACK CLASSIFIER")
# label=st.subheader("Feedback")

area=st.text_area(" ", value="", height=200, max_chars=None, key=None, help=None,placeholder="Hi Welcome Please Enter the Sentence....")


blob=TextBlob(area)
if st.button("Predict"):
    if len(area)>20:
        if blob.sentiment.polarity >0:
            # st.write(area)
            st.subheader("Positive Feedback")
        else:
            st.subheader("Negative Feedback")
    else:
        st.subheader("Enter  Max 5 words")
hide="""
<style>
#MaimMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}
</style>
"""
st.markdown(hide,unsafe_allow_html=True)
