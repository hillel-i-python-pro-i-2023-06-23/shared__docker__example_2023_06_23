import pathlib

from app.config import FILES_INPUT_DIR
from app.services.generate_csv_with_users import read_csv_with_users
from app.services.save_users_to_json import save_users_to_json
from app.services.save_users_to_yaml import save_users_to_yaml


def convert_file(path: pathlib.Path = None):
    if path is None:
        path = FILES_INPUT_DIR.joinpath("users.csv")

    users = read_csv_with_users(csv_file_path=path)

    save_users_to_json(users=users)

    save_users_to_yaml(users=users)
