import os

from groq import Groq
import groq

client = groq.Groq(api_key="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")


#client = Groq(
    # This is the default and can be omitted
#    api_key=os.environ.get("GROQ_API_KEY"),
#)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)