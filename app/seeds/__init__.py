from flask.cli import AppGroup
from .loans import seed_loans, undo_loans

seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    # Add other seed functions here
    seed_loans()

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_loans()

@seed_commands.command('reset')
def reset():
    """
    `flask seed reset` unseeds all of the data and then reseeds
    """
    undo_loans()
    seed_loans()
