import pandas
import streamlit
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("pick fruit:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
                              
