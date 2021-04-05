from rake_nltk import Rake
rake_nltk_var = Rake()

#RAKE stands for Rapid Automatic Keyword Extraction. 
#It is only built to extract keywords by using the NLTK library in Python. 
#Now let’s see how to use this library for extracting keywords.

#Now I will store some text into a variable:

text = """ I am a smart programmer from prague, and I am here to guide you
with Data Science, Machine Learning, and Python for free.
I hope you will learn a lot in your journey towards Coding,
Machine Learning and Artificial Intelligence with me."""


#Now let’s extract the keywords from the text and print the output:

rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)


