import os
import openai

openai.api_key = ""

def doc_generate_function(description):
    response = openai.Completion.create(
        # model="code-davinci-002",
        model="text-davinci-001",
        prompt=f"Write the documentation for this code in bullet points:\n {description}\n",
        temperature=0.8,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        # stop=["```"]
    )
    return response.choices[0].text

# description = input()
# print(doc_generate_function(description))