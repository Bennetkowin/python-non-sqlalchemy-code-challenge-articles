#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article, Author, Magazine

if __name__ == '__main__':
    print("HELLO! :) Let's debug :vibing_potato:")

    # Sample data
    author1 = Author("Carry Bradshaw")
    author2 = Author("Nathaniel Hawthorne")

    magazine1 = Magazine("Vogue", "Fashion")
    magazine2 = Magazine("AD", "Architecture & Design")

    article1 = Article(author1, magazine1, "How to wear a tutu with style")
    article2 = Article(author1, magazine2, "Dating life in NYC")
    article3 = Article(author2, magazine1, "The power of minimalist design")

    # Check data relationships
    print("All Articles:", Article.all)
    print("Author1 Articles:", author1.articles())
    print("Magazine1 Contributors:", magazine1.contributors())

    # Debugging session
    ipdb.set_trace()
