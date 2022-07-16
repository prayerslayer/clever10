# CLEVER10

Custom cards for [Piatnik's Smart 10](https://www.piatnik.com/spiele/marken/smart-10/smart-10) quiz game! [DEMO](demo.pdf)

**CAVEATS**

* Obviously not an official project by Piatnik


## Installation

Clone this project.

## Data Entry

Your questions go into a file `questions.txt`. A question consists of:

* 1 question text (goes into the large circle in the center)
* 10 options (go around the large circle)
* 10 answers (go around the options and are hidden as per game mechanics)

### Questions Format

Describe a question in the following format in the file:

```
# This is a comment, the line will be ignored.
# Empty lines are skipped.

This is the question text.
Answer1;Option1
Answer2;Option2
Answer3;Option3
Answer4;Option4
Answer5;Option5
Answer6;Option6
Answer7;Option7
Answer8;Option8
Answer9;Option9
Answer10;Option10
```

As you can see, the first line is the question and the 10 following lines are option/answer pairs separated by a semicolon `;`. Hence, 11 consecutive non-empty lines in the file will be interpreted as one question. Don't worry about shuffling answers or questions, the card generation code will do that for you.

The typesetting is done by LaTeX, so whatever you write as question text, option or answer will be in the end copied into a larger LaTeX file and compiled. This means that on the one hand, you can go crazy with, e.g., formulae: `$e=mc^2$` will work just fine. On the other hand, take care to escape special LaTeX characters with a backslash, like, e.g., `\&`, `\%`, etc. clever10 includes a command `find-bad-chars` which prints all questions with special LaTeX characters.

### Answer/Option Types

Clever10 supports some special non-text answer/option types. These are currently images (`[img:PATH]`) and colors (`[color:HEXCODE]`).

To use images for options or answers place them in the `images` folder and reference them with `[img:FILENAME_WITHOUT_EXTENSION]`. Images will be cropped by an appropriately-sized circle. Incidentally, this is also how the true/false question type works.

To use colors reference them with `[color:HEXCODE]`, where `HEXCODE` is, e.g., `ff0000` for red.

### Question Categories

Clever10 supports categories of questions, i.e., groups of differently formatted questions. The exact format differences are called a "context". A context is specified by a special string between two questions in `questions.txt`. Specifically, `key:value` pairs in curly brackets. Currently only the color of the circle (as [`dvipsnames` color names](https://www.overleaf.com/learn/latex/Using_colours_in_LaTeX)) is supported, e.g., `{color:MidnightBlue}`.

## Generating the Cards

1. `pip3 install -r requirements.txt` (installs dependencies)
2. `python3 clever10.py generate-cards`
3. Take `main.tex`, `content.tex` and the `images` folder, upload them to [Overleaf](https://overleaf.com) and download PDF. Or alternatively, compile `main.tex` on your own system (`pdflatex main && pdflatex main` if you have all dependencies installed).

## License

MIT

