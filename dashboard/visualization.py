import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

st.title('Titanic data Analysis')
titanic=sns.load_dataset('titanic')

st.dataframe(titanic)

figure1=px.bar(data_frame=titanic,x='survived',y='pclass',color='sex')
st.plotly_chart(figure1,use_container_width=True)

sellive=st.selectbox('Dead or Alive',[0,1])

figure2=px.pie(data_frame=titanic[titanic['survived']==sellive].groupby('class',as_index=False).count(), values='pclass', labels='class',names='class')
st.plotly_chart(figure2)
