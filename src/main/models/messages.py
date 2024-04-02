from datetime import date


class Messages:
    def __init__(self,
                 id: str,
                 name: str,
                 age: int,
                 value: float,
                 date: date,
                 key_pix: str,
                 source: str,
                 to: str,
                 subject: str,
                 body: str,
                 phone_numbers: str
                 ) -> None:
        self.id=id
        self.name=name
        self.age=age
        self.value=value
        self.date=date
        self.key_pix=key_pix
        self.source=source
        self.to=to
        self.subject=subject
        self.body=body
        self.phone_numbers=phone_numbers
