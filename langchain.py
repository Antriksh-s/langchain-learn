import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-4o", temperature=0.9)

result = chat.invoke([{"role": "user", "content": "What is the capital of France?"}])

print(result)
