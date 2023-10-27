import utils

with open('plan-4457277571-RUTO-3.log', 'r') as f:
    lines = f.readlines()

started_tests = []
failed_tests = []
skipped_tests = []
test_count = 0

for index, line in enumerate(lines):
    if "[TestEventLogger]" in line and '>' in line:
        test_name = utils.extract_test_name(line)
        if " STARTED" in line:
            started_tests.append(test_name)
            test_count +=1
        elif " PASSED" in line:
            if test_name in started_tests:
                started_tests.remove(test_name)
        elif " FAILED" in line:
            if test_name in started_tests:
                started_tests.remove(test_name)
            failed_tests.append(test_name)
        elif " SKIPPED" in line:
            if test_name in started_tests:
                started_tests.remove(test_name)
            skipped_tests.append(test_name)


print(f"Number of tests read: {test_count}")
print(f"Number of failed tests: {len(failed_tests)}")
print(f"Failed tests: \n")
print('\n'.join(map(str, failed_tests)))
print(f"Number of Skipped tests: {len(skipped_tests)}")
print(f"Skipped tests: ")
print('\n'.join(map(str, skipped_tests)))
print(f"Number of not finished tests: {len(started_tests)}")
print(f"Not finished tests: ")
print('\n'.join(map(str, started_tests)))
started_tests.clear()
failed_tests.clear()
skipped_tests.clear()




