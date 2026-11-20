#  String Output Parser

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

prompt=PromptTemplate.from_template(
    "Act as a senior ai developer Explain this {Topic} in easy way even 5 years kid also understand what your'e explain in 30 words"
)

llm=ChatGroq(model="llama3-70b-8192", temperature=0)

parser = StrOutputParser()

chain = prompt | llm | parser
formatted=chain.invoke({"Topic":"Langchain"})
print(formatted)

    #  Json Output Parser

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
prompt=PromptTemplate.from_template(
"""
Analyze This Institute Review,
Review : {Review}
Return only json with these keys:
{{
    "sentiment":"positive/negative/netural",
    "reason":"i want a indetail in 20 words",
    "rating":"rating out of 5"
}}

"""
)

llm = ChatGroq(model="llama3-70b-8192", temperature=0)

parser=JsonOutputParser()

chain=prompt | llm | parser

result = chain.invoke(
        {
            "Review":"Institute was good but placement support was netural"
        }
)
print(result)