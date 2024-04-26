# Smart ATS (Applicant Tracking System) - Resume Improvement Tool

Smart ATS is a web application designed to help users improve their resumes by leveraging AI-powered analysis and generating tailored feedback. The tool utilizes Google's Generative AI capabilities to provide insights, match percentages, and even generate cover letters for job applications.

## Features

- **Resume Analysis**: Upload your resume and receive feedback on how well it aligns with a given job description.
- **Match Percentage**: Get a percentage indicating how well your resume matches the requirements of a job posting.
- **Cover Letter Generator**: Generate a customized cover letter based on your resume and the job description.
- **User-friendly Interface**: Simple and intuitive interface for easy navigation and interaction.

## Installation

1. Clone the repository:

git clone [https://github.com/SoumapriyoM/GenAi-Resume-Parse.git](https://github.com/SoumapriyoM/GenAi-Resume-Parse.git)


2. Navigate to the project directory:


3. Install dependencies:


4. Set up environment variables:

   - Create a `.env` file in the project root directory.
   - Add your Google API key to the `.env` file:

GOOGLE_API_KEY=your_api_key_here


5. Run the Streamlit app: streamlit run app.py


7. Access the application in your web browser at `http://localhost:8501`.

## Usage

1. **Upload Resume**: Click the "Upload Your Resume" button to upload your resume in PDF format.

2. **Paste Job Description**: Enter the job description into the text area provided.

3. **Resume Analysis**: Click the "Tell Me About the Resume" button to receive feedback on your resume's alignment with the job description.

4. **Match Percentage**: Click the "Percentage match" button to get a percentage indicating the match between your resume and the job description.

5. **Cover Letter Generation**: Click the "Give the cover letter" button to generate a cover letter based on your resume and the job description.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
