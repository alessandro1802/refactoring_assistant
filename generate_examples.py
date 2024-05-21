from os.path import join
from dotenv import load_dotenv
from openai import OpenAI


if __name__ == "__main__":
    # Connect to the API
    load_dotenv()
    client = OpenAI()

    n = 10  # Number of example pairs to generate

    # API call
    prompt = """Generate more or less simple example of Python code which is subject to refactoring and the corresponding refactored code in the following format:
    Before:
    ```python
    [code_before_refactoring]
    ```
    After:
    ```python
    [code_after_refactoring]
    ```
    The before code must contain function calls, variable assignments etc. While the results must have type annotations, docstrings, etc."""

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a Python code refactoring generator. Your response strictly follows the specified format. Your answers must be unique."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        n=n
    )

    output_path = "./examples"
    file_name_template = "{}.py"
    idx = 40  # Last present example number

    # Write output
    for i in range(n):
        for line in completion.choices[i].message.content.split("```")[:-1]:
            if "Before" in line:
                idx += 1
                file_name = file_name_template.format(idx)
                file = open(join(output_path, "before", file_name), "w+")
            elif "After" in line:
                file = open(join(output_path, "after", file_name), "w+")
            else:
                file.write(line.strip("python")[1:])
                file.close()
