# SmartHire AI — Resume Matcher

SmartHire AI is an NLP-powered application that compares resumes with job descriptions using TF-IDF and cosine similarity. It identifies matching keywords, highlights potential skill gaps, and provides basic resume improvement suggestions.

**Internship:** IBM SkillsBuild AI & ML Internship  
**Theme:** SDG 8 — Decent Work and Economic Growth

## Features

- Resume and job description matching
- Text similarity score
- Matching keyword identification
- Missing keyword analysis
- Resume improvement suggestions
- Interactive web interface using Streamlit

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## Project Structure

```text
SmartHire-AI/
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
cd SmartHire-AI
```

**2. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**3. Run the application**

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## How It Works

1. Enter your resume text.
2. Paste the target job description.
3. The application converts the text into numerical features using TF-IDF.
4. Cosine similarity estimates the textual similarity between the resume and job description.
5. Review matching keywords, potential keyword gaps, and improvement suggestions.

## Methodology

- **TF-IDF:** Assigns weights to words based on their importance within the text.
- **Cosine Similarity:** Measures the similarity between numerical text vectors.
- **Keyword Comparison:** Identifies overlapping and missing terms using basic token matching.

## Future Enhancements

- Resume PDF and DOCX upload support
- Semantic matching using sentence embeddings
- Advanced skill extraction with NLP
- Downloadable resume analysis reports
- Improved user interface and accessibility

## Responsible Use

SmartHire AI is an educational NLP prototype. Its similarity score is not a measure of hiring probability, candidate quality, or model accuracy. Keyword matching may overlook synonyms and context. The application should not be used as the sole basis for recruitment decisions. Users should provide truthful information and avoid entering sensitive personal data into public demos.

## SDG Alignment

This project aligns with **UN Sustainable Development Goal 8: Decent Work and Economic Growth** by exploring accessible tools that help job seekers understand job requirements and improve resume relevance.




