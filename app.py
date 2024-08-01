from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "Profile_Picture.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Bishwarup Dey"
PAGE_ICON = ":wave:"
NAME = "Bishwarup Dey"
DESCRIPTION = """
Data Analyst with a knack for uncovering insights and driving data-driven decisions.
"""
EMAIL = "bishwarupdey11@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/bishwarup-dey-b0915123a/",
    "GitHub": "https://github.com/Bishwarup10",
    "Twitter": "https://x.com/Bishwarup96",
}
PROJECTS = {
    "Olympic Games Analysis [Power BI | SQL]": "https://github.com/Bishwarup10/Olympic-Games-Analysis-SQL-Power-BI",
    "British Airways Reviews [Tableau]": "https://github.com/Bishwarup10/Tableau-Project",
    "Data Science Job Analysis w/SQL": "https://github.com/Bishwarup10/SQL_Project_Data_Job_Analysis",
    "Credit Card Consumption [Python]": "https://github.com/Bishwarup10/Credit-Card-Consumption",
    "Sales Data Analysis And Visualizations w/ Python": "https://github.com/Bishwarup10/Sales-Data-Visualizations",
    "Customer Analysis for Retail [Python]": "https://github.com/Bishwarup10/Retail-Case-Study",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- PROFESSIONAL SUMMARY ---
st.write('\n')
st.subheader("Professional Summary")
st.write(
    """
- ✔️ Experience in extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in Python and SQL
- ✔️ Proficient in data visualization with Power BI and Tableau
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn,Pandas, Numpy, Matplotlib, Seaborn), SQL 
- 📊 Data Visualization: Power BI, Tableau, MS Excel,Plotly
- 🗄️ Databases: MySQL, PostgreSQL
"""
)


# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write("🎓", "**Bachelor of Computer Applications**")
st.write("2014 - 2017 | IITM, GGSIPU, New Delhi")
st.write(
    """
- ► CGPA: 6.9/10.0
"""
)
st.write("🎓", "**Master of Computer Applications**")
st.write("2017 - 2020 | BVICAM, GGSIPU, New Delhi")
st.write(
    """
- ► CGPA: 7.9/10.0
"""
)


# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
st.write("📜", "**Data Analytics With Python | AnalytixLabs**")
st.write("Issued: 2021")
st.write(
    """
- ► Completed courses on Python for Data Science, Data Visualization, and Machine Learning.
"""
)
st.write("📜", "**AI & DL Using Python | AnalytixLabs**")
st.write("Issued: 2022")
st.write(
    """
- ► Gained expertise in Artificial Intelligence and Deep Learning using Python.
"""
)


# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Assistant Football Coach | Crio High Performance Academy**")
st.write("01/2021 - 08/2022 | Gurugram, Haryana")
st.write(
    """
- ► Assisted the First Team Coach in conducting drills and sessions.
- ► Analyzed team performance to provide insights for improvements.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst Intern | INB Vacations**")
st.write("07/2022 - 12/2022 | New Delhi")
st.write(
    """
- ► Analyzed large datasets using SQL and Python, identifying key trends and patterns, which enabled employers to uncover critical insights for informed decision-making, resulting in a 15% increase in operational efficiency.
- ► Developed and presented data visualizations using Power BI, resulting in enhanced stakeholder understanding of complex data sets.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst Intern | Fairdeal.Market**")
st.write("06/2023 - 08/2023 | Gurugram, Haryana")
st.write(
    """
- ► Played a key role in crafting the brand dashboard utilizing no-code software, and engaged in rigorous testing, resulting in a 25% reduction in deployment time.
- ► Participated in a team project to enhance data quality, achieving a 20% improvement in data accuracy.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Business Analyst | Fairdeal.Market**")
st.write("09/2023 - 02/2024 | Gurugram, Haryana")
st.write(
    """
- ► Designed and implemented dynamic dashboards in Excel and Power BI, empowering brands with data-driven insights for strategic decision-making.
- ► Participated in a team project to engineer a Python-based data extractor app utilizing Flask, streamlining information retrieval processes, and facilitating stakeholder access to critical data.
"""
)


# --- CONTACT ---
st.write('\n')
st.subheader("Contact")
st.write("Feel free to reach out via email or phone.")
st.write("📫 Email: [bishwarupdey11@gmail.com](mailto:bishwarupdey11@gmail.com)")
st.write("📞 Phone: +91-8375822148")
