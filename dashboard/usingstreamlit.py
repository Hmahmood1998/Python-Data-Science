import streamlit as st

st.title("Cristiano Ronaldo")
st.text("Cristiano Ronaldo dos Santos Aveiro ")
st.button("Click me")

sidebar=st.sidebar

sidebar.title("Main page")

st.image('ronaldo-portugal.jpg', use_column_width=True)
st.text('''*Ronaldo with Portugal at the 2018 World Cup*''')
st.header("About")
st.write('''Cristiano Ronaldo dos Santos Aveiro born in 5 February 1985.He is a Portuguese professional footballer
who plays as a forward for Premier League club Manchester United and captains the Portugal national team.
Often considered the best player in the world and widely regarded as one of the greatest players of all time.

Born and raised in Madeira, Ronaldo began his senior club career playing for Sporting CP, before signing with
Manchester United in 2003,at aged 18, winning the FA Cup in his first season. He would also go onto win three 
consecutive Premier League titles, the Champions League and the FIFA Club World Cup; at age 23, he won his first 
Ballon d'Or. Ronaldo was the subject of the then-most expensive association football transfer when he signed for 
Real Madrid in 2009 in a transfer worth €94 million (£80 million), where he won 15 trophies, including two La Liga
titles, two Copa del Rey and four Champions Leagues, and became the club's all-time top goalscorer. He also finished
runner-up for the Ballon d'Or three times, behind Lionel Messi, and won back-to-back Ballons d'Or in 2013 and 2014,
and again in 2016 and 2017. In 2018, he signed for Juventus in a transfer worth €100 million (£88 million), 
the most expensive transfer for an Italian club and the most expensive transferfor a player over 30 years old.
He won two Serie A titles, two Supercoppe Italiana and a Coppa Italia, before returning to Manchester United in 2021.

One of the world's most marketable and famous athletes, Ronaldo was ranked the world's highest-paid athlete by Forbes
in 2016 and 2017 and the world's most famous athlete by ESPN from 2016 to 2019. Time included him on their list of the
100 most influential people in the world in 2014. He is the first footballer and the third sportsman to earn 
US$1 billion in his career
''')

st.image('FC-Ar.jpg',use_column_width=True)

st.header("Career statistics")
st.subheader("Club")

st.text('I agree with terms and conditions')
st.checkbox('I agree')
st.radio('Pick one',['Cristiano Ronaldo','Lional Messi'])
st.selectbox('Pick one', ['Cristiano Ronaldo', 'Lional Messi','Neymar jr.'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.text_input('Last name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a photo')

st.color_picker('Pick a color')



username = st.text_input('Username')
password = st.text_input('Password')
st.text_input('Date of Birth')
st.selectbox('Marital Status',['Single','Married','Widowed','Divorced'])
st.button('Login')