import pandas
import streamlit
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
selfruits=streamlit.multiselect("pick fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])
showfruits=my_fruit_list.loc[selfruits]
streamlit.dataframe(showfruits)
                              
