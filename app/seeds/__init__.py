from flask.cli import AppGroup

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    # Add other seed functions here
    pass

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    # Add other undo functions here
    pass

def reset():
    """
    `flask seed reset` unseeds all of the data and then reseeds
    """
    # Add more undo functions here
    pass
    #add more seed functions here
