import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My brand new super app")
st.write("Let's start building Stuff! For help and inspiration, head over to nothing")

st.divider()

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)
