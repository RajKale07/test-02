# MVC Example
class Model:
    def __init__(self):
        self.data = "Hello from Model"

class View:
    def render(self, data):
        print(f"View: {data}")

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        self.view.render(self.model.data)

if __name__ == "__main__":
    c = Controller()
    c.run()
