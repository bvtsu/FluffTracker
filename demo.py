import streamlit as st
import pandas as pd
import altair as alt
import requests

url = "https://api.mangadex.org/v2/"
id_num = "4290"
user_auth = ("ProjectFluff", "fluff4thesoul")
req = requests.get(url + "/manga/" + id_num, auth=user_auth)


try:
    df_md = pd.DataFrame.from_dict(req.json())
    #st.write("### Random MangaDex Entry", data_md.sort_index())
    data_md = df_md.T.reset_index()
    #data_md = pd.melt(data_md, id_vars=["index"])
    st.write("### Random MangaDex Entry", data_md.sort_index())
    
except:
    print("Error")