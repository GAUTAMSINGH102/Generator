import os
import openai

openai.api_key = ""

def code_converter_function(description):
    response = openai.Completion.create(
        # model="code-davinci-002",
        model="text-davinci-001",
        prompt=f"Convert this code from python to javascript:\n {description}\n",
        temperature=0.7,
        max_tokens=1000,
        # top_p=1,
        # frequency_penalty=0.3,
        # presence_penalty=0,
        # stop=["```"]
    )
    return response.choices[0].text

# description = input()
# print(code_converter_function(description))