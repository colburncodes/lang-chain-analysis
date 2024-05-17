import os
import openai 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

load_dotenv()

# Load the API key from the environment variables
api_key = os.getenv('OPEN_API_KEY')
openai.api_key = api_key

if not api_key:
    raise ValueError("API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Create the Sqlite database
db_uri = "sqlite:///financial_data.db"
db = SQLDatabase.from_uri(db_uri)

llm = ChatOpenAI(api_key=api_key, temperature=0.5, verbose=True)

# Create an SQL Agent
"""
create_sql_agent Function:
- Function Purpose: Initializes an SQL agent. The method creates an agent with specified properties.
- Parameters Explained:
  - llm: The language model being used, in this case, provided by OpenAI.
  - toolkit: The SQLDatabaseToolkit, which contains tools for query creation, execution, syntax checking, and more.
  - verbose: A boolean flag to enable detailed logging.
  - agent_type: Specifies the type of agent. Here 'ZERO_SHOT_REACT_DESCRIPTION' implies the agent's capability to understand and react to descriptions in a zero-shot learning context.
"""

agent_excute = create_sql_agent(llm, toolkit=SQLDatabaseToolkit(db=db, llm=llm), verbose=True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# Query SQL Agent
query_result = agent_excute.invoke("List the yield curve values on 8/29/2006 00:00:00.")

print("Query Result:", query_result)