from langchain.prompts import PromptTemplate
from constants import ANSWER_LANGUAGE

prompt_template_context = "{context}"
prompt_template_question = "{question}"
prompt_template = f"""Use the following portion of a long document to see if any of the text is relevant to answer the question. 
Return any relevant text verbatim. State your answer in the following language: {ANSWER_LANGUAGE}.
{prompt_template_context}
Question: {prompt_template_question}
Relevant text, if any:"""

QUESTION_PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)