from models.Publication import Publication


class Monograph(Publication):
    def __init__(self, name: str, price_in_uah: int, subject: str):
        super().__init__(name, price_in_uah)
        self.subject = subject

    def __str__(self):
        return f"name of Monograph:{self.name},it's price:{ self.price_in_uah} uah," \
               f" and the subject of it is:{self.subject}"
