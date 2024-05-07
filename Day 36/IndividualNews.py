from dotenv import dotenv_values


class IndividualNews:
    def __init__(self, source: str, author: str, title: str, url: str, publication, description: str) -> None:

        self.source_name = source
        self.author = author
        self.title = title
        self.url = url
        self.publication_date = publication
        self.description = description
