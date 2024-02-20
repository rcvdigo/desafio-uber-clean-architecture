from dataclasses import dataclass

@dataclass
class EmailRequest:
    to: str
    subject: str
    body: str
