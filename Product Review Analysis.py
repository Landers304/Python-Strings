#Task 1:


reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

# Highlight keywords in a review
def highlight_keywords(review):
    for word in review.split():
        if word.lower() in keywords:
            review = review.replace(word, word.upper())
    return review

for review in reviews:
    highlighted_review = highlight_keywords(review)
    print(highlighted_review)




#Task 2:


def sentiment_tally(review):
    # Lists of positive and negative words
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
    # Counter for positive and negative words
    positive_count = 0
    negative_count = 0
    
    for word in review.split():
        # Check if the word is in the positive words list
        if word.lower() in positive_words:
            positive_count += 1
        # Check if the word is in the negative words list
        elif word.lower() in negative_words:
            negative_count += 1
    
    #Return of postive and negative 
    return positive_count, negative_count

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for idx, review in enumerate(reviews, start=1):
    positive_count, negative_count = sentiment_tally(review)
    print(f"Review {idx}: Positive words: {positive_count}, Negative words: {negative_count}")




#Task 3: 


def create_summary(review):
    if len(review) <= 30:
        return review
    else:
        last_space_index = review[:30].rfind(' ')
        if last_space_index != -1:
            return review[:last_space_index] + "..."
        else:
            return review[:30] + "..."

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for idx, review in enumerate(reviews, start=1):
    summary = create_summary(review)
    print(f"Review {idx} Summary:", summary)
