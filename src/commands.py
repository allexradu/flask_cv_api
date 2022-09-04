import click
from flask.cli import with_appcontext
from .utils import read_data_from_file
import json


@click.command(name = 'show_cv')
@with_appcontext
def show_cv():
    data = read_data_from_file()
    print(json.dumps(data['cv'], indent = 4))
