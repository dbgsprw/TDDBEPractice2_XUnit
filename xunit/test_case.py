class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setup()
        method = getattr(self, self.name)
        method()

    def setup(self):
        pass


class WasRun(TestCase):

    def __init__(self, name):
        self.was_run = False
        TestCase.__init__(self, name)

    def setup(self):
        self.was_run = False
        self.was_setup = True

    def test_method(self):
        self.was_run = True
