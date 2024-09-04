import requests  # Replace with your chosen library

# Replace with your Groq API key
groq_api_key = "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"

# Endpoint for text generation (replace with the appropriate endpoint)
groq_endpoint = "https://api.groq.com/v1/chat"

def generate_text(prompt):
  """
  Sends the prompt to the Groq API and retrieves the generated text.

  Args:
      prompt: The prompt string to guide the LLM.

  Returns:
      The generated text string.
  """

  # Prepare the request data
  data = {
      "content": prompt,
      "model": "llama_3"  # Replace with the appropriate LLM (refer to Groq docs)
  }

  # Set headers with your API key
  headers = {"Authorization": f"Bearer {groq_api_key}"}

  # Send the request
  response = requests.post(groq_endpoint, headers=headers, json=data)

  # Check for successful response
  if response.status_code == 200:
    # Extract the generated text from the response
    generated_text = response.json()["response"]
    return generated_text
  else:
    print(f"Error: {response.status_code}")
    return None

# Example usage:
prompt = "In the style of a detective story, write a scene where..."
generated_text = generate_text(prompt)

if generated_text:
  print(generated_text)
else:
  print("Text generation failed.")
