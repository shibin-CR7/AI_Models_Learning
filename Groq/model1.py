import os
from groq import Groq
#from flask_sqlalchemy import SQLAlchemy
#from flaskext.sqlalchemy import SQLAlchemy
#from Flask-SQLAlchemy import SQLAlchemy
#from Flask-SQLAlchemy import SQLAlchemy

import groq
#from sanity import Client

client = groq.Groq(api_key="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")

#client = Groq(
#    api_key=os.environ.get("GROQ_API_KEY"),
#)
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": "your are a chatbot ,only know about cars\n"
        },
        {
            "role": "user",
            "content": "explaine about porche 992 gt3 rs"
        },
        {
            "role": "assistant",
            
            "content": "model year and its configuration"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
