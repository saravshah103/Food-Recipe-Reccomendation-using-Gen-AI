import ollama
import streamlit as st


st.title("Food Recipe Recommender App")

ingredients = st.text_input("Ingredients")
food_type  = st.text_input("Type")
cuisine = st.text_input("Cuisine")

if st.button("Generate"):
    with st.spinner("Generating suggestions..."):
   
        response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": f"Suggest me some {food_type} recipes of {cuisine} cuisine that I can make  with {ingredients}",
            },
        ],
    )
        st.write(response["message"]["content"])