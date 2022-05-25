from models.Publication import Publication


class Magazine(Publication):
    def __init__(self, name: str, price_in_uah: int, topic: str):
        super().__init__(name, price_in_uah)
        self.topic = topic

    def __str__(self):
        return f"name of Magazine:{self.name},it's price:{ self.price_in_uah} uah, and it's about: {self.topic}"
