import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from a .env file
load_dotenv()

# Configure the Gemini API with the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set the parameters for text generation
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Create a model instance with the specified configuration
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

def summarize_text(input_text):
    # Start a chat session with an empty history
    chat_session = model.start_chat(history=[])

    # Send a message to the model asking to summarize the input text
    prompt = f"Please summarize the following text in short:\n\n{input_text}"
    response = chat_session.send_message(prompt)

    # Return the summarized text
    return response.text

# Main function to accept user input and provide summary
if __name__ == "__main__":
    # Accept input text from the user
    input_text = input("Please enter the text you want to summarize:\n")

    # Get the summarized text
    summary = summarize_text(input_text)
    
    # Print the summarized text
    print("\nSummarized Text:\n", summary)
