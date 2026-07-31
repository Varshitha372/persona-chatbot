try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None


def extract_resume_text(uploaded_file):
    """
    Extract text from uploaded PDF resume.
    """
    if PdfReader is None:
        return "Resume parsing is temporarily disabled because the pypdf package is not installed."

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text