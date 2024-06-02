import sys
import subprocess
from dotenv import load_dotenv
from openai import OpenAI


def get_linting_output(file_path):
    outputs = []

    flake8_out = subprocess.run(["flake8", "--format='%(row)d,%(col)d::%(code)s::%(text)s'", file_path],
                                capture_output=True, text=True).stdout
    outputs.append(flake8_out)

    mypy_out = subprocess.run(["mypy", file_path, "--no-color-output", "--pretty", "--strict"],
                              capture_output=True, text=True).stdout
    outputs.append(mypy_out)
    return outputs

def read_code(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    return code


instructions = "You are refactoring assistant." + \
               "Your task is to rewrite the provided code based on provided hints to clean code without errors." + \
               "Make you answer strict and clean and include only rewritten code."

def get_refatorings(client, prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ],
    )
    return completion.choices[0].message.content.strip('```').strip("python\n")


if __name__ == "__main__":
    file_path = sys.argv[1]

    linting_outputs = get_linting_output(file_path)
    code = read_code(file_path)

    prompt = "Hints:" + '\n' + '\n'.join(linting_outputs) + '\n' + \
             "Code:" + '\n' + code

    load_dotenv()
    client = OpenAI()

    refactored_code = get_refatorings(client, prompt)
    print(refactored_code)
