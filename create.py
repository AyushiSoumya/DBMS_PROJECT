import streamlit as st
from database import add_data_manager
from database import add_data_donor
from database import add_data_blood_bank


def create():
    
    with st.expander("Add Manager Details:"):
     col1, col2 = st.columns(2)
     with col1:
        emp_id = st.text_input("Emp_id:")
        name = st.text_input("Name:")
     with col2:
        email = st.text_input("Email:")
        ph_no=st.text_input("Phone_No:")
     if st.button("Add Manager details"):
        add_data_manager(emp_id, name, email, ph_no)
        st.success("Successfully added Manager: {} going to {}")
    with st.expander("Add Donor Details:"):
     col1, col2 = st.columns(2)
     with col1:
        DID=st.text_input("DID:")
        name = st.text_input("name:")
        gender = st.text_input("gender:")
        DOB=st.text_input("DOB:")
        Ph_no=st.text_input("Ph_no:")
     with col2:
        state=st.text_input("state:")
        city=st.text_input("city:")
        pin=st.text_input("pin:")
        recomm_did=st.text_input("recomm_did:")
        receptionist_emp_id=st.text_input("receptionist_emp_id")

   

   
     if  st.button("Add Donor details"):
        add_data_donor(DID,name,gender,DOB,Ph_no,state,city,pin,recomm_did,receptionist_emp_id)
        st.success("Successfully added Donor: {} going to {}")
    with st.expander("Add Blood_bank Details:"):
     col1, col2 = st.columns(2)
     with col1:
        B_No = st.text_input("B_No:")
        services = st.text_input("services:")
     with col2:
        timings = st.text_input("timings:")
        MGR_emp_id=st.text_input("MGR_emp_id:")
     if st.button("Add Blood_bank details"):
        add_data_blood_bank(B_No,services,timings,MGR_emp_id)
        st.success("Successfully added blood_bank: {} going to {}")