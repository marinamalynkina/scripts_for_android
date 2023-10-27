import re

def extract_test_name(line):
    pattern = r"\[TestEventLogger\] (.*?) (STARTED|PASSED|FAILED|SKIPPED)"
    match = re.search(pattern, line)
    if match:
        return match.group(1)
    else:
        return None