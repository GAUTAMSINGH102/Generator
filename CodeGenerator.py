import os
import openai

# load API Key ( https://beta.openai.com/account/api-keys )
# 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
openai.api_key = ""

def code_generate_function(description):
    # response = openai.Completion.create(
    #     # model="code-davinci-002",
    #     model="text-davinci-001",
    #     # prompt=f"Python function to do the following: {description}\n\n```python\n",
    #     prompt=f"write a python code following these description:{description}",
    #     temperature=0.5,
    #     max_tokens=500,
    #     # top_p=1
    #     # frequency_penalty=0.3,
    #     # presence_penalty=0.3,
    #     # stop=["```"]
    # )

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Create a Python script from the idea of this text: {}".format(description),
        temperature=0.7,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].text

# print("What should the function do?")
# description = input()
# print(generate_function(description))