import datetime

import pandas as pd
import streamlit as st
from database import view_all_data_manager, edit_dealer_data


def update():
    result = view_all_data_manager()
    # st.write(result)
    df = pd.DataFrame(result, columns=['emp_id', 'name', 'email', 'ph_no'])
    with st.expander("Current Data"):
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            up_manager_id = st.text_input("Email_id:")
            
        with col2:
            new_email = st.text_input("email")

        if st.button("Update email"):
            edit_dealer_data(up_manager_id,new_email)

            st.success("Successfully updated")

    result2 = view_all_data_manager()
    df2 = pd.DataFrame(result2, columns=['emp_id', 'name', 'email', 'ph_no'])
    with st.expander("Updated data"):
        st.dataframe(df2)