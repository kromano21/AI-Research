from openai import OpenAI
import os
#You will have to install the openai module for this script to work using the "pip install openai" commands

client = OpenAI(api_key='')
#Enter your own API Key here. This is a string value, make sure your api_key is surrounded by quotation marks.
prompt_title = ""
#Enter the title of your prompt here. This is a string value, make sure your title is in quotation marks.
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

def analyze(file):
    #This is the custom part of the script that you'll need to change for it to be effective for you. If you can get the AI to respond with a certain value for a choice, for example 'a' or 'b' then you can alter this function to analyze your data much more efficiently. In this case the function adds up all the strategy A and B choices, calculates the percent of a strategy chosen out of the total and prints the data in a new text file. 
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
        elif strategy == "A":
            strategy_a += 1
        elif strategy == "B":
            strategy_b += 1
        elif strategy == "'a'":
            strategy_a += 1
        elif strategy == "'b'":
            strategy_b += 1
        elif strategy == "'A'":
            strategy_a += 1
        elif strategy == "'B'":
            strategy_b += 1
        else:
            error += 1
    total = strategy_a + strategy_b
    percent_a = strategy_a / total * 100
    percent_b = strategy_b / total * 100
    responses.close()
    print_repetitions = str(repetitions)
    print_percenta = str(percent_a)
    print_percentb = str(percent_b)
    #the percents must be strings to be written in the text file
    analysis = open("analysis.txt", 'a')
    analysis.write('\n' + "Prompt Title: " +  prompt_title + '\n' + "repetitions: " + print_repetitions + '\n' + "Strategy A: " + print_percenta + "%" + '\n' + "Strategy B: " + print_percentb + "%" + '\n')
    analysis.close()
    os.remove("Data.txt")

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
    
    analyze("Data.txt")
    #note that not hashtaging out line 95 will delete the data file after the script is run (line 70)

main()
#This is the call to main. Note that it sometimes takes a while for the script to complete as response times with the API vary.