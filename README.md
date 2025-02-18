📚 **Book Recommender System**




This is a Book recommendation system built using **Streamlit** and **Collaborative Filtering**. It suggests books based on user preferences and displays the **top 50 popular books**.




🚀 **Features**
🔥 Top 50 Books: Displays the most popular books based on user interactions.


📖 Personalized Recommendations: Uses collaborative filtering to suggest similar books.

🔍 Interactive UI: Built with Streamlit for an easy-to-use interface.

📊 Data Insights: Allows users to explore the dataset used for recommendations.

🛠️ Installation
Clone the repository:

git clone https://github.com/your-repo-name.git

cd your-repo-name

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py


📂 Dataset
This project uses the Book Recommendation Dataset from Kaggle:

📌 https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

It contains:

Books.csv: Book details including title, author, and cover images.

Ratings.csv: User ratings data.

Users.csv: User demographic information.

🏗️ How It Works

The model loads precomputed similarity scores and pivot tables.
Users select a book from the dropdown menu.
The system recommends 5 similar books based on collaborative filtering.
Users can also explore the top 50 books.

📦 Files

app.py - Streamlit application for the recommender system.

Book_Recommender_Algo.ipynb - Jupyter Notebook with data processing and model building.

popular.pkl, books.pkl, pt.pkl, similarity_scores.pkl - Precomputed recommendation data.

📝 Future Enhancements
✅ Add user-based recommendations.
✅ Improve UI/UX.
✅ Enable book search functionality.


👨‍💻 Author
Developed by Sujith.
