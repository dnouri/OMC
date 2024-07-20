import click


@click.group()
def group():
    pass


if __name__ == '__main__':
    group(standalone_mode=False)
