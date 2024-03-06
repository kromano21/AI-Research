from openai import OpenAI
#You will have to install the openai module for this script to work using the "pip install openai" commands
client = OpenAI(api_key='')
#Enter your own API Key here. This is a string value, make sure your api_key is surrounded by quotation marks.
repetitions = 100
#Enter the number of time you want your prompt sent to ChatGPT here. This is an integer value.
user_input = ""
#Enter your prompt here. This is a string value, make sure your prompt is in quotes.

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            #Input the model you are using here. Use "gpt-3.5-turbo" for 3.5 and "gpt-4" for 4.0
            temperature=1.0,
            #This temperature parameter impacts the variance of responses. Valid Range: 0-2 where 0 is most determinastic and 2 is least determinastic. If you put a hashtag in front of it it will not be considered. 
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=150
            #maximum amount of tokins that can be generated in the chat, this will limit the reponse to the number of tokens given, Integer Value.
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error:", e)
        return None

def main():
    for i in range(repetitions):
        response = chat_with_gpt(user_input)
        if response:
            data = open("Data.txt", 'a')
            #saves responses to a text file
            #The 'a' puts the file in append mode. In this mode any data will be added to the end of file.
            data.write(response + "\n")
            #"\n" adds a line break, putting each response on a new line"
            data.close()
        else:
            print("Failed to get response from GPT")

main()
#This is the call to main. Note that it sometimes takes a while for the script to complete as response times with the API vary.