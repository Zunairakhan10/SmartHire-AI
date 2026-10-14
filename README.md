# SmartHire AI — Resume Matcher

SmartHire AI is an NLP-powered application that compares resume text with a job description using TF-IDF and cosine similarity. It highlights overlapping keywords, potential keyword gaps, and basic resume-improvement suggestions.

**Program:** IBM SkillsBuild AI & ML Internship — Final Project Prototype  
**Theme:** UN SDG 8 — Decent Work and Economic Growth

## Features

- Resume and job-description text comparison
- Text similarity score
- Matching keyword identification
- Potential missing-keyword analysis
- Basic resume improvement suggestions
- Downloadable text summary
- Streamlit web interface

## Technology Stack

- Python
- Streamlit
- Scikit-learn
- TF-IDF vectorization
- Cosine similarity

## Project Structure

```text
SmartHire-AI/
├── app.py
├── requirements.txt
└── README.md
```

## Run Locally

1. Install Python 3.10 or later.
2. Clone your repository and open the project folder in VS Code.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL shown in the terminal.

On some Windows systems, use `py` instead of `python`.

## How It Works

1. The user pastes resume text and a target job description.
2. TF-IDF converts both texts into weighted numerical vectors.
3. Cosine similarity estimates their textual similarity.
4. Basic token comparison identifies shared terms and terms present in the job description but not the resume.
5. The application displays the results and suggestions.

## Limitations and Responsible Use

This is an educational NLP prototype, not a trained hiring prediction model. The similarity score is not model accuracy, candidate quality, or probability of being hired. Keyword comparison can miss synonyms and context. Do not use this tool as the sole basis for recruitment decisions, and do not add skills that are not true. Avoid entering sensitive personal information in a public demo.

## SDG Alignment

The project explores ways to help job seekers understand job requirements and present their qualifications more effectively, aligning with the broader goals of **SDG 8: Decent Work and Economic Growth**.

## Project Information

- **Developer:** YOUR NAME
- **Institution:** YOUR UNIVERSITY
- **Program:** IBM SkillsBuild AI & ML Internship
- **Repository:** YOUR REPOSITORY URL
- **Live Demo:** Add only after successful deployment

## Disclaimer

SmartHire AI is intended for educational and demonstration purposes. Its output is informational and does not guarantee employment.
