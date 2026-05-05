import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# 1. Setup the Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 2. Define the Research Function
def conduct_bible_research(user_input):
    # System instructions tell Gemini how to behave
    instruction = (
        "You are a world-class Biblical Scholar. For any verse or topic provided: "
        "1. Provide the context. 2. Analyze key Greek/Hebrew words. "
        "3. Suggest 3 related cross-references. 4. Keep it concise and academic."
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"{instruction}\n\nResearch Request: {user_input}"
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

# 3. The Main Interface Loop
def main():
    print("--- 📖 Welcome to the Bible Research Assistant ---")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("Enter a verse or theological topic: ")
        
        if query.lower() == 'exit':
            print("Goodbye!")
            break
        
        print("\nSearching the archives...\n")
        result = conduct_bible_research(query)
        print(result)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()