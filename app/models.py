class Task:
    def __init__(self, id, title, date_of_creation):
        self.id = id
        self.title = title
        self.date_of_creation = date_of_creation
        self.done = False

    def mark_as_done(self):
        self.done = True

    def modify_title(self, new_title):
        self.title = new_title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'date_of_creation': self.date_of_creation,
            'done': self.done
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            date_of_creation=data.get('date_of_creation')
        )
