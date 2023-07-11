from typing import NamedTuple
from collections.abc import Iterator

from app.loggers.loggers import get_core_logger
from app.services.faker_instance import faker


class User(NamedTuple):
    username: str
    password: str
    email: str
    age: int = 18

    def get_dict(self) -> dict:
        return self._asdict()

    @classmethod
    def get_fieldnames(cls) -> list[str]:
        return list(cls._fields)

    @classmethod
    def from_raw_dict(cls, raw_data: dict) -> "User":
        return cls(
            username=raw_data["username"],
            password=raw_data["password"],
            email=raw_data["email"],
            age=int(raw_data["age"]),
        )


def generate_user() -> User:
    return User(
        username=faker.user_name(),
        password=faker.password(),
        email=faker.email(),
        age=faker.pyint(min_value=18, max_value=100),
    )


def generate_users(amount: int) -> Iterator[User]:
    logger = get_core_logger()

    logger.debug(msg="generate_users.start")

    for index in range(1, amount + 1):
        logger.debug(f"generate_users.iteration.{index}/{amount}")
        yield generate_user()

    logger.debug("generate_users.end")
