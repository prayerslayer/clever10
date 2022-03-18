from functools import cmp_to_key
from jinja2 import Environment, PackageLoader, select_autoescape
from util import read_questions, get_yes_no_ratio
import click
import locale
import random
import termplotlib as tpl


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
    click.echo(f"{total} questions / {total/2} cards")


@click.command()
def true_false_dist():
    """For true/false questions, outputs distribution of ratio between true and false answers."""
    questions = read_questions("./questions.txt", False)
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

if __name__ == "__main__":
    cli()
