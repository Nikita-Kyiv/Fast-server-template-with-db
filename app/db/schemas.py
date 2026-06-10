from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger


class models(DeclarativeBase):
    pass


# This file contains the SQLAlchemy models for the database schemas. 
# These models are used to define the structure of the data that will be stored in the database
# and to validate the data before it is saved.
# example:
# class profile(models):
#     __tablename__ = "profile"
#     id: Mapped[int] = mapped_column(
#         type_=BigInteger, primary_key=True, nullable=False, unique=True
#     )
#     role: Mapped[str] = mapped_column(nullable=False)
#     name: Mapped[str] = mapped_column(nullable=False)
#     email: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
#     password: Mapped[str] = mapped_column(nullable=False)
#     subscribed: Mapped[int] = mapped_column(nullable=False, default=False)
#     title: Mapped[str] = mapped_column(nullable=True)
#     skills: Mapped[str] = mapped_column(nullable=True)
#     portfolio: Mapped[str] = mapped_column(nullable=True)
#     company: Mapped[str] = mapped_column(nullable=True)
#     website: Mapped[str] = mapped_column(nullable=True)
#     avatar: Mapped[str] = mapped_column(nullable=True)
