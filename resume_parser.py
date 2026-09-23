try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None


def extract_resume_text(uploaded_file):
    """
    Extract text from the uploaded PDF.
    """

    if PdfReader is None:
        return ""

    try:
        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception:
        return ""


def is_resume(text):
    """
    Validate whether the uploaded PDF looks like a resume.

    Required:
    - Contact information
    - Education
    - Skills
    - Experience OR Projects
    """

    if not text:
        return False

    text_lower = text.lower()

    # -----------------------------
    # 1. Contact Information
    # -----------------------------

    has_email = "@" in text_lower

    phone_digits = sum(
        character.isdigit()
        for character in text
    )

    has_phone = phone_digits >= 10

    has_contact = has_email or has_phone


    # -----------------------------
    # 2. Education
    # -----------------------------

    education_keywords = [
        "education",
        "academic",
        "b.tech",
        "btech",
        "m.tech",
        "mtech",
        "degree",
        "bachelor",
        "master",
        "university",
        "college",
    ]

    has_education = any(
        keyword in text_lower
        for keyword in education_keywords
    )


    # -----------------------------
    # 3. Skills
    # -----------------------------

    skills_keywords = [
        "skills",
        "technical skills",
        "programming",
        "technologies",
        "tools",
    ]

    has_skills = any(
        keyword in text_lower
        for keyword in skills_keywords
    )


    # -----------------------------
    # 4. Experience / Internship
    # -----------------------------

    experience_keywords = [
        "experience",
        "work experience",
        "professional experience",
        "internship",
        "intern",
    ]

    has_experience = any(
        keyword in text_lower
        for keyword in experience_keywords
    )


    # -----------------------------
    # 5. Projects
    # -----------------------------

    project_keywords = [
        "projects",
        "project",
        "academic project",
        "personal project",
    ]

    has_projects = any(
        keyword in text_lower
        for keyword in project_keywords
    )


    # -----------------------------
    # Final Resume Validation
    # -----------------------------

    if (
        has_contact
        and has_education
        and has_skills
        and (has_experience or has_projects)
    ):
        return True

    return False