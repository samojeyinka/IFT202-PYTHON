import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

def summarize_text(input_text):

    chat_session = model.start_chat(history=[])


    prompt = f"Please summarize the following text in short:\n\n{input_text}"
    response = chat_session.send_message(prompt)


    return response.text

def count_words_and_characters(text):
    words = len(text.split())
    characters = len(text)
    return words, characters


if __name__ == "__main__":

    file_path = 'text.txt'
    try:
        with open(file_path, 'r') as file:
            input_text = file.read()
        
        initial_word_count, initial_char_count = count_words_and_characters(input_text)


        summary = summarize_text(input_text)
        
 
        result_word_count, result_char_count = count_words_and_characters(summary)
        
  
        print("\nSummarized Text:\n", summary)

 
        print("\nInitial Word Count:", initial_word_count)
        print("Initial Character Count:", initial_char_count)
        print("Result Word Count:", result_word_count)
        print("Result Character Count:", result_char_count)
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found. Please make sure the file exists and try again.")
