from functools import cmp_to_key
from jinja2 import Environment, PackageLoader, select_autoescape
from util import read_questions
import click
import locale
import random

random.seed(4131)
locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--debug",
    is_flag=True,
    help="When set, cards and options/answers are not shuffled. Also a 1cm grid is overlayed over cards, centered at the page center.",
)
def generate_cards(debug):
    """Produce a content.tex file from reading questions.txt and applying the card.tex template"""
    env = Environment(loader=PackageLoader("clever10"), autoescape=select_autoescape())
    questions = read_questions("./questions.txt", debug)
    if not debug:
        random.shuffle(questions)
    template = env.get_template("card.tex")
    with open("./content.tex", "w") as f:
        for question in questions:
            tex = template.render({**question, "debug": debug})
            f.write(tex)
            f.write("\n")
    click.echo(f"Wrote {len(questions)} questions to content.tex!")


@click.command()
def list_questions():
    questions = sorted(
        map(lambda x: x["question"], read_questions("./questions.txt")),
        key=cmp_to_key(locale.strcoll),
    )
    for question in questions:
        click.echo(question)
    click.echo("---")
    total = len(questions)
    completion = "" if total % 2 == 0 else "-> INCOMPLETE!!"
    click.echo(f"{total} questions / {total/2} cards {completion}")


cli.add_command(generate_cards)
cli.add_command(list_questions)

if __name__ == "__main__":
    cli()
