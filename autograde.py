#!/usr/bin/env python3

import click
import os
import json
import re

@click.command()
@click.option("--submission", required=True,  type=click.Path(exists=True), help="Test directory")
@click.option("--results", required=True, type = click.File(mode="w"), help="Where to put results")
def autograde(submission=None, results=None):
    with open(os.path.join(submission, "hello.txt")) as f:
        text = f.read().strip()
        success = re.match("Hello\s+\w+@ucsd.edu!\sThe\ssum\sof\syour\sinputs\sis:\s45", text) is not None

        # https://gradescope-autograders.readthedocs.io/en/latest/specs/#output-format
        json.dump(dict(output="The autograder ran.",
                       visibility="visible",
                       stdout_visibility="visible",
                       tests=[ dict(score=1 if success else 0,
                                    max_score=1,
                                    number="1",
                                    output=text,
                                    tags=[],
                                    visibility="visible",
                       )
                       ]#,
#                       leaderboard=[
 #                          dict(name="goodness", value=1 if success else 0)
                       #               ]
        ), results, sort_keys=True, indent=4)
        
if __name__== "__main__":
    autograde()
