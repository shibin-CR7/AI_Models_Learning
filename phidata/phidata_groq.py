from phi.assistant import Assistant
from phi.llm.groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Check and load the Groq API key
os.environ['GROQ_API_KEY'] = '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'

assistant = Assistant(
    llm=Groq(model="mixtral-8x7b-32768"),
    description="You help people with their health and fitness goals.",
    # debug_mode=True,
)
assistant.print_response("Share a quick healthy breakfast recipe.", markdown=True)
