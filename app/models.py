class Task:
    def __init__(self, id, title, creation_date):
        self.id = id
        self.title = title
        self.creation_date = creation_date
        self.done = False

    def mark_as_done(self):
        self.done = True

    def modify_title(self, new_title):
        self.title = new_title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'creation_date': self.creation_date,
            'done': self.done
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            creation_date=data.get('creation_date')
        )
