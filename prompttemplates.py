
################## SINGLE TURN PROMPT TEMPLATE #####################

# from langchain_core.prompts import PromptTemplate

# prompt=PromptTemplate.from_template(

#     """
#     Explain {Topic}
#     in simple telugu
#     """
# )

# formatted_prompt = prompt.invoke(
#     {"Topic":"Data Science"}
# )

# print(formatted_prompt.to_string())

# from langchain_core.prompts import ChatPromptTemplate

# prompt = ChatPromptTemplate.from_template(
#     "Explain {Topic} in simple Telugu"
# )
# formatted = prompt.invoke({"Topic": "Data Science"})
# print(formatted)

################ MULTI TURN OR DYNAMIC VARIABLES ###############

# from langchain_core.prompts import PromptTemplate

# prompt=PromptTemplate.from_template(
# """
# create a {days} days travel plan for {destination}.
# budget:{budget}
# language:{language}
# """
# )

# formatted=prompt.invoke(
#     {
#         "destination":"Goa",
#         "days":3,
#         "budget":"Medium",
#         "language":"Telugu"
#     }
# )

# print(formatted.to_string())


################## CHAT PROMPT TEMPLATE ###################

# from langchain_core.prompts import ChatPromptTemplate 
# from langchain_ollama import ChatOllama
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You Are a Senior Gen-Ai and Agentic-Ai Trainer"
#         ),
#         (
#             "human",
#             "Explain {Topic}"
#         )
#     ]
# )

# llama=ChatOllama(model="qwen2.5:3b",temperature=0,timeout=120)

# chain = prompt | llama
# formatted=chain.invoke(
#     {"Topic":"Prompt Engineering"}
# )
# print(formatted.content)

from langchain_core.prompts import(
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

llm=ChatOllama(model="qwen2.5:3b",temperature=0)

prompt=ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant."
    ),
    MessagesPlaceholder(
        variable_name="history"
    ),
    (
        "human",
        "{question}"
    )
])

history=[
    HumanMessage(
        content="Who is MS.Dhoni"
    )
]
chain=prompt | llm 
messages=chain.invoke(
    {
        "history": history,
        "question":"Where was he born"
    }
)

print(messages.content)
