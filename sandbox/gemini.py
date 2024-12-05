# https://ai.google.dev/gemini-api/docs/quickstart?lang=python
import google.generativeai as genai
import os

api_key = "AIzaSyBv9jSPmF30c4cpy4-QOpqVManAXfPPAv8"

source_language = "FR"
target_language = "ES"

prompt = """
Traduis "J'aime les fleurs" en japonais. La réponse ne doit contenir que la traduction
"""

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
print(response.text)