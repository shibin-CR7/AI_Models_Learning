from phi.assistant import Assistant
from phi.tools.sql import SQLTools
from phi.llm.groq import Groq
from dotenv import load_dotenv
import os

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
host='ep-odd-frog-a5q7xu81.us-east-2.aws.neon.tech', 
dbname='uat',
user='postgres',
password='sCDZTFr15Svj',
port=5432


# Load environment variables
load_dotenv()

# Check and load the Groq API key
os.environ['GROQ_API_KEY'] = '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'

assistant = Assistant(
    llm=Groq(model="mixtral-8x7b-32768"),
    tools=[SQLTools(
        db_url=db_url,
    )],
    show_tool_calls=True,
)

assistant.print_response("List the tables in the database. Tell me about contents of one of the tables", markdown=True)
