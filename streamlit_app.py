from streamlit_option_menu import option_menu
import pandas as pd

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Product", ["BFR CORPORATE", 'BFR mikro', 'BFR Consumer', 'BRF'], 
        icons=['play', 'play'], menu_icon="cast", default_index=1)
    selected
    print(selected)
df = pd.read_excel("adult.csv")
st.dataframe(df)
