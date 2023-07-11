from app.loggers.loggers import get_core_logger


def func_with_error(a: int, b: int) -> int | None:
    logger = get_core_logger()

    logger.info("start")

    try:
        result = a / b
    except ZeroDivisionError as exc:
        # logger.warning(f'Zero division error: {a=}, {b=}')
        logger.exception(exc)
        result = None

    logger.info("finish")

    return result
