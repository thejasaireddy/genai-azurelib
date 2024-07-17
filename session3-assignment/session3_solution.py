"""
Problem Statement:
You're Software Developer at Azurelib , you have assigned a task to develop a simple text analysis tool that uses both Google's Gemini and OpenAI's ChatGPT models to analyze 
short text inputs.

 The tool will determine the sentiment of the text using Gemini and generate a one-word category for the text using ChatGPT.


TODOS

Create a Python script that can process a list of short text inputs.

For each input:

Use the Gemini API to determine if the sentiment is positive, negative, or neutral.
Use the ChatGPT API to categorize the text into a single word (e.g., "Technology", "Sports", "Politics", etc.).
Print the results for each input.
"""

# Gemini API

import google.generativeai as genai

genai.configure(api_key="AIzaSyCqWIBzyncc2UATMWYildyl32u1BjoRt3Q")

model = genai.GenerativeModel("gemini-1.5-flash")

def get_text_inputs():
  """
  This function prompts the user for short text inputs and returns them as a list.
  """
  text_list = []
  while True:
    user_input = input("Enter a short text input (or 'q' to quit): ")
    if user_input.lower() == 'q':
      break
    text_list.append(user_input)
  return text_list

# Example usage
text_inputs = get_text_inputs()
print("Your inputs:")
for text in text_inputs:
  print(text)

response_list = []
for prompt in text_inputs:
    response_list.append(model.generate_content("Determine if the sentiment of this text /'" + prompt +"' is positive, negative, or neutral and provide the word and sentiment only two words." ))

for response in response_list:
    print(response.text)

# ChatGPT API

import openai

# Set your OpenAI API key
openai.api_key = "sk-proj-TEt6M7EuMPY2kEzN6Q0tT3BlbkFJw1QAjV9boBM3CGE2mcL7"

def get_openai_response(prompt):
    try:
        # Make a request to the OpenAI API
        response = openai.Completion.create(
            model = "gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=16,  # Maximum number of tokens in the response
            n=1,  # Number of responses to generate
            stop=None,  # Sequences where the API should stop generating further tokens
            temperature=0.7  # Sampling temperature
        )
        
        # Extract and return the generated text
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Example usage
if __name__ == "__main__":
    for prompt in text_inputs:
        response = get_openai_response("Categorize the text into a single word " + prompt + "(e.g., 'Technology', 'Sports', 'Politics', etc.).")
        print("Response from OpenAI:", response)
