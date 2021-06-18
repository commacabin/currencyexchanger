import streamlit as st
from PIL import Image
import pandas as pd
import requests
class Currency_convertor:
	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()
		self.rates = data["rates"]

	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]

		amount = round(amount * self.rates[to_currency], 2)
		st.subheader('Real-Time Currency Converter: ')
		st.write('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

YOUR_ACCESS_KEY='6fd361151b32247fe1d01a28969d9dfc'
url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
c = Currency_convertor(url)

image = Image.open('logo_1.png')

st.image(image, width = 500)


st.header("Quick Fiat Exchanger")
st.sidebar.header('Input Options')

From_Country = ['USD','INR','PKR','AUD','EUR','NGN','QAR']
from_country = st.sidebar.selectbox('Select base currency for conversion', From_Country, 1)

To_Country = ['USD','INR','PKR','AUD','EUR','NGN','QAR']
to_country = st.sidebar.selectbox('Select target currency to convert in', To_Country, 1)
amount=st.sidebar.number_input('Amount ')

st.sidebar.button('Calculate',c.convert(from_country, to_country, amount))
expander_bar = st.beta_expander("About")
expander_bar.markdown("""
* **Credit:** Web Application by Arafat Ali Khan 
* **Roll No:** Fa-19/BS-DFCS/024
* **Semester:** 4th
* **Department:** Digital Forensics & Cyber Security
* **University:** Lahore Garrison University
""")