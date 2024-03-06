from openai import OpenAI
#You will have to have the OpenAI module install for this script to work. Use the command "pip insall openai" in a command terminal
client = OpenAI(api_key='')
#Enter your own API Key here

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            #Input the model you are using here. Use "gpt-3.5-turbo" for 3.5 and "gpt-4" for 4.0
            temperature=0.2,
            #This temperature parameter impacts the variance of responses. Valid Range: 0-2 where 0 is most determinastic and 2 is least determinastic.
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
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            #YOU CAN TYPE exit TO BREAK THE LOOP
            print("Exiting...")
            break
        response = chat_with_gpt(user_input)
        if response:
            print("GPT:", response)
        else:
            print("Failed to get response from GPT")

if __name__ == "__main__":
    main()

