from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

response = model.invoke("Act as a senior deveoloper,write a program find second highest number in the list python")

print(response.content)