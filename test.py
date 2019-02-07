from xunit.was_run import WasRun

test = WasRun("testMethod")

print(test.was_run)

test.test_method()

print(test.was_run)
