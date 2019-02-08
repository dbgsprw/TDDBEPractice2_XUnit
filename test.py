from xunit.test_case import TestCase, WasRun


class TestCaseTest(TestCase):

    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert test.log == 'setup test_method teardown '


TestCaseTest('test_template_method').run()
