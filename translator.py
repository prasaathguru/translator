import streamlit as st
from streamlit.delta_generator import DeltaGenerator as _DeltaGenerator
from altair import Chart
from deep_translator import GoogleTranslator

def translator(input,selected_option):
    t = GoogleTranslator(
        source="auto",target=(selected_option)
    )
    r = t.translate(input)
    return r

def main():
    st.header("Give translating sentence")
    input2 = st.text_input("Give translating sentence")
    selected_option = st.selectbox('Choose an option:', ['en', 'tamil', 'hindi'])
    output1 = translator(input2,selected_option)
    st.write(output1)


if __name__ == "__main__":
    main()