# Book Recommender System 📚

A web-based book recommendation system that suggests similar books based on user input and displays popular books. The system uses collaborative filtering and content-based filtering to provide personalized book recommendations.

## Features ✨

- **Popular Books Display**: Shows top 50 books with ratings and number of votes
- **Book Search**: Search for any book in the database
- **Similar Book Recommendations**: Get personalized book recommendations based on your input
- **Partial Match Support**: Find books even with partial name matches
- **Interactive UI**: Modern, responsive design with easy-to-use interface
- **Rating System**: Shows normalized ratings out of 5 stars

## Tech Stack 🛠️

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Flask
- **Data Processing**: NumPy, Pandas
- **Machine Learning**: Scikit-learn
- **Database**: Pickle files (pre-processed data)

## Installation 🚀

1. Clone the repository
```bash
git clone <repository-url>
cd book-recommender-system
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

5. Open your browser and go to `http://localhost:5000`

## Project Structure 📁

```
book-recommender-system/
├── app.py                  # Main Flask application
├── templates/             
│   ├── index.html         # Home page template
│   └── recommend.html     # Recommendation page template
├── static/                # Static files (if any)
├── *.pkl                  # Preprocessed data files
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Data Files 📊

The system requires the following pickle files:
- `popular.pkl`: Contains popular books data
- `pt.pkl`: Pivot table for user-book interactions
- `books.pkl`: Complete books dataset
- `similarity_scores.pkl`: Matrix of similarity scores

## Features in Detail 🔍

### Home Page
- Displays top 50 popular books
- Shows book cover, title, author
- Displays number of ratings and average rating
- Quick access to recommendation system

### Recommendation System
- Search for any book in the database
- Supports partial name matching
- Shows multiple matches if found
- Provides similar book recommendations
- Displays book details with cover images

## Contributing 🤝

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Book dataset from Goodreads
- Built with Flask and Bootstrap
- Inspired by various recommendation systems 