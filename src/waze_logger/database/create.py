"""module used for the creation of the database on setup"""

import json

from sqlalchemy import (
    Engine,
    Text,
    Column,
    String,
    DECIMAL,
    Integer,
    CheckConstraint,
    UniqueConstraint,
    ForeignKey,
    PrimaryKeyConstraint,
    Table,
    MetaData,
    DateTime
)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_database(engine: Engine, force: bool = False):

    meta_data = MetaData()

    Table(
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

    Table(
        "route", meta_data,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("origin", ForeignKey("location.id"), nullable=False),
        Column("destination", ForeignKey("location.id"), nullable=False),
        UniqueConstraint("origin", "destination", name="unique_route")
    )

    Table(
        "route_duration", meta_data,
        Column("logged_time", DateTime),
        Column("route", ForeignKey("route.id")),
        Column("trip_duration", Integer),
        PrimaryKeyConstraint("logged_time", "route", name="route_duration_pk"),
    )

    meta_data.create_all(engine)
