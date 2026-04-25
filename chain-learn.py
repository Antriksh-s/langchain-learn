import json
import os
from dotenv import load_dotenv  
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Load environment variables (ensure OPENAI_API_KEY is in your .env file)
load_dotenv()

# 1. Define the Prompt
prompt = ChatPromptTemplate.from_template(
    "Return a JSON object which can be pretty printed using jq with the keys 'topic' and 'joke' for a joke about {topic}."
    )

# 2. Initialize the Model
# By default, this looks for the OPENAI_API_KEY environment variable
model = ChatOpenAI(model="gpt-4o", temperature=0.7)

# 3. Initialize the Parser
parser = JsonOutputParser()

# 4. Construct the Chain (using LCEL: LangChain Expression Language)
chain = prompt | model | parser

# 5. Execute the Chain
#topic_input = {"topic": "Engineering"}

topic_input = [
    {"topic": "artificial intelligence"},
    {"topic": "space travel"},
    {"topic": "cooking"},
    {"topic": "coding"}
]

response = chain.batch(topic_input)
json_output = json.dumps(response, indent=2)

print(json_output)