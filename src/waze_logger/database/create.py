"""module used for the creation of the database on setup"""

from sqlalchemy import (
    Engine,
    Text,
    Column,
    String,
    DECIMAL,
    Integer,
    CheckConstraint,
    UniqueConstraint,
    Table,
    MetaData
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_database(engine: Engine, force: bool = False):

    with engine.connect() as connection:

        meta_data = MetaData()

        statement = Text("CREATE DATABASE waze_logger;")
        connection.execute(statement)
        connection.commit()

    location = Table(
        "location", meta_data,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", String(32), nullable=False),
        Column("latitude", DECIMAL(8, 5), nullable=False),
        Column("longitude", DECIMAL(7, 5), nullable=False),
        UniqueConstraint("latitude", "longitude", name="unique_location"),
        CheckConstraint(
            "latitude >= -180 AND latitude <= 180",
            name="latitude_scope"
        ),
        CheckConstraint(
            "longitude >= -90 AND longitude <= 90",
            name="longitude_scope"
        ),
    )

    route = Table(
        "route", meta_data,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", String(32)),
        Column("origin", Integer,)
    )
