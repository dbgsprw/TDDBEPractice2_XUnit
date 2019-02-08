class TestResult:
    def __init__(self):
        self.run_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self):
        return f"{self.run_count} run, 0 failed"


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        result = TestResult()
        result.test_started()
        self.setup()
        method = getattr(self, self.name)
        method()
        self.teardown()
        return result

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

    def test_broken_method(self):
        raise Exception
