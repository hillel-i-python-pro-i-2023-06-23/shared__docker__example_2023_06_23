import csv
import logging
import pathlib

from app.config import FILES_OUTPUT_DIR
from app.loggers.loggers import get_custom_logger
from app.services.generate_users import generate_users, User


def read_csv_with_users(csv_file_path: pathlib.Path) -> list[User]:
    logger = get_custom_logger(__name__)

    with csv_file_path.open("r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        users = [User.from_raw_dict(row) for row in csv_reader]

    logger.info(f"csv file with users is read: {csv_file_path.as_uri()}")
    return users


def generate_csv_with_users(amount: int = 100, csv_file_path: pathlib.Path = None) -> pathlib.Path:
    logger = get_custom_logger(__name__)
    # logger = get_core_logger()

    if csv_file_path is None:
        csv_file_path = FILES_OUTPUT_DIR.joinpath("users.csv")
        logger.info(f"csv_file_path is None. Use default value: {csv_file_path.as_uri()}")

    with csv_file_path.open("w") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=User.get_fieldnames())
        _generate_to_file(logger=logger, csv_writer=csv_writer, amount=amount)

    logger.info(f"csv file with users is generated: {csv_file_path.as_uri()}")
    return csv_file_path


def _generate_to_file(logger: logging.Logger, csv_writer: csv.DictWriter, amount: int):
    logger.info("start generating csv file with users")
    csv_writer.writeheader()

    users_generator = generate_users(amount=amount)
    for index, user in enumerate(users_generator, start=1):
        csv_writer.writerow(user.get_dict())
        logger.info(f"write user {index}/{amount} to csv file")

    logger.info("end generating csv file with users")
