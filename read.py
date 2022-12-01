import pandas as pd
import streamlit as st
# import plotly.express as px
from database import view_all_data_manager
from database import view_all_data_donor
from database import view_all_data_blood_bank


def read():
    
    with st.expander("View all manager"):
        result = view_all_data_manager()
        #st.write(result)
        df = pd.DataFrame(result)
        st.dataframe(df)
    with st.expander("View all donor"):
        result1 = view_all_data_donor()
        #st.write(result)
        df = pd.DataFrame(result1)
        st.dataframe(df)
    with st.expander("View all blood_bank"):
        result2 = view_all_data_blood_bank()
        #st.write(result)
        df = pd.DataFrame(result2)
        st.dataframe(df)
    
    
