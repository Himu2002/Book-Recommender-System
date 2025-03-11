from flask import Flask,render_template,request
import pickle
import numpy as np

# Load pre-trained models and data
popular_df = pickle.load(open('popular.pkl','rb'))    # DataFrame containing popular books
pt = pickle.load(open('pt.pkl','rb'))                # Pivot table for user-book interactions
books = pickle.load(open('books.pkl','rb'))          # Complete books dataset
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))  # Matrix of similarity scores between books

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """
    Home page route that displays top 50 popular books.
    Returns:
        Rendered template with book details including:
        - Book titles
        - Author names
        - Book cover images
        - Number of ratings
        - Average rating (normalized to 5-point scale)
    """
    # Normalize ratings to be out of 5
    max_rating = popular_df['avg_rating'].max()
    normalized_ratings = [(x/max_rating) * 5 for x in popular_df['avg_rating'].values]
    
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=[int(round(x)) for x in normalized_ratings]
                           )

@app.route('/recommend')
def recommend_ui():
    """
    Route to display the book recommendation search page.
    Returns:
        Rendered template with search form.
    """
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    """
    Route to handle book recommendation requests.
    Process:
    1. Get user input and validate
    2. Search for matching books
    3. If multiple matches found, show options to user
    4. If single match found, generate recommendations
    5. Return appropriate template with results
    
    Returns:
        Rendered template with either:
        - Error message
        - List of matching books
        - List of recommended books
    """
    # Get and clean user input
    user_input = request.form.get('user_input').strip()
    
    # Validate input
    if not user_input:
        return render_template('recommend.html', 
                             error=True,
                             message="Please enter a book name.")
    
    # Find books that contain the user input (case-insensitive)
    matching_books = [book for book in pt.index 
                     if user_input.lower() in book.lower()]
    
    # Handle no matches found
    if not matching_books:
        return render_template('recommend.html', 
                             error=True,
                             message="No books found matching your search. Please try another name.")
    
    # Process exact match
    if len(matching_books) == 1:
        book_to_use = matching_books[0]
    else:
        # Handle multiple matches - show options to user
        book_data = []
        for book_name in matching_books[:5]:  # Limit to 5 matches for better UX
            temp_df = books[books['Book-Title'] == book_name]
            if not temp_df.empty:
                item = [
                    book_name,
                    list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values)[0],
                    list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values)[0]
                ]
                book_data.append(item)
        
        return render_template('recommend.html', 
                             matching_books=book_data,
                             search_term=user_input,
                             show_matches=True)
    
    # Generate recommendations for the selected book
    # 1. Find the book's index in our pivot table
    index = np.where(pt.index == book_to_use)[0][0]
    # 2. Get similar items based on similarity scores
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    # 3. Collect recommended book details
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    # Return recommendations
    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)