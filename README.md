# CLEVER10

Custom cards for [Piatnik's Smart 10](https://www.piatnik.com/spiele/marken/smart-10/smart-10) quiz game! [DEMO](demo.pdf)

So, is this Very Easy? The answer is: Maybe?! This project alleviates only the problem of card layout (to some extent, see below). You still have the problems of content creation (someone needs to come up with questions and answer options) and card production (printing, cutting).

**CAVEATS**

* Obviously not an official project by Piatnik
* In my one try I didn't get the sizing of the cards 100% right

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


## Production

### Printing

Use heavy paper, around 300 grams/square-meter.

The generated PDF technically allows to be printed double-sided as the original Smart10. Put 2 cards on one DIN A4 page, rotate every 3rd and 4th by 180 degree to make the cut marks align. This is doable, e.g., in Adobe Acrobat. However I could not persuade the printers I've used to print cards _exactly_ behind each other. Not for many pages anyways. Thus I recommend to print one-sided, sadly. (2 per DIN A4 page)

### Cutting

Cutting the cards is some effort but doable with basic equipment. 6 cuts with a swingline paper trimmer and 8 scissor cuts per page (assuming 2 cards per page). You could also pay a person to do this in your local copyshop.

### Packaging

Make a shallow box template at [template maker](https://www.templatemaker.nl/en/shallowbox/) with appropriate dimensions. The cards are 10.5cm x 10.5cm, so a bit more length and height than that. Width (thickness) depends on how many cards you have and the paper weight used. With 100 cards on 300g/m^2 paper you're looking at a staple of around 3 cm.

Ideally you want heavier paper also here to make the box stable.

Alternatively, paper/craft/art shops often sell ready-made boxes. You can't print custom images on them, but they are sturdy.

## License

MIT

