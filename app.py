import re
import streamlit as st
from sklearn.feature_extraction.text import (
    TfidfVectorizer,
    ENGLISH_STOP_WORDS,
)
from sklearn.metrics.pairwise import cosine_similarity


# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="SmartHire AI | Resume Matcher",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ---------------- CUSTOM STYLING ----------------
st.markdown(
    """
    <style>
    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        padding: 1.6rem 1.8rem;
        border-radius: 20px;
        background: linear-gradient(120deg, #101827, #233b63);
        color: white;
        margin-bottom: 1.2rem;
    }

    .hero h1 {
        font-size: 2.35rem;
        margin-bottom: 0.45rem;
    }

    .hero p {
        font-size: 1.02rem;
        color: #dbeafe;
        margin-bottom: 0;
    }

    .pill {
        display: inline-block;
        padding: 5px 10px;
        margin: 3px;
        border-radius: 999px;
        background: #e0f2fe;
        color: #075985;
        font-size: 0.85rem;
    }

    .small-muted {
        color: #64748b;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------- HEADER ----------------
st.markdown(
    """
    <div class="hero">
        <h1>🎯 SmartHire AI</h1>
        <p>
            Discover how closely your resume matches a job description
            with clear keyword insights and practical suggestions.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "IBM SkillsBuild AI & ML Internship Project Prototype "
    "| SDG 8: Decent Work and Economic Growth"
)


# ---------------- TEXT INPUTS ----------------
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📄 Your Resume")
    resume = st.text_area(
        "Resume text",
        height=270,
        placeholder=(
            "Paste your resume here...\n\n"
            "Example: Computer Science student with experience "
            "in Python, Java, SQL, Git, and machine learning projects."
        ),
        label_visibility="collapsed",
        key="resume",
    )

with col2:
    st.subheader("💼 Job Description")
    job = st.text_area(
        "Job description",
        height=270,
        placeholder=(
            "Paste the job description here...\n\n"
            "Example: Seeking a software engineering intern "
            "with Python, Java, data structures, SQL, Git, "
            "and problem-solving skills."
        ),
        label_visibility="collapsed",
        key="job",
    )


# ---------------- TEXT PROCESSING ----------------
def clean_tokens(text):
    """Extract basic keywords while excluding common English stop words."""
    tokens = re.findall(
        r"[a-zA-Z][a-zA-Z0-9+#.]*",
        text.lower(),
    )

    return {
        token
        for token in tokens
        if token not in ENGLISH_STOP_WORDS
        and len(token) > 1
    }


# ---------------- RESUME ANALYSIS ----------------
def analyze(resume_text, job_text):
    """Compare resume and job-description text using TF-IDF."""

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
    )

    try:
        matrix = vectorizer.fit_transform(
            [resume_text, job_text]
        )
    except ValueError as exc:
        raise ValueError(
            "Please enter meaningful text in both fields."
        ) from exc

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2],
    )[0][0]

    score = float(similarity) * 100

    resume_terms = clean_tokens(resume_text)
    job_terms = clean_tokens(job_text)

    matched = sorted(resume_terms & job_terms)
    missing = job_terms - resume_terms

    # Rank missing single-word terms by their TF-IDF importance.
    feature_names = vectorizer.get_feature_names_out()
    job_weights = matrix[1].toarray().ravel()

    term_weights = {
        term: float(job_weights[index])
        for index, term in enumerate(feature_names)
        if " " not in term and term in missing
    }

    missing = sorted(
        missing,
        key=lambda term: term_weights.get(term, 0),
        reverse=True,
    )

    return score, matched, missing[:15]


# ---------------- IMPROVEMENT SUGGESTIONS ----------------
def generate_suggestions(resume_text, missing):
    suggestions = []

    if missing:
        suggestions.append(
            "Review the missing keywords and include only those "
            "that genuinely match your skills and experience."
        )

    if len(resume_text.split()) < 100:
        suggestions.append(
            "Consider adding relevant project descriptions, "
            "coursework, or experience details."
        )

    if not re.search(
        r"\b(project|built|developed|created|implemented|designed|improved)\b",
        resume_text,
        re.IGNORECASE,
    ):
        suggestions.append(
            "Describe what you built, implemented, or contributed "
            "to, where applicable and truthful."
        )

    if not re.search(
        r"\b(github|portfolio|linkedin)\b",
        resume_text,
        re.IGNORECASE,
    ):
        suggestions.append(
            "Consider including a professional portfolio or "
            "GitHub/LinkedIn link if available."
        )

    suggestions.append(
        "Use measurable achievements only when you can support "
        "them with real evidence."
    )

    return suggestions


# ---------------- ANALYZE BUTTON ----------------
if st.button(
    "✨ Analyze Resume",
    type="primary",
    use_container_width=True,
):
    if len(resume.strip()) < 30 or len(job.strip()) < 30:
        st.session_state.pop("analysis_result", None)
        st.warning(
            "Please enter both your resume and job description "
            "with at least 30 characters each."
        )
    else:
        try:
            result = analyze(resume, job)
            st.session_state["analysis_result"] = result
        except ValueError as error:
            st.session_state.pop("analysis_result", None)
            st.error(str(error))


# ---------------- DISPLAY RESULTS ----------------
if "analysis_result" in st.session_state:
    score, matched, missing = st.session_state["analysis_result"]

    st.divider()
    st.subheader("📊 Your Match Analysis")

    metric1, metric2, metric3 = st.columns(3)

    metric1.metric(
        "Text Similarity",
        f"{score:.1f}%",
    )

    metric2.metric(
        "Matching Keywords",
        len(matched),
    )

    metric3.metric(
        "Potential Keyword Gaps",
        len(missing),
    )

    if score >= 60:
        st.success(
            "Your texts have relatively strong overlap. "
            "Review the keyword analysis before making changes."
        )
    elif score >= 30:
        st.info(
            "Your texts have some overlap. Review the potential "
            "gaps and tailor your resume truthfully."
        )
    else:
        st.warning(
            "Text overlap is currently low. Check your inputs "
            "and review the job requirements carefully."
        )

    left, right = st.columns(2, gap="large")

    with left:
        st.markdown("#### ✅ Matching Keywords")

        if matched:
            html = " ".join(
                f'<span class="pill">{term}</span>'
                for term in matched[:35]
            )
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.write(
                "No matching keywords were detected."
            )

    with right:
        st.markdown("#### 🔎 Potential Missing Keywords")

        if missing:
            html = " ".join(
                f'<span class="pill">{term}</span>'
                for term in missing
            )
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.write(
                "No missing keywords were detected by the "
                "basic keyword comparison."
            )

    st.markdown("#### 💡 Resume Improvement Suggestions")

    suggestions = generate_suggestions(resume, missing)

    for suggestion in suggestions:
        st.markdown(f"- {suggestion}")

    # Create a downloadable plain-text report.
    report = [
        "SmartHire AI - Resume Match Report",
        "=" * 36,
        f"Text similarity: {score:.1f}%",
        "",
        f"Matching keywords ({len(matched)}):",
        ", ".join(matched) if matched else "None detected",
        "",
        "Potential missing keywords:",
        ", ".join(missing) if missing else "None detected",
        "",
        "Improvement suggestions:",
        *[f"- {item}" for item in suggestions],
        "",
        "Disclaimer:",
        "The similarity score measures textual similarity only.",
        "It is not hiring probability, candidate quality, "
        "or model accuracy.",
    ]

    st.download_button(
        "⬇️ Download Analysis Report",
        data="\n".join(report),
        file_name="smarthire-analysis.txt",
        mime="text/plain",
    )


# ---------------- EXPLANATION ----------------
with st.expander("ℹ️ How It Works and Limitations"):
    st.markdown(
        """
        **TF-IDF:** Converts text into weighted numerical features.

        **Cosine similarity:** Estimates similarity between the
        resume and job-description vectors.

        **Keyword comparison:** Identifies words shared by both
        texts and selected terms found only in the job description.

        **Limitations:** This is an educational NLP prototype, not
        a trained hiring prediction model. Its score is not model
        accuracy, candidate quality, or probability of being hired.
        Basic keyword matching may miss synonyms and context.

        Do not use this tool as the sole basis for recruitment
        decisions. Never add skills you do not possess, and avoid
        entering sensitive personal information in public demos.
        """
    )


# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    '<p class="small-muted">'
    "Built for learning and career support "
    "| SDG 8: Decent Work and Economic Growth"
    "</p>",
    unsafe_allow_html=True,
)
