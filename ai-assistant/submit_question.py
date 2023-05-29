import openai
import argparse

from dotenv import dotenv_values


def prompt_and_response(text_prompt, num_tokens):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text_prompt}],
        max_tokens=num_tokens,
        temperature=0.4
    )

    # print(response)
    return response["choices"][0]["message"]["content"]

if __name__ == '__main__':
    config = dotenv_values(".env")
    openai.api_key = config["OPENAI_API_KEY"]

    argparser = argparse.ArgumentParser()

    argparser.add_argument("--text", type=str, default="What is the meaning of life?", help="Text to send to ChatGPT")
    argparser.add_argument("--num_tokens", type=int, default=250, help="Number of response tokens")
    args = argparser.parse_args()

    text_prompt = args.text
    num_tokens = args.num_tokens

    print(prompt_and_response(text_prompt, num_tokens))
