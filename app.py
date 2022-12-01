# Importing pakages
import streamlit as st
#import mysql.connector
from create import create
# from database import create_table
from delete import delete
from read import read
from update import update
from query import query1
from donor import donor1


def main():
    st.title("Blood donation app(PES1UG20CS097_DBMS_PROJECT)")
    menu = ["About","Add", "Read", "Edit", "Remove","Query","Find Donor"]
    choice = st.sidebar.selectbox("About/Add/Read/Update/Delete/Query/DonorList", menu)

    # create_table()
    if choice =="About":
        st.image('a.png',channels="RGB",output_format="auto")
        """
        Providing information about the availability of blood from donors at the blood banks and hospitals easily to the people. This may save time as well as life.
        """
    if choice == "Add":
        create()

    if choice == "Read":
        st.subheader("Read details")
        read()

    if choice == "Edit":
        st.subheader("Update Manager details")
        update()

    if choice == "Remove":
        st.subheader("Delete Manager")
        delete()

    if choice =="Query":
         st.subheader("query and extract data from tables")
         query1()
    if choice=="Find Donor":
        st.subheader("Donor List")

        donor1()
    
    # elif choice=="Function":
    #     st.subheader("Enter type of blood")
    #     function1()

    


if __name__ == '__main__':
    main()