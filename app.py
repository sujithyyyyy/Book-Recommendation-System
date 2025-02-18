# import the librareis 
import streamlit as st 
import pickle 
import numpy as np 
import pandas as pd 

st.set_page_config(layout="wide")

st.header("Book Recommender System")

st.markdown('''
            ##### The site usinging colaborative filtering suggests books from our catalog. 
            ##### We recommend top 50 books for every one as well. 
            ''')
#import our models

popular=pickle.load(open("popular.pkl","rb"))
books=pickle.load(open("books.pkl","rb"))
pt=pickle.load(open("pt.pkl","rb"))
similarity_scores=pickle.load(open("similarity_scores.pkl","rb"))


#top 50 books

st.sidebar.title("Top 50 books")

if st.sidebar.button("SHOW"):
    columns_per_row=5
    nums_rows=10
    for row in range(nums_rows):
        columns=st.columns(columns_per_row)
        for cols in range(columns_per_row):
            book_index=row*columns_per_row+cols
            if book_index<len(popular):
                with columns[cols]:
                    st.image(popular.iloc[book_index]["Image-URL-M"]) #Displays the image
                    st.text(popular.iloc[book_index]["Book-Title"]) #displays book title               
                    st.text(popular.iloc[book_index]["Book-Author"]) #displays book Author               


#function to recommend books

def recommend(book_name):
  index=np.where(pt.index==book_name)[0][0]
  similar_items=sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
  # lets create a empty list & in that list I want to Populate with the book
# information. I want Book author,Book title,Image URl. %%
#Empty list
  data=[]
  for i in similar_items:
    item=[]
    temp_df=books[books['Book-Title']==pt.index[i[0]]]
    item.extend(list(temp_df.drop_duplicates('Book-Title')["Book-Title"].values))
    item.extend(list(temp_df.drop_duplicates('Book-Title')["Book-Author"].values))
    item.extend(list(temp_df.drop_duplicates('Book-Title')["Image-URL-M"].values))
    data.append(item)
  return data


#displays list of books
book_list=pt.index.values



#similar book suggestion

st.sidebar.title("Similar Book Suggestion ")
#Dropdown to select the Books
selected_box=st.sidebar.selectbox("Select a book from dropdown",book_list)

#if button is triggered
if st.sidebar.button("Recommend Me"):
    book_recommend=recommend(selected_box)
    cols=st.columns(5)
    
    for col_idx in range(5):
        with cols[col_idx]:
            if col_idx<len(book_recommend):
                st.image(book_recommend[col_idx][2])

                st.text(book_recommend[col_idx][0])

                st.text(book_recommend[col_idx][1])


#import data 
#import data
books=pd.read_csv("C:/Users/Sujith/Downloads/Books.csv") #Book data
ratings=pd.read_csv("C:/Users/Sujith/Downloads/Ratings.csv") # User's ratings data
users=pd.read_csv("C:/Users/Sujith/Downloads/Users.csv")#Users's location and age data


st.sidebar.title("Data Used")


if st.sidebar.button("Show Data Used"):
    st.subheader("This is the books data we used in our model")
    st.dataframe(books)
    st.subheader("This is the user ratings data we used in our model")
    st.dataframe(ratings)
    st.subheader("This is the user data we used in our model")
    st.dataframe(users)










