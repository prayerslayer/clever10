import random

random.seed(4131)


def part_or_answer_to_dict(part_or_answer):
    if part_or_answer.startswith("[img:"):
        return {"type": "image", "content": part_or_answer[5:-1]}
    else:
        return {"type": "text", "content": part_or_answer}


def parse_question(question_str):
    question = question_str[0]
    parts = list(
        map(lambda x: part_or_answer_to_dict(x.split(";")[1]), question_str[1:])
    )
    answers = list(
        map(lambda x: part_or_answer_to_dict(x.split(";")[0]), question_str[1:])
    )

    ordering = random.sample(range(10), 10)
    parts = [parts[i] for i in ordering]
    answers = [answers[i] for i in ordering]

    return {"question": question, "parts": parts, "answers": answers}


def read_questions(path_to_file):
    questions = list()
    with open(path_to_file, "r") as f:
        while True:
            cntr = 11
            question_str = list()
            while cntr > 0:
                line = f.readline()
                if line == "\n":
                    continue
                if line == "":
                    return questions

                question_str.append(line.strip())
                cntr -= 1
            questions.append(parse_question(question_str))
    # Turn on for final rendering
    # random.shuffle(questions)
    return questions
