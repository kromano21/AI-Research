from openai import OpenAI
import os

client = OpenAI(api_key='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')
repetitions = 10
number_of_questions = 1
question_counter = 1
correct_ratios = []

question_1 = "2, 4, 6, 8. What number logically follows this series? Respond with only the number"
answer_1 = 10

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error:", e)
        return None

def get_data(question):
    global question_counter
    for x in range(repetitions):
        response = chat_with_gpt(question)
        if response:
            with open("Data.txt", 'a') as data:
                data.write(response + "\n")
        else:
            print("Failed to get response from GPT")
    correct_answers = 0
    wrong_answers = 0
    total_answers = repetitions
    with open("Data.txt") as responses:
        for x in range(repetitions):
            answer = int(responses.readline().strip())  #Fix: Convert response to integer
            if answer == answer_1:
                correct_answers += 1
            else:
                wrong_answers += 1
    os.remove("Data.txt")
    correct_ratio = correct_answers / total_answers
    percent_correct = correct_ratio * 100
    print_percent_correct = str(percent_correct)
    with open("Results.txt", 'a') as results:
        results.write("Percent Correct: " + print_percent_correct + "%" + "\n" + "\n")
    correct_ratios.append(correct_ratio)
    question_counter += 1

def analyze():
    accumulated_ratio = sum(correct_ratios)
    raw_test_score = accumulated_ratio / number_of_questions
    test_score = raw_test_score * 100
    printable_test_score = str(test_score)
    with open("Results.txt", 'a') as results:
        results.write("Average Test Score: " + printable_test_score + "%")

def main():
    global question_counter  #Fix:Declare question_counter as global
    if question_counter == 1:
        get_data(question_1)
    analyze()

main()