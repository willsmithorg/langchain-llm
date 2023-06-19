from langchain.chains import PALGenericChain, PALChain
from langchain.vectorstores import Chroma
import lessons

from langchain import OpenAI
import os

os.environ['OPENAI_API_KEY'] = 'sk-sHdd3jVAqyCPEiShN8sOT3B' + 'lbkFJMGaOoCiZGt77yUyJ3Ye4'

llm = OpenAI(temperature=0, max_tokens=512)
from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
vectorstore=Chroma


# question = "On the desk, you see two blue booklets, two purple booklets, and two yellow pairs of sunglasses. If I remove all the pairs of sunglasses from the desk, how many purple items remain on it?"
# question = "Print hello 10 times , but every 3rd time print goodbye instead"
# question = "How many vowels are in the word palindrome?"
# question = '''
# Given the following table:
#
# Country,Capital,GDP_Per_Capita
# Russia,Moscow,15000
# Sweden,Stockholm,45000
#
# How many times higher is the GDP per capita in Sweden than Russia?
# '''
# question = "What is 4 times the sum of the first 20 terms, 1 - 1/3 + 1/5 - 1/7 + ...?"
# question = "How many numbers are there in the sentence '1 2 buckle my shoe 3 456 knock at the door'?"
# question = "How many letters of the alphabet are neither vowels nor in the word 'Timbuktu'?"
# question = "How many unique letters are there in the names of the capital cities of Singapore, Malaysia and Thailand?"
question = "If the first day of the non-leap year is a wednesday, how many days in the year are not weekends?"

pal_generic_chain = PALGenericChain.from_generic_prompt(llm, embeddings, vectorstore, lessons.lessons, verbose=True)
print(pal_generic_chain.run(question))

#
pal_chain = PALChain.from_math_prompt(llm, verbose=True)
print(pal_chain.run(question))