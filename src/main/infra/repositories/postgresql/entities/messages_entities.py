from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Date


from src.main.infra.repositories.postgresql.settings.base import Base


class Messages(Base):
    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    age = Column(
        Integer,
        nullable=False
    )

    value = Column(
        Float,
        nullable=False
    )

    date = Column(
        Date,
        nullable=False
    )

    key_pix = Column(
        String,
        nullable=False
    )

    source = Column(
        String,
        nullable=False
    )

    to = Column(
        String,
        nullable=False
    )

    subject = Column(
        String,
        nullable=False
    )

    body = Column(
        String,
        nullable=False
    )

    phone_numbers = Column(
        String,
        nullable=False
    )

    def __repr__(self):
        return f"""
Messages [
    id={self.id}
    name={self.name}
    age={self.age}
    value={self.value}
    date={self.date}
    key_pix={self.key_pix}
    source={self.source}
    to={self.to}
    subject={self.subject}
    body={self.body}
    phone_numbers={self.phone_numbers}
]        
"""
