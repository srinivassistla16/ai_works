import os
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path: str):
    """
    Loads a PDF file and returns its pages as LangChain Document objects.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
        
    print(f"Loading PDF from: {file_path}")
    # Initialize the PyPDFLoader
    loader = PyPDFLoader(file_path)
    
    # Load and optionally split the document into pages
    pages = loader.load_and_split()
    
    print(f"Successfully loaded {len(pages)} pages.")
    return pages

if __name__ == "__main__":
    # Example usage:
    pdf_path = "sample-pdf.pdf" # Replace with your PDF path
    pages = load_pdf(pdf_path)
    for i, page in enumerate(pages):
        print(f"--- Page {i+1} ---")
        print(page.page_content[:200] + "...")
    pass