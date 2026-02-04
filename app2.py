import streamlit as st

st.title("my age and city app")

age = st.number_input("enter your age" , 1 ,100)
city = st.selectbox("select your city" , ["mumbai" , "los angeles" , "chicago" , "houston" , "phoenix"])

if st.button("show details"):
    st.write("your age is" , age)
    st.write("your city is" , city)