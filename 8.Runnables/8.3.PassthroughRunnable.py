from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,  RunnablePassthrough, RunnableSequence 

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}' ,
    input_variables=['text']
    
)

joke_gen_chain = prompt1 | model | parser


parallel_chain = RunnableParallel({
    "joke": joke_gen_chain,
    "explanation": prompt2 | model | parser
})


print(parallel_chain.invoke({"topic": "cricket"}))