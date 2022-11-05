import logging

from app.db.init_db_dev import init_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial DEV data")
    init()
    logger.info("Initial DEV data created")


if __name__ == "__main__":
    main()
