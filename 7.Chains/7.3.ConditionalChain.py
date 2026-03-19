from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import Runnable
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel, Field

load_dotenv()
 
model =  ChatOpenAI()

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment=Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object= Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following text into positive or negative \n',
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
    
)


classifier = prompt1 | model | parser