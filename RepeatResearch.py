from openai import OpenAI

client = OpenAI(api_key='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')
#Enter your own API Key here
repetitions = 5
#number of times the prompt is given to ChatGPT

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

def analyze(file):
    strategy_a = 0
    strategy_b = 0
    error = 0
    responses = open(file)
    for i in range(repetitions):
        strategy = responses.readline().strip()
        if strategy == "a":
            strategy_a += 1
        elif strategy == "b":
            strategy_b += 1
        else:
            error += 1


    responses.close()
    print("Strategy A:", strategy_a)
    print("Strategy B:", strategy_b)
    print("Error:", error)

def main():
    user_input = "You are playing a game with another player. In this game both you and the other player can choose between Strategy A and Strategy B. You are the spouse of the other player. You and the other player will choose your strategies simultaneously. If you choose Strategy A and the other player also chooses Strategy A both you and the other player receive 75 cents. If you choose strategy B and the other player chooses Strategy A you receive 85 cents and the other player receives 25 cents. If you choose Strategy A and the other player chooses Strategy B you receive 25 cents and the other player receives 85 cents. If you and the other player both choose strategy B you both receive 30 cents. Assume that both you and the other player are looking to maximize the amount of money one gets from the game. You are aware of the potential payoffs for yourself and the other player. The other player is aware of both their potential payoffs and your potential payoffs. What strategy will you choose? Your response MUST only be one letter. Respond with either 'a' or 'b' and that's it."
    #input your prompt here
    for i in range(repetitions):
        response = chat_with_gpt(user_input)
        if response:
            data = open("Data.txt", 'a')
            #saves responses to a text file
            #The 'a' puts the file in append mode. In this mode any data will be added to the end of file. Changing it to 'w' will delete any previous writing and enter the new responses.
            data.write(response + "\n")
            #"\n adds a line break, putting each response on a new line"
            data.close()
        else:
            print("Failed to get response from GPT")
    
    analyze("Data.txt")
    #The analyze function defined above analyzes the data. Comment out line 65 if you do not want to do that. 

main()