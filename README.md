Hello!

This repository has scripts that allow you to connect to the ChatGPI API. The most simple script allows you connect to the API, more advanced scripts will allow you to repeatedly input a prompt rapidly, and some of the scripts will even analyze the returned data for you with some minor tweaking. Here is an overview of the 5 scripts I have created at this point.

Looped_Request.py: This script connects to the API using your API key. Once you run the script you are asked for a prompt that will be sent to ChatGPT until you type "exit" and break the loop. 

Repeat_Research.py: Based on the previous script, this script will send a given prompt to ChatGPT a specified number of times and append the API's returns in a seperate text file, printing every response on a new line. 

Pie_Chart.py: Based on the previous script, this script will do the same thing but also create a pie chart based off the data if tweaked correctly.

Percent_Analysis.py: Based on the Repeat_Research.py script, this script will do the same thing as before but also analyze data and print percentages in a new text file if tweaked correctly. 

IQ_Test.py: This script takes a given number of questions for a test, asks it to ChatGPT a set number of times, and analyzes the data to print the percent correct for each question and print an average aggregate test score in a seperate text file. 
