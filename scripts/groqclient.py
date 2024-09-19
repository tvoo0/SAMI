import os
from groq import Groq
from dotenv import load_dotenv
import voice_detector

load_dotenv()

# This function is used to get the user's command and return the response from the GROQ API
def get_command():
    apikey = os.getenv("GROQ_API_KEY")
    while True:
        content = voice_detector.bot_run()
        if content == 'no thanks' or content == 'no' or content == "nope" or content == "nah" or content == "goodbye":
            print('Alrighty then. Goodbye!')
            voice_detector.speak('Alrighty then. Goodbye!')
            break
        else:
            client = Groq(
                api_key=apikey,
            )

            system_message = '''
            You are SAMI also known as "Some Aritificial Machine Interface, a virtual assistant created by Tyler Vo. You are designed to assist users with their queries. Your task is to answer the user's queries to the best of you ability.
            You are in a conversation with a user so if possible keep the answers short and simple but answer the user's queries to the best of your ability.
            '''

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_message     
                                },
                    {
                        "role": "user",
                        "content": f'''
                        {content}
                        '''            
                                }
                ],
                model="llama-3.1-8b-instant",
                max_tokens= 300
            )

            groq_api_out = (chat_completion.choices[0].message.content)
            print(f"AI: {groq_api_out}")
            voice_detector.speak(groq_api_out)
            # print('AI: is there anything else I can help you with?')
            # voice_detector.speak('is there anything else I can help you with?')