import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load the SpaCy English model
nlp = spacy.load('en_core_web_sm')

# Define custom stopwords
custom_words = ['a','about','abstract','academy','accelerator','achievement','advanced','again','al','all',
'almost','also','although','always','among','an','and','another','any','appendix','are','article',
'as','at','author','award','background','be','beamline','because','been','before','being','between',
'bind','both','but','by','can','career','case','citation','conclusion','could','did','do','does',
'domain','done','due','during','each','early','either','elsevier','enough','especially','et','etc',
'facility','fellow','find','for','found','from','further','given','goal','group','had','has','have',
'having','here','how','however','i','if','ii','iii','in','international','into','introduction',
'is','it','its','itself','iv','just','kg','km','light','made','mainly','make','material','materials',
'may','medal','method','methods','mg','might','ml','mm','model','most','mostly','must','nature','nearly',
'neither','no','nor','not','objective','obtained','of','often','on','or','our','overall','particle',
'perhaps','pmid','presentation','prize','propose','publication','quite','rather','really','reference',
'regarding','research','result','results','science','scientist','section','seem','seen','several',
'should','show','significantly','since','site','so','society','some','source','springer','state',
'student','study','study ','such','symposium','than','that','the','their','then','there','therefore',
'these','they','this','those','through','thus','to','toward','two','upon','use','used','user','using',
'v','various','very','vi','vii','viii','was','we','were','what','whatever','when','whether','which',
'while','with','within','without','would']

# Update SpaCy's stopwords with custom stopwords
STOP_WORDS.update(custom_words)

def lemmatize_text_spacy(text):
    """
    Lemmatizes the text using SpaCy.
    """
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc]
    return ' '.join(lemmatized_tokens)

def remove_stopwords_spacy(text):
    """
    Removes stopwords from the text using SpaCy's stopword list.
    """
    doc = nlp(text)
    filtered_tokens = [token.text for token in doc if token.text.lower() not in STOP_WORDS]
    return ' '.join(filtered_tokens)

def clean_text_ext_spacy_old(text):
    """
    Cleans the text by lemmatizing and removing stopword tokens using SpaCy.
    """
    text = lemmatize_text_spacy(text)
    text = remove_stopwords_spacy(text)
    return text

def clean_text_ext_spacy(text):
    """
    Cleans the text by removing stopwords, special characters, and lemmatizing using SpaCy.
    """
    # Process text with SpaCy
    doc = nlp(text)
    
    # Filter tokens: keep only alphabetic, non-stopword tokens
    clean_tokens = [
        token.lemma_ for token in doc
        if token.is_alpha and not token.is_stop
    ]
    
    # Return the cleaned text as a string
    return ' '.join(clean_tokens)   
