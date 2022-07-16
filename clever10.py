from functools import cmp_to_key
from jinja2 import Environment, PackageLoader, select_autoescape
from util import read_questions, get_yes_no_ratio, contains_latex_char
import click
import locale
import random
import termplotlib as tpl



locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")


@click.group()
def cli():
    pass


@click.command()
@click.option(
    '--questions-file',
    default='./questions.txt'
)
@click.option("--seed", type=int, help="Seed for option and question shuffling.", default=4131)
@click.option(
    "--debug",
    is_flag=True,
    help="When set, cards and options/answers are not shuffled. Also a 1cm grid is overlayed over cards, centered at the page center.",
)
def generate_cards(questions_file, seed, debug):
    """Produce a content.tex file from reading questions.txt and applying the card.tex template"""
    env = Environment(loader=PackageLoader("clever10"), autoescape=select_autoescape())
    questions = read_questions(questions_file, seed, debug)
    template = env.get_template("card.tex")
    with open("./content.tex", "w") as f:
        for question in questions:
            tex = template.render({**question, "debug": debug})
            f.write(tex)
            f.write("\n")
    click.echo(f"Wrote {len(questions)} questions to content.tex!")


@click.command()
@click.option(
    '--questions-file',
    default='./questions.txt'
)
def list_questions(questions_file):
    questions = sorted(
        map(lambda x: x["question"], read_questions(questions_file, False)),
        key=cmp_to_key(locale.strcoll),
    )
    for question in questions:
        click.echo(question)
    click.echo("---")
    total = len(questions)
    click.echo(f"{total} questions / {total/2} cards")


@click.command()
@click.option(
    '--questions-file',
    default='./questions.txt'
)
def find_bad_chars(questions_file):
    questions = read_questions(questions_file, False)
    for question in questions:
        strs = list(question['question']) + list(map(lambda x: x['content'], question['options'])) + list(map(lambda x: x['content'], question['answers']))
        if any(map(lambda x: contains_latex_char(x), strs)):
            click.echo(question['question'])
    click.echo("---")


@click.command()
@click.option(
    '--questions-file',
    default='./questions.txt'
)
def true_false_dist(questions_file):
    """For true/false questions, outputs distribution of ratio between true and false answers."""
    questions = read_questions(questions_file, False)
    labels = list(map(lambda x: f"{x} T / {10-x} F", range(11)))
    dist = list(map(lambda x: 0, range(len(labels))))

    for question in questions:
        [yes, no] = get_yes_no_ratio(question)
        if yes > 0 or no > 0:
            dist[yes] += 1

    fig = tpl.figure()
    fig.barh(dist, labels)
    fig.show()


cli.add_command(generate_cards)
cli.add_command(list_questions)
cli.add_command(true_false_dist)
cli.add_command(find_bad_chars)

if __name__ == "__main__":
    cli()
