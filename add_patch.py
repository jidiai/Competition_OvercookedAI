import os
import click
import shutil
import argparse

import overcooked_ai_py


def do_cp(file_path, local_path, force=False):
    file_path = os.path.abspath(os.path.join(overcooked_ai_py.__file__, f"../{file_path}"))
    local_home = os.path.abspath(os.path.join(__file__, f"../{local_path}"))

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Package not found: {file_path}")

    assert os.path.exists(local_home), local_home

    if not force and not (click.confirm(f"This will replace \n {file_path} \n with : \n {local_home}", default=True)):
        return

    shutil.copy(local_home, file_path)

    print('Success')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Add soup cooking restriction")
    parser.add_argument(
        "--force", "-f", action="store_true", help="force")
    args = parser.parse_args()

    do_cp('mdp/overcooked_mdp.py', 'game_core_patch/overcooked_mdp.py', force=args.force)
    print('Finish cp')