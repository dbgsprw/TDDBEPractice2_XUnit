class TestResult:
    def __init__(self):
        self.run_count = 0
        self.failure_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.failure_count += 1

    def summary(self):
        return "{} run, {} failed".format(self.run_count, self.failure_count)


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self, result):
        result.test_started()
        self.setup()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
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
