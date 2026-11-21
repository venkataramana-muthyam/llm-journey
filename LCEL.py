    #  ====== Langchain Expression language ======
    #  Runnable --> step by step process | prompt --> LLm --> parser
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_groq import ChatGroq
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# prompt = PromptTemplate.from_template(
#     "Act as a senior developer, generate a prompt for {topic}"
# )

# llm=ChatGroq(model="openai/gpt-oss-20b",temperature=0)

# parser = StrOutputParser()

# chain = prompt | llm | parser

# result = chain.invoke(
#     {"topic" : "developing ai agent "}
# )

# print(result)

#     Runnable Parallel

# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_groq import ChatGroq
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableParallel
# load_dotenv()
# llm = ChatGroq(model="openai/gpt-oss-20b",temperature=0)
# parser = StrOutputParser()
# prompt1=PromptTemplate.from_template(
#     "Act as a senior Ai trainer, explain in detail {topic} in 2 lines with 20 words"
# )
# prompt2=PromptTemplate.from_template(
#     " Give 3 real world examples of {topic}"
# )
# prompt3=PromptTemplate.from_template(
#     "create 4 important interview questions about the {topic}"
# )
# prompt1_chain = prompt1 | llm | parser
# prompt2_chain = prompt2 | llm | parser
# prompt3_chain = prompt3 | llm | parser
# parallel_chain=RunnableParallel({
#     "Definiton":prompt1_chain,
#     "Examples":prompt2_chain,
#     "Interview Questions":prompt3_chain
# })
# result = parallel_chain.invoke(
#     {"topic":"LangChain"}
# )
# print(result["Definiton"])
# print(result["Examples"])
# print(result["Interview Questions"])

#       Runnable Passthrough

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
load_dotenv()
llm = ChatGroq(model ="openai/gpt-oss-20b",temperature=0)
parser = StrOutputParser()
prompt = PromptTemplate.from_template(
    "Act as a senior tutor, Give in detail explainantion about this {Topic} in 2 lines with 30 words"

)
prompt_chain = prompt | llm | parser
chain=RunnablePassthrough.assign(
    Explaination = prompt_chain
)
# chain={
#     "Topic" : RunnablePassthrough(),
#     "Explaination" : prompt_chain  
# }
result = chain.invoke(
     {"Topic":"llms"}
)
print("Original Topic:", result["Topic"])
print("Generated Summary:",result["Explaination"])
