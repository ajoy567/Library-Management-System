class User:
    def __init__(self, first_name, last_name, member_id):
        self.first_name = first_name
        self.last_name = last_name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"User: {self.first_name} {self.last_name} (Books Borrowed : {len(self.borrowed_books)})"