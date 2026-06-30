# 📧 AI Business Email Summarizer

An AI-powered business email summarization application that converts lengthy professional emails into concise, easy-to-read summaries using GPT-5 Mini via the OpenRouter API. The application features a simple Streamlit interface for real-time summarization.

---

## 🚀 Features

- AI-powered business email summarization
- Generates concise summaries in 2–5 sentences
- Focuses on the main purpose and key information
- Removes greetings, signatures, and unnecessary details
- Interactive Streamlit web interface
- Fast inference using OpenRouter GPT-5 Mini API
- Professional and recruiter-friendly output

---

## 🛠️ Technology Stack

- Python
- Streamlit
- OpenRouter API
- GPT-5 Mini
- OpenAI Python SDK
- python-dotenv
- Regular Expressions (Regex)

---

## 📂 Project Structure

```
business-email-summarizer/
│
├── app/
│   └── streamlit_demo.py
│
├── src/
│   └── inference.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/girivardhan86/business-email-summarizer-ai.git
cd business-email-summarizer-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app/streamlit_demo.py
```

---

## 💡 Example

### Input

A long business proposal or professional email containing multiple paragraphs.

### Output

A concise executive summary highlighting the email's purpose, key information, and important details in just a few sentences.

---

## 🎯 Learning Outcomes

- Built an end-to-end AI-powered NLP application
- Integrated GPT-5 Mini using the OpenRouter API
- Engineered prompts for high-quality email summarization
- Developed an interactive Streamlit application
- Managed API integration and environment variables securely
- Applied text preprocessing and prompt optimization techniques

---

## 🔮 Future Improvements

- Support PDF and DOCX email uploads
- Batch summarization for multiple emails
- Email spam detection
- Multi-language summarization
- One-click email export
- Meeting action item extraction
- Outlook and Gmail integration

---

## 👨‍💻 Author

**Girivardhan Reddy**

B.Tech CSE (AI & ML)

Passionate about Artificial Intelligence, NLP, Machine Learning, and Software Development.
