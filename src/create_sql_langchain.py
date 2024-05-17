import os
import openai 
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

load_dotenv()

# Load the API key from the environment variables
api_key = os.getenv('OPEN_API_KEY')
openai.api_key = api_key

if not api_key:
    raise ValueError("API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Create the Sqlite database
db_uri = "sqlite:///financial_data.db"
db = SQLDatabase.from_uri(db_uri)

llm = OpenAI(api_key=api_key, temperature=0.5, verbose=True)

# Create our SQL Chain instance for building our SQL Queries
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# please replace this query with your own question
natural_language_question = "List the yield curve values on 8/29/2006 00:00:00."

# Generate the query
response = db_chain.invoke(natural_language_question)
print("Response", response)