import requests
from xml.etree import ElementTree

def fetch_pubmed_data(pubmed_id):
    """
    Fetches the title and abstract of a PubMed article using its PubMed ID.

    Uses the E-Utilities API provided by NCBI to fetch the data - specifically the efetch endpoint.
    Documented here: https://www.ncbi.nlm.nih.gov/books/NBK25499/#_chapter4_EFetch_
    Note that this function doesn't include the email or API key parameters, which are required for high-volume usage.
    
    This function is limited to fetching data for a single article at a time.

    Args:
        pubmed_id (str): The PubMed ID of the article to fetch.
    Returns:
        tuple: A tuple containing the title and abstract of the article.
    Raises:
        Exception: If there is an error fetching data from PubMed.
    """
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={str(pubmed_id)}&retmode=xml&tool=topic_modeling_project&retmax=1"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error fetching data from PubMed: {response.status_code}")

    # Parse the XML response
    root = ElementTree.fromstring(response.content)

    # Extract the PMID, title and abstract
    pmid = root.find(".//PMID").text
    title = root.find(".//ArticleTitle").text
    abstract = root.find(".//AbstractText").text

    return pmid, title, abstract