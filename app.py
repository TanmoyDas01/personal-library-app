import streamlit as st
from utils.sheets import load_books


st.set_page_config(page_title="Personal Library")

st.title("📚 My Personal Library")

st.write("Search a book in your collection")

df = load_books()

search = st.text_input("Search for a book")


if search:

    search_lower = search.lower()

    results = df[
        df["Book Name"].str.lower().str.contains(search_lower)
    ]

    if len(results) > 0:

        st.success("Book found in library")

        st.dataframe(results)

    else:

        st.error("Book not found")