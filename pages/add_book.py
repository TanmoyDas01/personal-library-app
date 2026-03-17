import streamlit as st
from utils.sheets import load_books, connect_sheet


def format_title(text):
    return text.strip().title()


st.title("➕ Add a Book")

df = load_books()

book = st.text_input("Book Name")
author = st.text_input("Author")


if st.button("Add Book"):

    if book == "" or author == "":
        st.warning("Please fill both fields")

    else:

        book = format_title(book)
        author = format_title(author)

        match = df[
            (df["Book Name"].str.lower() == book.lower()) &
            (df["Author"].str.lower() == author.lower())
        ]

        if len(match) > 0:

            st.error("This book already exists")

        else:

            sheet = connect_sheet()

            sheet.append_row([book, author, ""])

            st.success("Book added successfully!")