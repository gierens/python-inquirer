import os
import sys
import re
sys.path.append(os.path.realpath('.'))
from pprint import pprint

import inquirer

def initials(answers):
  return 'Are these your initials? {}{}'.format(answers['name'][0], answers['surname'][0])

questions = [
    inquirer.Text('name',
                  message="What's your name?"),
    inquirer.Text('surname',
                  message="{name}, what's your surname?"),
    inquirer.Text('alias',
                  message="What's your Alias [{name}]",
                  default="{surname}"),
    inquirer.Confirm('initials',
                  message=initials,
                  default=True),
]

answers = inquirer.prompt(questions)

pprint(answers)
