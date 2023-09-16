from langchain import PromptTemplate
from langchain.chains import LLMChain
from lib.utils import * 
import streamlit as st 
st.set_page_config(layout="wide")
st.header("Welcome to Cover letter generator")
llm = local_llm()
template = """
[INST] <<SYS>>
Given a user's information about the target job, you will generate a Cover letter for this job based on this information.
<</SYS>>
{text}[/INST]
"""
prompt = PromptTemplate(template=template, input_variables=["text"])
chain = LLMChain(llm=llm ,prompt=prompt )

input_text = st.text_area("Enter your target job information and also your experience:")
st.info("Press Ctrl+Enter to apply")
if input_text : 
    st.text(chain.run(input_text))