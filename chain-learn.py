import os
from dotenv import load_dotenv  

# Updated Imports
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables (ensure OPENAI_API_KEY is in your .env file)
load_dotenv()

# 1. Define the Prompt
prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")

# 2. Initialize the Model
# By default, this looks for the OPENAI_API_KEY environment variable
model = ChatOpenAI(model="gpt-4o-mini")

# 3. Initialize the Parser
parser = StrOutputParser()

# 4. Construct the Chain (using LCEL: LangChain Expression Language)
chain = prompt | model | parser

# 5. Execute the Chain
topic_input = {"topic": "artificial intelligence"}
response = chain.invoke(topic_input)

print(response)