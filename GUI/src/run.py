import streamlit as st

from src.PasswordGenerator import PinGenerator , RandomPasswordGenerator , MemorablePassword

 
st.image('img/image.png', width=500)
st.title('Password Generator')


option = st.radio("Choose the type of password you want to generate:",
                  ("PIN password","Random password","Memorable password"))


if option == 'PIN password':
    length = st.slider("Select the length of the pin code: ",4,32)
    generator = PinGenerator(length)
elif option == 'Random password':
    length = st.slider("select the length of the password: ",4,100)
    include_number = st.toggle("Include Number")
    include_symbol = st.toggle("Include Symbol")
    generator = RandomPasswordGenerator(length,include_number,include_symbol)

elif option == "Memorable password":
    length = st.slider("select the length of the password: ",4,100)
    seperator = st.text_input("-")
    capitalize = st.toggle("Capitalize")
    generator = MemorablePassword(length,seperator,capitalize)
    
    
password = generator.generator()
st.write(f"Your {option} is : {password}")