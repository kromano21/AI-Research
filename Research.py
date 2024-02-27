from openai import OpenAI

client = OpenAI(api_key='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')
#Enter your own API Key here

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.2,
            #This temperature parameter impacts the variance of responses. Valid Range: 0-2 where 0 is most determinastic and 2 is least determinastic.
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=150
            #maximum amount of tokins that can be generated in the chat, impacts the length of responses
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error:", e)
        return None

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        response = chat_with_gpt(user_input)
        if response:
            print("GPT:", response)
        else:
            print("Failed to get response from GPT")

if __name__ == "__main__":
    main()

