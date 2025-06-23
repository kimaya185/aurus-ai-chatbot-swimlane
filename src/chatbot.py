
import json
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load swimlane flow data
with open('data/swimlane_order_flow.json', 'r') as f:
    steps = json.load(f)

# Format data
flow_text = "\n".join([
    f"{step.get('actor', 'Decision')}: {step.get('action', step.get('condition'))}" for step in steps
])
docs = [Document(page_content=flow_text)]

# Initialize OpenAI LLM
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
print("✅ Using OpenAI LLM (gpt-3.5-turbo)")

# Create QA chain
chain = load_qa_chain(llm, chain_type="stuff")

# Chat loop
def ask_question(question):
    return chain.run(input_documents=docs, question=question)

if __name__ == "__main__":
    while True:
        q = input("\nAsk a question about the order flow: ")
        if q.lower() in ['exit', 'quit']:
            break
        print("Answer:", ask_question(q))

