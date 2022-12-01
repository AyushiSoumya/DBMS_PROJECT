import streamlit as st
from database import donor
import pandas as pd






def donor1():
 q=st.text_input("Enter blood type:")

 
 if st.button("Get Donor List"):
        result=donor(q);
        df2 = pd.DataFrame(result,columns=['DONOR_ID', 'name', 'ph_no'])
        st.dataframe(df2)