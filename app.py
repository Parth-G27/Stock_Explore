# WRITE YOUR STREAMLIT CODE  HERE
import streamlit as st

def main():
    #Sidebar
    user='user'
    with st.sidebar:
        #Form for Login
        with st.form(key='form1'):
            st.header(f"Welcome {user}👋")
            username=st.text_input("Username")
            password=st.text_input("Password",type='password')
            submit_button=st.form_submit_button(label='Login')
        if submit_button:
            st.success(f"Welcome to the app {username}")


    st.title("Welcome to Stock Explorer🪙")
    st.header("A DBMS Project")
    tab1,tab2=st.tabs(["Querying","About Us"])
    #Querying Tab
    with tab1:
         with st.form(key='form2'):
            st.header("Database Queries📝")
            query_input=st.text_input("Enter your database Query Here")
            submit_query=st.form_submit_button()
    #Team Details Section
    with tab2:
        st.title("Team Details🌟")
        col1,col2=st.columns(2,gap='large')
        with col1:
            st.header("Darshan N N")
            st.header("Jeswin M S")
            st.header("Parth Bidari")
            st.header("Venkatesh R")
        with col2:
            st.header("1MS21CI018")
            st.header("1MS21CI024")
            st.header("1MS21CI036")
            st.header("1MS21CI065")       

if __name__=='__main__':
    main()



