# Multilingual Storytelling with Accents

## Project Overview

This project is a **Streamlit web application** that translates text into different languages and converts the translated text into speech. Users can either **enter text manually** or **upload files**, and the application will translate the content and generate an **audio narration**.

The system demonstrates how **AI-powered language translation and speech synthesis** can be integrated into an interactive web interface.

---

## Proposed System

The original project specification proposes the use of:

- **GPT-3.5-turbo model from OpenAI** for language translation  
- **Google Text-to-Speech (gTTS)** for speech generation  

---

## Implemented System

Due to **OpenAI API payment limitations**, the implemented project uses:

- **Deep Translator (Google Translate service)** for translation  
- **Google Text-to-Speech (gTTS)** for audio generation  

This allows the application to function using **free translation services while maintaining the intended functionality of the project**.

---

## Features

- Translate text into **multiple languages**
- Convert **translated text into speech**
- Upload files for translation
- Download generated **audio files**
- Simple and **user-friendly interface using Streamlit**

---

## Supported Languages

The application currently supports translation into the following languages:

- French  
- Spanish  
- German  
- Hindi  
- Malayalam  

---

## Supported File Formats

Users can upload the following file types for translation:

- **TXT files**
- **PDF files**
- **CSV files**
- **Excel (XLSX) files**

---

## Technologies Used

- **Python**
- **Streamlit**
- **Deep Translator**
- **Google Text-to-Speech (gTTS)**
- **Pandas**
- **PyPDF2**

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/multilingual-storytelling.git
cd multilingual-storytelling
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows
```bash
venv\Scripts\activate
```

Mac/Linux
```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the Streamlit application using the following command:

```bash
streamlit run app.py
```

After running the command, the application will open automatically in your browser.

---

## How to Use

1. **Enter text** or **upload a file**  
2. **Select the target language**  
3. Click **Translate and Convert to Speech**  
4. View the **translated text**  
5. Listen to the **generated audio**  
6. **Download the audio file** if needed  

---

## Project Structure

```
multilingual-storytelling
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

- Add **more languages**
- Allow users to select **different voice accents**
- Add **speech playback speed control**
- **Deploy the application online**

---

## Author

**Krishna Priya**