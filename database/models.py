from sqlalchemy import Table, Column, BigInteger, Integer, String, MetaData


metadata_obj = MetaData()


users = Table(
    "users",
    metadata_obj,
    Column("user_id", BigInteger, primary_key=True),
    Column("username", String),
    Column("first_name", String),
    Column("time_start", String),
    Column("chating_user", BigInteger),
    Column("ready", BigInteger, default=0),
    Column("active", BigInteger),
    Column("videonotes_available", Integer)
)