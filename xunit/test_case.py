class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setup()
        method = getattr(self, self.name)
        method()
        self.teardown()

    def setup(self):
        pass

    def teardown(self):
        pass


class WasRun(TestCase):

    def __init__(self, name):
        self.was_run = False
        TestCase.__init__(self, name)

    def setup(self):
        self.was_run = False
        self.log = 'setup '

    def test_method(self):
        self.was_run = True
        self.log = self.log + "test_method "

    def teardown(self):
        self.log = self.log + "teardown "
