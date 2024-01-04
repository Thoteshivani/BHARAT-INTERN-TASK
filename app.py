import streamlit as st
import pickle 

#lets load the saved vectorizor and naive bayes 
tfidf = pickle.load(open("vectorizer.pkl","rb"))
model = pickle.load(open("model.pkl","rb"))

#saving the stremlit code
st.title("Email spam Classifier")
input_sms = st.text_area("Enter Message")

if st.button("predict"):
    #preprocess
    transformed_sms = transform_text(input_sms)
    #vectorize
    vector_input = tfidf.transform([transformed_sms])
    #predict
    result = model.predict(vector_input)[0]
    #display
    if result ==1:
        st.header("Spam")
    else:
              st.header("Not Spam")
            
           
