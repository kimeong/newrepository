import streamlit as st
view = [300,200,100,500,600]
show_raw = st.checkbox('show raw data')
st.write('raw data')
view
st.write('# table')
st.table(view)
st.write('# bar graph')
st.bar_chart(view)
