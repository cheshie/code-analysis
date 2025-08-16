import ast
import bandit
from bandit.core import test_properties as test
from bandit.core.issue import Cwe

@test.checks("ImportFrom")
@test.test_id("B1337")
def main_check(context):
  print(dir(context))
  return bandit.Issue(severity=bandit.LOW, text=f"Imports:: {[alias.name for alias in context.node.names]} from {context.node.module}")