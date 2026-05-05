import os
import google.generativeai as genai

# On Mac, this pulls from your environment variables
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Explain the significance of the Greek word 'Logos' in John 1:1.")
print(response.text)