class Post:
    def __init__(self, title: str, subtitle: str, body: str, id: int) -> None:
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body