import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

class AiCodeReviewer:
    def __init__(self):
        curr_path = os.getcwd()
        cred_path = os.path.abspath(os.path.join(curr_path, "..", ".env_sep/creds.env"))
        load_dotenv(cred_path)
        self.key = os.getenv("google_api_key")

    def chatbot(self, human_prompt:str=None, system_instruction:str=None)-> object:
        """
        # gemini supports python version greater that 3.9
        # pip install google-generativeai
        """
        genai.configure(api_key=self.key)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                      system_instruction=system_instruction)
        # response = model.generate_content("Explain how AI works")
        # print(response.text)
        return model
    
    def streamlit_app(self)->None:
        st.title("AI Code Reviewer")
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"]=[]
        instruction = """You are expert in "AI fields". Act as an expert AI code reviewer.
          Analyze the provided code for clarity, efficiency, maintainability, and adherence to best practices.
          Identify potential errors, suggest improvements, and provide clear, actionable feedback. Highlight sections of code that demonstrate excellent design and explain why. 
          Avoid generic remarks; focus on specific, meaningful insights that help improve the code's quality..
                              """
        model = self.chatbot(instruction)
        chat = model.start_chat(history=st.session_state["chat_history"])

        for msg in chat.history:
            st.chat_message(msg.role).write(msg.parts[0].text)

        user_prompt = st.chat_input()

        if user_prompt:
            st.chat_message("user").write(user_prompt)
            response = chat.send_message(user_prompt)
            st.chat_message("ai").write(response.text)
            st.session_state["chat_history"]=chat.history

if __name__ == "__main__":
    ai = AiCodeReviewer()
    ai.streamlit_app()

