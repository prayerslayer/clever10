import random


def option_or_answer_to_dict(option_or_answer):
    if option_or_answer.startswith("[img:"):
        return {"type": "image", "content": option_or_answer[5:-1]}
    else:
        return {"type": "text", "content": option_or_answer}


def parse_question(question_str, debug):
    question = question_str[0]
    options = list(
        map(lambda x: option_or_answer_to_dict(x.split(";")[1]), question_str[1:])
    )
    answers = list(
        map(lambda x: option_or_answer_to_dict(x.split(";")[0]), question_str[1:])
    )

    ordering = random.sample(range(10), 10) if not debug else range(10)

    options = [options[i] for i in ordering]
    answers = [answers[i] for i in ordering]

    return {"question": question, "options": options, "answers": answers}


def read_questions(path_to_file, debug):
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
            questions.append(parse_question(question_str, debug))
    return questions


def get_yes_no_ratio(question):
    answers = question["answers"]
    all_img = all(map(lambda x: x["type"] == "image", answers))
    if not all_img:
        return [0, 0]
    answer_contents = list(map(lambda x: x["content"], answers))
    all_img_t_or_f = all(map(lambda x: x in ["T", "F"], answer_contents))
    if not all_img_t_or_f:
        return [0, 0]
    return [answer_contents.count("T"), answer_contents.count("F")]
