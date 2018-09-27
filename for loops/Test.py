from class2 import Question

question_prompts = [
   
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a)  Red\n(b) Green\n(c) Brown\n\n"
]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    
    ]



def run_test(questions):
    score = 0
    for every_question in questions:
        answer = input(every_question.prompt)
        if answer == every_question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")
    


run_test(questions)