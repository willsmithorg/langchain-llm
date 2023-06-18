from langchain.chains import PALGenericChain, PALChain
from langchain.vectorstores import Chroma

from langchain import OpenAI
import os

os.environ['OPENAI_API_KEY'] = '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'

llm = OpenAI(temperature=0, max_tokens=512)
from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
vectorstore=Chroma

lessons = [
{'question':'There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?',
'solution':'''
def solution():
    """There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"""
    trees_initial = 15
    trees_after = 21
    # Added today must be the difference between initial and after.
    trees_added = trees_after - trees_initial
    # Compute and return result.    
    return trees_added
'''
},
{'question':'Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?',
'solution':'''
def solution():
    """Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?"""
    
    # Compute total before any were eaten.
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    
    # Remove chocolates that were eaten, to give chocolates left.
    chocolates_eaten = 35
    chocolates_left = total_chocolates - chocolates_eaten
    return chocolates_left
'''
},

{'question':'Print yes 4 times.',
'solution':'''
def solution():
    """Print yes 4 times."""
    
    # Repeat yes 4 times, with spaces in between.
    result = ' '.join(['yes' for _ in range(4)])
    # Return result.
    return result
'''
},
{'question':'On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball?',
'solution':'''
def solution():
    """On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball?"""
    # Put objects into a dictionary for quick look up
    colors = dict()
    colors['pencil'] = 'red'
    colors['mug'] = 'purple'
    colors['keychain'] = 'burgundy'
    colors['teddy bear'] = 'fuchsia'
    colors['plate'] = 'black'
    colors['stress ball'] = 'blue'

    # Look up the color of stress ball
    stress_ball_color = colors['stress ball']
    return stress_ball_color
'''
},
{'question':'How many letters are there in the string "a bcd efg"?',
'solution':'''
def solution():
    """How many letters are there in the string "a bcd3 efg()" """
    # remove whitespace
    str = "a bcd23 efg()"
    letters = ''.join(x for x in str if x.isalpha()) 
    # Return number of letters
    return len(letters)
'''
},
{'question':'How many unique letters are there in the string "United States"?',
'solution':'''
def solution():
    """How many unique letters are there in the string "United States" """
    str = "United States"
    # keep only lowercase alphabetical letters
    letters = [ c for c in str.lower() if c.isalpha() ]
    # Return number of unique letters
    return len(set(letters))
'''
},
{'question':'How many unique words are there in the string "a wood chuck could chuck wood"?',
'solution':'''
def solution():
    """How many unique words are there in the string "a wood chuck could chuck wood"?' """
    # split into words
    str = "a wood chuck could chuck wood"
    words = str.split()
    # Get unique by converting to set
    unique_words = set(words)
    # Return count.
    return len(unique_words)
'''
},

# {'question':'''Given the following table of data, what is the age of John?
#
# Name,Height_cm,Age
# Richard,170,25
# Mark,180,26
# John,160,27
# ''',
# 'solution':'''
# import pandas as pd
# from io import StringIO
# def solution():
#     """Given a  table of data, what is the age of John?"""
#
#     # Convert CSV into StringIO string.
#     str = StringIO("""
# Name,Height_cm,Age
# Richard,170,25
# Mark,180,26
# John,160,27
# """)
#     # Convert string into dataframe.
#     df = pd.read_csv(str)
#     # Extract John's record.  Assume there is only 1 John.
#     john_record = df[df['Name']=='John'].iloc[0]
#     # return John's age.
#     return john_record['Age']
# '''
# },
]

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

pal_generic_chain = PALGenericChain.from_generic_prompt(llm, embeddings, vectorstore, lessons, verbose=True)
print(pal_generic_chain.run(question))

#
pal_chain = PALChain.from_math_prompt(llm, verbose=True)
print(pal_chain.run(question))