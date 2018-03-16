class UI:
    
    def __init__(self, elements):
        self.elements = elements
        pass

    def update(self, ms):
        for e in elements:
            e.update(ms)

    def draw(self, tb):
        for e in elements:
            e.draw(tb)

