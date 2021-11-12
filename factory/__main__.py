import signal
import argparse
import sys
import os
from pathlib import Path

from ImageGoNord import GoNord

from rich.console import Console
from rich.panel import Panel


def main():
    signal.signal(signal.SIGINT, signal_handler)
    console = Console()
    args = fromCommandArgument(console)

    gruvbox_factory = GoNord()
    gruvbox_factory.reset_palette()

    # Checks if there's an argument
    if len(sys.argv) > 1:
        image_paths = args.images
        add_gruvbox_palette(gruvbox_factory, "doombox")
    else:
        image_paths = fromTui(console)
        add_gruvbox_palette(gruvbox_factory, "doombox")

    for image_path in image_paths:
        if os.path.isfile(image_path):
            process_image(image_path, console, gruvbox_factory)
        else:
            console.print(
                f"❌ [red]We had a problem in the pipeline! \nThe image at '{image_path}' could not be found! \nSkipping... [/]"
            )
            continue


# Gets the file path from the Argument
def fromCommandArgument(console):
    command_parser = argparse.ArgumentParser(
        description="A simple cli to manufacture doombox themed wallpapers.")

    command_parser.add_argument("-i",
                                "--images",
                                nargs="+",
                                type=str,
                                help="path(s) to the image(s).")

    args = command_parser.parse_args()
    return args


# Gets the file path from user input
def fromTui(console):
    console.print(
        Panel("🏭 [bold green] Gruvbox Factory [/] 🏭",
              expand=False,
              border_style="yellow"))

    image_paths = [
        os.path.expanduser(path) for path in console.input(
            "🖼️ [bold yellow]Which image(s) do you want to manufacture? (image paths separated by spaces):[/] "
        ).split()
    ]
    return image_paths


def process_image(image_path, console, gruvbox_factory):
    image = gruvbox_factory.open_image(image_path)

    console.print(
        f"🔨 [yellow]manufacturing '{os.path.basename(image_path)}'...[/]")

    # TODO: might be a better idea to save the new Image in the same directory the command is being run from
    save_path = os.path.join(os.path.dirname(image_path),
                             "doombox_" + os.path.basename(image_path))

    gruvbox_factory.convert_image(image, save_path=(save_path))
    console.print(f"✅ [bold green]Done![/] [green](saved at '{save_path}')[/]")


def add_gruvbox_palette(gruvbox_factory, palette):
    current_path = Path(__file__).parent.absolute()

    with open(str(current_path) + "/" + palette + ".txt", "r") as f:
        for line in f.readlines():
            gruvbox_factory.add_color_to_palette(line[:-1])


## handle CTRL + C
def signal_handler(signal, frame):
    print()
    sys.exit(0)


if __name__ == "__main__":
    main()
