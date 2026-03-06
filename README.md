This Python script scrapes book data from the website Books to Scrape
 and outputs a cleaned CSV file. It collects book titles, genres, prices, ratings, and the page number where each book appears.

 Features:
 1. Scrapes all 50 books from Books to Scrape.
 2. Extracts the following information from each book:
    - Title
    - Genre
    - Price
    - Rating
    - Page Number
3. Handles duplicates and cleans book titles.
4. Saves the final dataset as Book.csv

Libraries:
1. Requests
2. Beautifulsoup4
3. Pandas

Note:
I chose the Book to Scrape website because anyone can legally scrape the books there.
