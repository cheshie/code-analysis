import ast
import bandit
from bandit.core import test_properties as test
from bandit.core.issue import Cwe

@test.checks("Call")
@test.test_id("B1337")
def main_check(context):
  for arg in context.node.args:
    if isinstance(arg, ast.Name):
      return bandit.Issue(severity=bandit.LOW, text=f"Function: {context.call_function_name_qual}, Argument: {arg.id}")