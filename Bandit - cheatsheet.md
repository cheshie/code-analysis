# Bandit - cheatsheet

Specify file to scan
```
bandit file.py
```

Specify a severity level threshold to filter out low-severity issues
```
bandit file.py -s MEDIUM
```

Scan all the python files which is inside given directory (recursively)
```
bandit -r /path/to/source/root
```

Run custom check: 
```
bandit file.py -t B703
```

Use only the plugins listed in the *ShellInjection* profile:
```
bandit file.py -p ShellInjection
```

Custom/concise output format
```
bandit file.py --format custom
```

Compare test results against baseline (in JSON)
```
bandit file.py -b test_results.json
```

## Bandit - snippets 

### Complete empty plugin file
```py
r"""
============================
B###: Test for vulnerability
============================

...
"""
import ast
import bandit
from bandit.core import test_properties as test
from bandit.core.issue import Cwe

@test.checks("Call")
@test.test_id("B1337")
def main_check(context):
  print(context)
  print(dir(context))
  if False:
    return bandit.Issue(
                severity=bandit.LOW,
                confidence=bandit.LOW,
                cwe=Cwe.NOTSET,
                text=f"Vulnerability detected.")
```

### Return Issue
```py
return bandit.Issue(
            severity=bandit.MEDIUM,
            confidence=(
                bandit.MEDIUM
                if ...
                else bandit.LOW
            ),
            cwe=issue.Cwe.SQL_INJECTION,
            text="Vulnerability is in ...",
        )
```

### Get value for function argument
```python
context.check_call_arg_value("<arg>", "<val>")
```

### Access underlying AST object
```
context.node
```

### Function name (equal to Call.func.id)
```py
context.call_function_name
```

### Access function arguments
```py
# list of strings - argument IDs
context.call_args
# access argument objects directly
context.node.args
```

### Get function qualified name
```
context.call_function_name_qual
```

### Check for imports
```py
context.is_module_imported_like("<module>")
# OR
context.is_module_imported_exact("<module>")
```

### Provide line number of specific function
# In case the call is split over multiple lines, 
# get the correct one for the argument.
```py
bandit.Issue( ...
    lineno=context.get_lineno_for_call_arg("<arg name>")
)
```