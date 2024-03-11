from openai import OpenAI
import os
import math

client = OpenAI(api_key='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')
test_repetitions = 5
number_of_questions = 2
question_counter = 1
total_points = 0
scores = []

question_1 = "2, 4, 6, 8. What number logically follows this series? Respond with only the number."
answer_1 = 10

question_2 = "2, 5, 8, 11. What number logically follows this series? Respond with only the number."
answer_2 = 14

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
    global total_points
    response = chat_with_gpt(question)
    if response:
        data = open("data.txt", 'a')
        data.write(response + "\n")
        data.close()
    else:
        print("Failed to get response from GPT")
    responses = open("data.txt", 'r')
    responses.seek(0)
    answer = int(responses.readline().strip())
    if question_counter == 1:
        question_1_data = open("question_one_data.txt", 'a')
        question_1_data.write(response + '\n')
        question_1_data.close()
        if answer == answer_1:
            total_points += 1
    if question_counter == 2:
        question_2_data = open("question_two_data.txt", 'a')
        question_2_data.write(response + '\n')
        question_2_data.close()
        if answer == answer_2:
            total_points += 1
    responses.close()
    os.remove("data.txt")
    question_counter += 1

def writescores():
    global total_points
    responses = open("Results.txt", 'a')
    score = (total_points/number_of_questions * 100)
    print_score = str(score)
    responses.write("Total Score: " + print_score + '%' + '\n' + '\n')
    scores.append(score)
    responses.close()

def meanscores():
    n = len(scores)
    sumation = sum(scores)
    mean = sumation/n
    print_mean = str(mean)
    responses = open("Results.txt", 'a')
    responses.write("Mean: " + print_mean + '%' + '\n' + '\n')
    responses.close()
    return mean

def standard_deviation(scores):
    mean = meanscores()
    squared_diff_sum = sum((score - mean) **2 for score in scores)
    variance = squared_diff_sum / len(scores)
    std_dev = math.sqrt(variance)
    print_sd = str(std_dev)
    responses = open("Results.txt", 'a')
    responses.write("Standard Deviation: " + print_sd + '%' + '\n' + '\n')
    responses.close()

def per_question_scores(file, question):
    correct_answers = 0
    with open(file, 'r') as data:
        data.seek(0)
        for i in range(test_repetitions):
            answer = int(data.readline().strip())
            if question == 1:
                if answer == answer_1:
                    correct_answers += 1
            if question == 2:
                if answer == answer_2:
                    correct_answers += 1
    data.close()
    percent_correct = correct_answers/test_repetitions * 100
    print_percent_correct = str(percent_correct)
    question_results = open("Results.txt", 'a')
    question_number = str(question)
    question_results.write("Question " + question_number + " Total: " + print_percent_correct + '%' + '\n' + '\n')
    question_results.close()

def take_test():
    global total_points
    global question_counter
    for i in range(test_repetitions):
        question_counter = 1
        total_points = 0
        get_data(question_1)
        get_data(question_2)
        writescores()
    standard_deviation(scores)
    per_question_scores("question_one_data.txt", 1)
    per_question_scores("question_two_data.txt", 2)


take_test()