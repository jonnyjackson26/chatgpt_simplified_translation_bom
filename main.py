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

#capitalizes each line in lines 
def chat_gpt(lines):
    p="Translate each line to be easier to understand but retain the meaning:"+"".join(lines)
    r="""
    Here’s a simpler version of the text, retaining the core meaning:

The baptism of little children is a serious mistake. Little children are considered innocent and pure because of the Atonement of Christ. Faith, repentance, humility, receiving the Holy Ghost, and enduring to the end lead to salvation. This message was relevant around A.D. 401–21.

A letter from my father Mormon to me, Moroni, written shortly after I began my ministry. He said:

My dear son Moroni, I am very happy that the Lord Jesus Christ has remembered you and called you to His ministry. I am constantly praying for you, asking God the Father, through His Son Jesus, to keep you strong in faith until the end.

I am deeply troubled that there are arguments among you about baptizing little children.

If I understand correctly, there have been disputes among you about whether to baptize children. I want you to work hard to correct this mistake; that’s why I wrote this letter.

After learning about these disputes, I asked the Lord for guidance. The Lord, through the Holy Ghost, told me:

Listen to Christ, your Redeemer, Lord, and God. I came into the world not to call the righteous, but sinners to repentance. Children are innocent and do not need baptism because they cannot sin. The curse of Adam does not apply to them, and the law of circumcision is no longer needed.

The Holy Ghost has shown me that baptizing little children is a serious mistake before God.

Teach repentance and baptism only to those who are responsible for their actions and can sin. Teach parents to repent, be baptized, and humble themselves like their children, and they will be saved with their children.

Children do not need to repent or be baptized. Baptism is for those who need to repent and follow the commandments.

Children are pure in Christ from the beginning of the world. If not, God would be unfair and changeable. Many children have died without baptism. If baptism were required for salvation, these children would be condemned to hell.

Anyone who thinks children need baptism is misguided and lacks faith, hope, and charity.

It is wrong to believe that God saves one child because of baptism and condemns another for not being baptized. Those who distort God’s ways in this way will face judgment unless they repent. I speak with confidence and authority from God and fear nothing from men, because perfect love casts out fear.

I am filled with everlasting love and see all children equally. I love them with a perfect love, and they are all capable of salvation.

God is not partial or changeable but unchanging forever. Children cannot repent, so it is a serious wrong to deny God’s mercies to them. They are all alive in Him because of His mercy.

Anyone who says children need baptism denies Christ’s mercies and the power of His redemption.

Such individuals are in grave danger of death and torment. I speak boldly because God has commanded me. Listen to this message and heed it, or you will face judgment from Christ.

All children are alive in Christ, as are those without the law. Redemption comes to those who are not condemned. Those who are not condemned cannot repent, so baptism is of no use to them.

Baptism should not be a mockery or a false show of trust in dead works.

Repentance is for those under condemnation and the curse of breaking the law.

The first step of repentance is baptism, which comes by faith, and fulfilling commandments leads to remission of sins.

Remission of sins brings meekness and humility, which lead to receiving the Holy Ghost. This Comforter gives hope and perfect love, which endures through diligent prayer until all saints dwell with God.

I will write to you again if I do not go to fight the Lamanites soon. The pride of the Nephite people has led to their destruction unless they repent.

Pray for their repentance. I fear the Spirit has stopped striving with them, and they are trying to remove all God’s power and authority, denying the Holy Ghost.

Having rejected such knowledge, they will soon face the fulfillment of prophecies and the words of our Savior.

Goodbye for now until I write again or see you. Amen.


    """
    r=r.split("\n")
    r = [item for item in r if item != ''] #remove '' in list
    return r[1:-1] #get rid of the first and last part (chat gpt yapping)

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

path=f'bom-english/{"moroni"}/{"8"}.txt'
#write translated_lines to 'bom-simplified/{book}/{chapter}.txt
with open(path, 'r') as file:
    lines = file.readlines()

translated_lines = chat_gpt(lines) # Translate lines using ChatGPT

output_dir = f'bom-simplified/{"moroni"}'
os.makedirs(output_dir, exist_ok=True)

# Write translated_lines to the new file
output_path = f'{output_dir}/{"8"}.txt'
with open(output_path, 'w') as file:
    for line in translated_lines:
        file.write(line + '\n')

#main()
#print(chat_gpt("Tell me a joke about programming"))