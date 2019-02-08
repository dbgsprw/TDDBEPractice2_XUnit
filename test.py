from xunit.test_case import TestCase, WasRun


class TestCaseTest(TestCase):

    def setup(self):
        self.test = WasRun('test_method')

    def test_setup(self):
        self.test.run()
        assert self.test.log == 'setup test_method teardown '

    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert test.log == 'setup test_method teardown '

    def test_result(self):
        test = WasRun('test_method')
        result = test.run()
        assert '1 run, 0 failed' == result.summary()
        
    def test_failed_result(self):
        test = WasRun('test_broken_method')
        result = test.run()
        assert '1 run, 1 failed' == result.summary()


TestCaseTest('test_setup').run()
TestCaseTest('test_template_method').run()
TestCaseTest('test_result').run()
TestCaseTest('test_failed_result').run()

