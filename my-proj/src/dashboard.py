import streamlit as st
from my_password_utils import PasswordGenerator, PinGenerator, RandomPasswordGenerator, MemorablePasswordGenerator


st.image("/home/amirhossein/Desktop/my-proj/images/download.png" ,width=130)
st.title("Password Generator 👾")
option = st.radio("Select Password Type:", ("PIN", "Random Password", "Memorable Password"))
if option == "PIN":
    length = st.slider("Select PIN Length:", 6,12)
    generator = PinGenerator(length)

elif option == "Random Password":
    length = st.slider("Select Password Length:", 8, 24)
    include_numbers = st.checkbox("Include Numbers", value=True)
    include_symbols = st.checkbox("Include Symbols", value=False)
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)

else:
    num_of_words = st.slider("Number of Words:", 2, 6)
    separator = st.text_input("Separator:", "-")
    capitalize = st.checkbox("Capitalize Words", value=False)
    generator = MemorablePasswordGenerator(num_of_words, separator, capitalize)


password = generator.generate()
st.write(f"Generated Password: **`{password}`**")
