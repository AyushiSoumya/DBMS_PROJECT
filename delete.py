import pandas as pd
import streamlit as st
from database import view_all_data_manager, delete_data


def delete():
    result = view_all_data_manager()
    df = pd.DataFrame(result,columns=['emp_id', 'name', 'email', 'ph_no'])
    with st.expander("Current data"):
        st.dataframe(df)

    selected_manager=st.text_input("emp_id")

    st.warning("Do you want to delete ::{}".format(selected_manager))
    if st.button("Delete Manager"):
        delete_data(selected_manager)
        st.success("manager has been deleted successfully")
    new_result = view_all_data_manager()
    df2 = pd.DataFrame(new_result, columns=['emp_id', 'name', 'email', 'ph_no'])
    with st.expander("Updated data"):
        st.dataframe(df2)