# --- streamlit_app_openai.py ---
import streamlit as st
import json
import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Page config
st.set_page_config(page_title="AURUS HELP BOT", layout="centered")

# Custom CSS for background color
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 AURUS HELP BOT")
st.caption("Answering questions from process flows (Swimlanes) using AI")

st.markdown("---")

# Load available flows
FLOW_FILES = {
    "🛒 Order Processing": "data/swimlane_order_flow.json",
    "💳 Credit Card Approval": "data/credit_card_approval_flow.json",
    "🚚 Receiving Goods": "data/receiving_goods_flow.json"
}

st.header("🧩 Select a Process Flow")
selected_flow = st.selectbox("Select a flow to query:", list(FLOW_FILES.keys()))

SUGGESTED_QUESTIONS = {
    "🛒 Order Processing": [
        "What happens if the product is not in stock?",
        "Who is responsible for confirming the order?",
        "What step comes after checking the credit card?",
        "Under what conditions is the order cancelled?",
        "Which roles are involved in delivering the product?",
        "What is the final step of this process?"
    ],
    "💳 Credit Card Approval": [
        "What happens if the credit is bad?",
        "Who checks the credit criteria?",
        "What is the role of Accounts Receivable?",
        "What are the final steps to approve a sale?"
    ],
    "🚚 Receiving Goods": [
        "What happens if the contents don't match the order?",
        "Who performs the quality check?",
        "What is done if goods are rejected?",
        "Who is notified after the goods are accepted?"
    ]
}

# Load selected flow
def load_flow(file_path):
    with open(file_path, 'r') as f:
        steps = json.load(f)
    flow_text = "\n".join([f"{step.get('actor', 'Decision')}: {step.get('action', step.get('condition'))}" for step in steps])
    return flow_text

flow_text = ""
if selected_flow:
    flow_text = load_flow(FLOW_FILES[selected_flow])
    with st.expander("🔍 View Process Summary"):
        st.code(flow_text, language="markdown")

st.markdown("---")
st.subheader("💬 Ask a Question")

if 'question_input' not in st.session_state:
    st.session_state['question_input'] = ''

if selected_flow in SUGGESTED_QUESTIONS:
    st.markdown("💡 **Try one of the common questions:**")
    cols = st.columns(2)
    for i, q in enumerate(SUGGESTED_QUESTIONS[selected_flow]):
        if cols[i % 2].button(q, key=f"qbtn_{i}"):
            st.session_state['question_input'] = q

question = st.text_input("Or type your own question:", value=st.session_state['question_input'], key="question_box")
submit = st.button("🔎 Get Answer")

if submit and question:
    doc = [Document(page_content=flow_text)]
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=doc, question=question)

    st.markdown("### ✅ Answer")
    st.success(response.strip())
