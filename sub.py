#!/usr/bin/env python3

"""
    Replace in files with confirm
"""

import os
import questionary
import shutil
from ripgrepy import Ripgrepy
from typer import Typer
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.shortcuts import print_formatted_text
from collections import namedtuple, defaultdict

app = Typer(add_completion=False)
Match = namedtuple('Match', 'filename lineno line submatches')


def rg(needle, path):
    result = Ripgrepy(needle, path).with_filename().line_number().json().run()
    datas = [x['data'] for x in result.as_dict]
    results = []
    for data in datas:
        texter = lambda x, y: x[y].get('text') or x[y].get('bytes')
        m = Match(texter(data, 'path'), data['line_number'], texter(data, 'lines'), data['submatches'])
        results.append(m)
    return results

def fprint(filename, lineno, line, idx, start, end):
    linelen = len(line)
    print_formatted_text(FormattedText([
        ("", "\n"),
        ("bold", filename),
        ("", "\n"),
        ("", f"{lineno:>06}:"),
        ("", line[idx:start]),
        ("yellow", line[start:end]),
        (("", line[end:linelen].rstrip()) if end and idx != linelen else ("", "")),
    ]))

def ask(replacement):
    return questionary.text(
        "(n)ext/next (f)ile/(r)eplace/replace (a)ll/(q)uit >",
        validate=lambda text: not text or text in 'nfraq',
        qmark=f'Replace with "{replacement}"?',
    ).ask()

def ask_loop(needle, replacement, path):

    actions = defaultdict(lambda: defaultdict(list))
    jump_to_nextfile = False
    last_filename = None
    replace_all = False
    result = None

    for filename, lineno, line, submatches in rg(needle, path):
        if last_filename and jump_to_nextfile and last_filename == filename:
            continue
        jump_to_nextfile, last_filename = False, filename
        idx = end = 0
        for start, end in [(x['start'], x['end']) for x in submatches]:
            if not replace_all:
                fprint(filename, lineno, line, idx, start, end)
                result = ask(replacement)
            match result:
                case 'f':
                    jump_to_nextfile = True
                case 'r' | 'a':
                    actions[filename][lineno] += [(start, end)]
                    replace_all = (result == 'a')
                case 'q' | None:
                    return actions
            idx = end
    return actions


@app.command()
def sub(needle, replacement, path='.'):
    actions = ask_loop(needle, replacement, path)
    for filename, offset_dict in actions.items():
        with open(filename, "r", encoding="utf-8") as infile:
            with open(filename + '.new', "w", encoding="utf-8") as outfile:
                for i, line in enumerate(infile.readlines(), start=1):
                    newline = ""
                    if i in offset_dict:
                        idx = 0
                        for start, end in offset_dict[i]:
                            newline += line[idx:start] + replacement
                            idx = end
                        if idx < len(line):
                            newline += line[idx:]
                        outfile.write(newline)
                    else:
                        outfile.write(line)
        shutil.move(filename, f"{filename}.bak")
        shutil.move(f"{filename}.new", filename)
        os.remove(f"{filename}.bak")

app()
