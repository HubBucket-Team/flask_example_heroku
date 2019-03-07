from flashtext.keyword import KeywordProcessor
import pickle

# funtion that takes in a text string & returns "NER" output
def get_keywords_api():
    # read in pickled word processor
    with open("word_processor.pkl", "rb") as file:
        keyword_processor = pickle.load(file)
    
    # get our keywords 
    def keywords_api(post): 
        keywords_found = keyword_processor.extract_keywords(post, span_info=True)
        return keywords_found
