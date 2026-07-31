from pypdf import PdfReader

def extract_resume_text(uploaded_file):
    """
    Temporary function for testing deployment.
    Resume parsing is disabled.
    """
    return "Resume parsing is temporarily disabled."

def extract_resume_text(uploaded_file):
    """
    Extract text from uploaded PDF resume.
    """

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text