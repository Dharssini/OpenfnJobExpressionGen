import streamlit as st
import openai

# OpenAI API key
openai.api_key = 'sk-proj-1YwXzXlKQNcLTPFnvXrTT3BlbkFJRiVDorm7mdu7rps42ZYO'

def generate_code(text_prompt, json_input, adaptor_specification, max_tokens=100):

    prompt = f"{text_prompt}\n\nJSON Input:\n{json_input}\n\nAdaptor Specification:\n{adaptor_specification}\n\nCode:"


    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the GPT-3 model (you can experiment with other engines)
        prompt=prompt,
        max_tokens=max_tokens,
        stop="\n\n"
    )

    generated_code = response.choices[0].text.strip()

    return generated_code

# Sample existing code
existing_text_prompt = "Create a new trackedEntityInstance \"person\" in dhis2 for the \"dWOAzMcK2Wt\" orgUnit."
existing_json_input = '{"data": {"name": "bukayo saka", "gender": "male"}}'
existing_adaptor_specification = "@openfn/language-dhis2@4.0.3"

# Streamlit UI
st.title("Code Generator")

# Text input for prompt
text_prompt = st.text_area("Text Prompt", existing_text_prompt)

# JSON input
json_input = st.text_area("JSON Input", existing_json_input)

# Adaptor specification input
adaptor_specification = st.text_input("Adaptor Specification", existing_adaptor_specification)

# Generate button
if st.button("Generate Code"):
    generated_code = generate_code(text_prompt, json_input, adaptor_specification)
    st.subheader("Generated Code:")
    st.code(generated_code)
