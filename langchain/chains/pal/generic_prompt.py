# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

template = (
    '''
Q: {question}

# solution in Python:
{solution}
'''.strip()
    + "\n\n\n"
)
GENERIC_PROMPT = PromptTemplate(input_variables=["question", "solution"], template=template)
