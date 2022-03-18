from functools import cmp_to_key
from jinja2 import Environment, PackageLoader, select_autoescape
from util import read_questions
import click
import locale


locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")


@click.group()
def cli():
    pass


@click.command()
def generate_cards():
    """Produce a content.tex file from reading questions.txt and applying the card.tex template"""
    env = Environment(loader=PackageLoader("clever10"), autoescape=select_autoescape())
    questions = read_questions("./questions.txt")
    template = env.get_template("card.tex")
    with open("./content.tex", "w") as f:
        for question in questions:
            tex = template.render(question)
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
