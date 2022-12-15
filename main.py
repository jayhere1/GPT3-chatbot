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
    prompt = prompt.encode(encoding="ASCII", errors="ignore").decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop,
    )
    text = response["choices"][0]["text"].strip()
    return text


if __name__ == "__main__":
    conversation = list()
    while True:
        user_input = input("USER: ")
        conversation.append("USER: %s" % user_input)
        text_block = "\n".join(conversation)
        prompt = f"Hello, {text_block}"
        prompt = prompt + "\nBOT:"
        response = gpt3_completion(prompt)
        print("BOT:", response)
        conversation.append("BOT: %s" % response)
