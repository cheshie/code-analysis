import ast
import bandit
from bandit.core import test_properties as test
from bandit.core.issue import Cwe

@test.checks("Call")
@test.test_id("B1337")
def main_check(context):
  if True:
    return bandit.Issue(
      severity=bandit.LOW, 
      text=f"Function name: {context.call_function_name_qual}")