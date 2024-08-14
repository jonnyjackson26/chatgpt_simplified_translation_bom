import os
from openai import OpenAI
from key import api_key


client = OpenAI(api_key=api_key,)
def chat_gpt2(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def chat_gpt(lines):
    prompt="I am going to give you verses of a chapter in the book of mormon. I need you to give me back the list, but have each verse translated or rephrased to be easier to understand. It is important you keep the same order and number of lines. Do not give me numbered lists. Do not include any friendly message like 'here you go:', just start your response with the translation of the first line: "+"\n".join(lines)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    r=response.choices[0].message.content
    r=r.split("\n")
    print("response:\n\n\n")
    print(r)
    r = [item for item in r if item != ''] #remove '' in list
    return r #[1:] #get rid of the first line (chat gpt yapping)

books = ["title","introduction", "three","eight","js", "1-nephi", "2-nephi", "jacob", "enos", "jarom", "omni", "words-of-mormon", "mosiah", "alma", "helaman", "3-nephi", "4-nephi", "mormon", "ether", "moroni"]
chapters = {
    "title":1,"introduction":1,"three":1,"eight":1,"js":1,
    "1-nephi": 22, "2-nephi": 33, "jacob": 7, "enos": 1, "jarom": 1, "omni": 1, "words-of-mormon": 1,
    "mosiah": 29, "alma": 63, "helaman": 16, "3-nephi": 30, "4-nephi": 1,
    "mormon": 9, "ether": 15, "moroni": 10
}

def main():
    for book in books:
        for chapter in range(1,chapters[book]+1):
            path=f'bom-english/{book}/{chapter}.txt'
            #write translated_lines to 'bom-simplified/{book}/{chapter}.txt
            with open(path, 'r') as file:
                lines = file.readlines()

            translated_lines = chat_gpt(lines) # Translate lines using ChatGPT

            output_dir = f'bom-simplified/{book}'
            os.makedirs(output_dir, exist_ok=True)

            # Write translated_lines to the new file
            output_path = f'{output_dir}/{chapter}.txt'
            with open(output_path, 'w') as file:
                for line in translated_lines:
                    file.write(line + '\n')

book="3-nephi"
chapter="11"

path=f'bom-english/{book}/{chapter}.txt'
#write translated_lines to 'bom-simplified/{book}/{chapter}.txt
with open(path, 'r') as file:
    lines = file.readlines()

translated_lines = chat_gpt(lines) # Translate lines using ChatGPT

output_dir = f'bom-simplified/{book}'
os.makedirs(output_dir, exist_ok=True)

# Write translated_lines to the new file
output_path = f'{output_dir}/{chapter}.txt'
with open(output_path, 'w') as file:
    for line in translated_lines:
        file.write(line + '\n')

#main()
#print(chat_gpt("Tell me a joke about programming"))