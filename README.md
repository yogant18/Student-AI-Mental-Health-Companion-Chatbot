# Student AI — Mental Health Companion Chatbot

A Streamlit chatbot powered by **Google Gemini** (Generative AI) to support student mental well-being.

---

## 🌱 Project Description

Students often face high levels of **stress, anxiety,** and **loneliness**, yet hesitate to approach professional counselors.  
This AI-driven chatbot aims to fill that gap by:

- Detecting user mood through **sentiment analysis**,  
- Generating empathetic, motivational responses, and  
- Offering short **relaxation/mindfulness tips**–all in a safe conversational interface.

It is **not a replacement for therapy**, but a supportive companion.

---

## 🚀 Features

- **Sentiment detection**: Uses TextBlob / optional HF pipeline to infer mood.  
- **Contextual replies**: Gemini generates responses based on prompt + mood.  
- **Relaxation tips**: Prompts include short guidance (breathing, grounding).  
- **Crisis keyword detection**: Recognizes phrases indicating self-harm or crisis and responds with care.  
- **Streamlit UI**: Clean, minimal interface for chat + settings (model, temperature, etc.).  
- **Modular architecture**: Separated config, AI client, sentiment utilities, and UI for clarity and ease of extension.

---

## 🧰 Technology Stack

| Component            | Tool / Library                |
|----------------------|-------------------------------|
| Web UI               | Streamlit                     |
| AI backend           | Google Gemini via `google-genai` SDK |
| Sentiment analysis   | TextBlob (fallback), optional Transformers |
| Language / Runtime   | Python 3.x                    |
| Config / secrets     | `dotenv` or `os.environ`      |

---

## 📥 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yogant18/Mental-Health-Companion-Chatbot.git
cd Mental-Health-Companion-Chatbot

## 📄 License

MIT License  

Copyright (c) 2025 Yogant (Mental Health Companion Chatbot)

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without li



