import streamlit as st
import db as db 
import pandas as pd

def get_connection(str):
    return str

def get_all_periods_btc_up():
    items = db.get_all_btc_up()
    # periods_item = [item["name"] for item in items]
    periods = [item for item in items]
    return periods

def get_all_periods_btc_low():
    items = db.get_all_btc_low()
    # periods_item = [item["name"] for item in items]
    periods = [item for item in items]
    return periods

def get_all_periods_tsla_up():
    items = db.get_all_tsla_up()
    # periods_item = [item["name"] for item in items]
    periods = [item for item in items]
    return periods

def get_all_periods_tsla_low():
    items = db.get_all_tsla_low()
    # periods_item = [item["name"] for item in items]
    periods = [item for item in items]
    return periods

def get_all_periods_sen(nam):
    items = db.get_all_sen(nam)
    # periods_item = [item["name"] for item in items]
    periods = [item for item in items]
    return periods

def get_all_periods_eth_up():
    items = db.get_all_eth_up()
    # periods_item = [item["name"] for item in items]
    periods = [item for item in items]
    return periods

def get_all_periods_eth_low():
    items = db.get_all_eth_low()
    # periods_item = [item["name"] for item in items]
    periods = [item for item in items]
    return periods

def get_all_periods_btc_time(start_t,end_t):
    items = db.get_all_btc_time(start_t,end_t)
    periods = [item for item in items]
    return periods
    
def get_all_periods_tsla_time(start_t,end_t):
    items = db.get_all_tsla_time(start_t,end_t)
    periods = [item for item in items]
    return periods

def get_all_periods_eth_time(start_t,end_t):
    items = db.get_all_eth_time(start_t,end_t)
    periods = [item for item in items]
    return periods

#MATIC 
def get_all_periods_matic_up():
    items = db.get_all_matic_up()
    periods = [item for item in items]
    return periods

def get_all_periods_matic_low():
    items = db.get_all_matic_low()
    periods = [item for item in items]
    return periods

def get_all_periods_matic_time(start_t,end_t):
    items = db.get_all_matic_time(start_t,end_t)
    periods = [item for item in items]
    return periods


def main():
    #Sidebar
    user='Parth Bidari'
    with st.sidebar:
        #Form for Login
        with st.form(key='form1'):
            st.header(f"Welcome 👋")
            con_str=st.text_input("Enter the MongoDB connection String")
            # password=st.text_input("Password",type='password')
            submit_button=st.form_submit_button(label='Login')
        if submit_button:
            st.success(f"Welcome to the app {user}")
            # get_connection(con_str)
            


    st.title("Welcome to Stock Explorer 🚀")
    st.header("A Stock Analysis Project")
    tab1,tab2=st.tabs(["Querying","About Us"])
    #Querying Tab
    with tab1:
         with st.form(key='form2'):
            st.header("Database Queries📝")
            query_input=st.text_input("Enter (BTC or ETH or TSLA or MATIC or sen)")
            start_time=st.text_input("Start time (YYYY-MM-DD)")
            end_time=st.text_input("end time (YYYY-MM-DD)")
            submit_query=st.form_submit_button()
            
            #     st.table(get_all_periods_tsla())
            # st.write(query_input+"Top 5 records")
            if query_input=='BTC':
                st.write('Bitcoin (BTC) Top 5 records')
                st.table(get_all_periods_btc_up())
                st.write('Bitcoin (BTC) Last 5 records')
                st.table(get_all_periods_btc_low())
                st.write('Sentimental analysis on Bitcoin (BTC)')
                st.table(get_all_periods_sen(query_input))
                st.write('Bitcoin (BTC) in the given time bracket')
                st.table(get_all_periods_btc_time(start_time,end_time))
                
            elif query_input=='TSLA':
                st.write('Tesla Inc. (TSLA) Top 5 records')
                st.table(get_all_periods_tsla_up())
                st.write('Tesla Inc. (TSLA) Last 5 records')
                st.table(get_all_periods_tsla_low())
                st.write('Sentimental analysis on Tesla Inc. (TSLA)')
                st.table(get_all_periods_sen(query_input))
                st.write('Tesla Inc. (TSLA) in the given time bracket')
                st.table(get_all_periods_tsla_time(start_time,end_time))
                
            elif query_input=='ETH':
                st.write('Ethereum (ETH) Top 5 records')
                st.table(get_all_periods_eth_up())
                st.write('Ethereum (ETH) Last 5 records')
                st.table(get_all_periods_eth_low())
                st.write('Ethereum (ETH) in the given time bracket')
                st.table(get_all_periods_eth_time(start_time,end_time))
            
            elif query_input=='sen':
                st.write("Sentimental analysis on BTC & TSLA")
                st.table(get_all_periods_sen(query_input))
                
            elif query_input=='MATIC':
                st.write('Polygon (MATIC) Top 5 records')
                st.table(get_all_periods_matic_up())
                st.write('Polygon (MATIC) Last 5 records')
                st.table(get_all_periods_matic_low())
                st.write('Polygon (MATIC) in the given time bracket')
                st.table(get_all_periods_matic_time(start_time,end_time))
                
                
            
            #st.write(get_all_periods_btc())
            
            
            
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