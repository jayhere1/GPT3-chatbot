"""
Main function

"""


import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt3_completion(
    prompt,
    engine="text-davinci-003",
    temp=0.7,
    top_p=1.0,
    tokens=400,
    freq_pen=0.0,
    pres_pen=0.0,
    stop=["BOT:", "USER:"],
):

    '''
    Get responses
    '''
    gpt_prompt = prompt.encode(encoding="ASCII", errors="ignore").decode()
    gpt_response = openai.Completion.create(
        engine=engine,
        prompt=gpt_prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop,
    )
    text = gpt_response["choices"][0]["text"].strip()
    return text


if __name__ == "__main__":
    CONVERSATION = []
    while True:
        user_input = input("USER: ")
        CONVERSATION.append(f"USER: {user_input}" )
        TEXT_BLOCK = "\n".join(CONVERSATION)
        current_prompt = f"Hello, {TEXT_BLOCK}"
        current_prompt = f'{current_prompt} \n BOT:'
        response = gpt3_completion(current_prompt)
        print("BOT:", response)
        CONVERSATION.append(f"BOT: {response}")
