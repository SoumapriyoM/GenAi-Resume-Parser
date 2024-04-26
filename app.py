import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
from io import BytesIO
import base64
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input.format(text=text, jd=jd))
    return response.text
def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text
# Function to download cover letter as text or PDF

def download_cover_letter(cover_letter_text):
    # if file_format == 'Text':
    #     # Download as text file
        b64 = base64.b64encode(cover_letter_text.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="cover_letter.txt">Download Cover Letter</a>'
    # elif file_format == 'PDF':
        # Download as PDF file
        # pdf_data = BytesIO()
        # pdf_data.write(cover_letter_text.encode('utf-8'))
        # b64 = base64.b64encode(pdf_data.getvalue()).decode()
        # href = f'<a href="data:application/pdf;base64,{b64}" download="cover_letter.pdf">Download Cover Letter</a>'

        return href

#Prompt Template

input_prompt1 = """
You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
resume:{text}
job_description:{jd}

Highlight the strengths and weaknesses of the applicant in relation to the specified job_description.
The structure should be like:
Strengths:
    . strength1
    . strength2
    . strength3
    ...
Weaknesses:
    .weakness1
    .weakness2
    .weakness3
    ... 
Overall summary: summary

"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of of tech field, software engineering, data science, data analyst
and big data engineer.  and ATS functionality, 
I have referring from the resume.

resume:{text}
job_description:{jd}

You are an skilled ATS with the given jobe role.Be critical of this and tell exact truth.
your task is to evaluate the resume against the provided job description by keywords. give me the percentage percentage (Match with job_description) of match if the resume matches
the job description. First the output should come as percentage , then point wise keywords matching,then point wise keywords missing and last final thoughts.
Follow the structure
job_description Match:"%",
MissingKeywords:[all missing key words],
Your opinion:""
"""
input_prompt = """
Generate a cover letter for the following job position:
and take 
candidates_info :{text}
job_description:{jd}

Job Title: [Job Title from jd]
Company: [Company Name from jd]

Candidate Information:
Name: [Candidate Name from candidates_info]
Skills: [List of Relevant Skills from candidates_info]
Qualifications: [List of Qualifications from candidates_info]
Experiences: [Summary of Work Experiences from candidates_info]

Cover Letter Structure:
- Salutation: Dear Hiring Manager,
- Introduction: [Brief Introduction of Candidate and Interest in Position from jd]
- Body Paragraphs: [Highlight Relevant Skills and Experiences from jd]
- Closing: [Closing Remarks]

Key Points to Include:
- Include my college name,Internships,certifications from candidates_info
- Express genuine interest in the position and company.
- Highlight specific skills and experiences that align with the job requirements.
- Demonstrate enthusiasm and eagerness to contribute to the team.

Tone and Style:
- Formal and professional tone.
- Positive and confident language.
- Concise and well-organized paragraphs.

Closing:
Thank you for considering my application. I look forward to the opportunity to discuss how my skills and experiences align with [Company Name]'s needs in more detail.

[Candidate's Name from candidates_info]

Must follow all the given instruction.
"""
## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit1 = st.button("Tell Me About the Resume", key="button1")

submit3 = st.button("Percentage match", key="button2")

submit4= st.button("Give the cover letter", key="button3")

if submit1:
    if uploaded_file and jd is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt1)
        st.subheader(response)
if submit3:
    if uploaded_file and jd is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt3)
        st.subheader(response)
if submit4:
    if uploaded_file and jd is not None:
        # Add functionality to download the cover letter
        text=input_pdf_text(uploaded_file)
        cover_letter = get_gemini_repsonse(input_prompt)
        download_link = download_cover_letter(cover_letter)
        st.markdown(download_link, unsafe_allow_html=True)
