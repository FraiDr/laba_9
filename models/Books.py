from models.Publication import Publication


class Books(Publication):
    def __init__(self, author: str, name: str, price_in_uah: int, page_count: int, genre: str):
        self.author = author
        super().__init__(name, price_in_uah)
        self.page_count = page_count
        self.genre = genre

    def __str__(self):
        return f"name of Book:{self.name},it's price:{self.price_in_uah} uah," \
               f" count of page is: {self.page_count} , and it's written in {self.genre} genre"
