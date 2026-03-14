from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os

print(os.path.exists("../.env"))

load_dotenv(find_dotenv())

model = ChatOpenAI(
    model="gpt-3.5-turbo",   
    temperature=0.7
)


messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")

]
result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)