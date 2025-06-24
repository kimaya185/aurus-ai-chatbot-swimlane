
# 🧠 Aurus Help Bot

A domain-specific AI assistant designed to answer queries from structured and unstructured workflows and documentation using natural language understanding. Built with LangChain, Streamlit, and OpenAI.

---
### 🔗 Live App

Try the chatbot live on Streamlit:

🌍 [Launch Aurus Help Bot](https://aurus-ai-chatbot-swimlane-we2u4m8c4ggraeflv3vmrq.streamlit.app/)

---
## 📌 Problem Statement

Build a chatbot that can respond to client questions using development portal data including text, swimlane flows, OpenAPI specs, etc. The chatbot must parse and understand different data formats with high accuracy (90%+).

---

## ⚙️ Tech Stack

- **LangChain** (QA chain, document loaders)
- **Streamlit** (User interface)
- **OpenAI GPT-3.5 Turbo** (LLM backend)
- **Python** (Core programming language)
- **JSON** (Used for representing swimlane flows)
- **GitHub Codespaces** (Project development and deployment environment)

> 🧪 Note: Integration trials with GPT-4.1, Gemini 1.5 Pro, Claude 3 Sonnet, and Mistral 7B (via HuggingFace) were explored but not used in the final build due to cost or access constraints.

---

## 🧪 Features

- Converts swimlane flow diagrams into structured JSON event sequences.
- Answers natural language queries by combining semantic understanding with step-wise flow reasoning.
- Flexible to handle various data types like structured text, swimlanes, OpenAPI specs (JSON/YAML), and potentially images.

---

## 🏗️ Implemented Swimlane Workflows

This project currently supports the following swimlane-based flows:

1. **Order Processing**
2. **Credit Card Approval**
3. **Receiving Goods**

Each flow is converted into a JSON structure that enables the chatbot to reason over multi-role processes and conditional logic.

### 🖼️ Swimlane Diagrams

#### 📦 Order Processing Flow
![Order Processing](https://github.com/kimaya185/aurus-ai-chatbot-swimlane/blob/main/ORDER_PROCESSING.png?raw=true)

#### 💳 Credit Card Approval Flow
![Credit Card Approval](https://github.com/kimaya185/aurus-ai-chatbot-swimlane/blob/main/CREDITCARD_APPROVAL.jpg?raw=true)

#### 📥 Receiving Goods Flow
![Receiving Goods](https://github.com/kimaya185/aurus-ai-chatbot-swimlane/blob/main/RECEIVING_GOODS.png?raw=true)

---

## 🚀 How to Run


- pip install -r requirements.txt

- streamlit run src/app.py

---

### 🎥 Demo Video
Walkthrough of querying 3 workflows with diverse questions.

Shows how the chatbot reasons based on actor roles, conditions, and flow transitions.

📺 https://www.loom.com/share/1309aa14393945c09eb7916a3d3766ec?sid=a0f9fb81-5aa7-4f72-9c99-372875b950e0

---


### 📖 Research & Model Justification

A comparative analysis of multiple LLMs (GPT-4.1, Claude 3, Gemini, Mistral) was conducted.

🧾 See [/docs/model_research.md](docs/model_research.md) for detailed insights on:

- Evaluation criteria (cost, latency, context size, reasoning)
- Model benchmarks and performance tradeoffs
- Final justification for selecting GPT-3.5 Turbo

---
```bash


