import datetime
from dataclasses import dataclass
from dataclass_wizard import JSONWizard

@dataclass(frozen=True)
class Event(JSONWizard):
    description: str
    timezone: str
    location: str
    day: int
    month: int
    year: int
    dweek: str
    start: str
    end: str

    def format_date(self):
        return datetime.date(self.year, self.month, self.day)

    def __str__(self):
        return f'Event: {self.description}, Timezone: {self.timezone}, Location: {self.location}, Date: {self.year}/{self.month}/{self.day}, Weekday: {self.dweek}, Time: {self.start}-{self.end}'

    def __repr__(self):
        return f'Event: {self.description}, Timezone: {self.timezone}, Location: {self.location}, Date: {self.year}/{self.month}/{self.day}, Weekday: {self.dweek}, Time: {self.start}-{self.end}'
