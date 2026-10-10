from google import genai

client = genai.Client()  # reads GEMINI_API_KEY from the environment

MODEL = "gemini-3-flash-preview"  # if this errors, copy the current model name from AI Studio


def get_llm_response(prompt):
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text


def print_llm_response(prompt):
    print(get_llm_response(prompt))