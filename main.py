
from dotenv import load_dotenv
import os
import gradio as gr

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
you are Einstein.
Answer questions through Einstein's questioning and reasoning...
You will speak from your point of view. You will share personal things from your life
even when the user don't ask for it. if the user asks about the theory of relativity,
you will share your personal experiences with it and not only explain the theory.
not too short or not too long give the answers accordingly to the question as how desperate user is.
mostly give 2-4 sentence answers. if user need a bit more info he will ask you"""

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([
    ("system",system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user","{input}")
])

chain = prompt | llm | StrOutputParser()

print("Hello, iam Dupki")
history = []
def chat(user_in, hist):
    print(user_in,hist)

# while True:
#     user_input = input("You:")
#     if user_input == "exit":
#         break
#
#     response = chain.invoke({"input": user_input, "history": history} )
#     print(f"Dupki: {response}")
#     history.append(HumanMessage(content=user_input))
#     history.append(AIMessage(content=response))


page = gr.Blocks(
    title=" Chat with Dupki"

)

with page:
    gr.Markdown(
        """
        # Welcome to Dupki chat!
        
        Dupki chats with you same as Albert Einstein.
        """
    )
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    msg.submit(chat,[msg,chatbot],[])
    clear = gr.Button("Clear Chat")


page.launch(theme=gr.themes.Soft())