# code-analysis
Supporting materials for presentation about fundamentals of security research focusing on static code analysis. 

## Key takeways
* Basic concepts related to vulnerability research
* Software analysis fundamentals 
* Static analysis tools

## Prerequisites 
- [ ] Set up a linux VM to use in exercises
- [ ] Set up virtual environment
```
$ cd ~/Documents
$ python3 -m venv bvenv
$ source bvebv/bin/activate
```
- [ ] Install [Bandit](https://bandit.readthedocs.io/en/latest/start.html),
  - Install from PIP: `pip install bandit`
  - Run `bandit --version` to note installed version. Presentation is prepared using the following environment: 
```
bandit 1.8.6
python version = 3.13.3
```
- [ ] Download this repository to follow exercises in the tutorial

## Exercises
This section contains interactive examples and exercises to be run during the session.

<details> 
  <summary>Example: Click on this exercise to reveal answer.</summary>
   Example Answer: Answer itself.
</details>

### Create AST of Hello World script
The `get_ast.py` script takes 1 cmd parameter, path to script.
Use it to list AST nodes in `Exercises/ex1.py`. 
<details> 
  <summary>Q1: What is the name of AST node type on line 3?</summary>
   A1: Assign
</details>
<details> 
  <summary>Q2: What AST node is the value of AST node from Q1?</summary>
   A2: ListComp
</details>
<details> 
  <summary>Q3: There is expression on line 4 (AST node is Expr) that has certain object as a `value` attribute. Provide type of this object, its id and id of its first argument. </summary>
   A3: Call -> print -> len
</details>

### Run Bandit plugin against vulnerable code
Use Bandit to identify security issues in `ex2.py` using default plugins. Suggestion: use `-f custom` parameter to keep output concise.

<details> 
  <summary>Q4: How many vulnerabilities were detected in ex2.py file? Provide plugin IDs that returned issue. </summary>
   A4: B101, B608, B201
</details>

Now, run it against `ex3.py`. How many issues were reported?

### Building own plugin
To create first plugin, create file `test.py` with contents of "Complete empty plugin file" section in [Bandit - cheatsheet](Bandit - cheatsheet.md). Comment out this line for now: 
```py
@test.checks("<AST TYPE>")
```
Also adjust test ID to arbitrary number, however it cannot duplicate any of existing plugins: 
```py
@test.test_id("B1337")
```

Unfortunately, there is no easy way to add bandit plugins. They must be installed just like a separate Python module.
In order to install Bandit plugin, a Python module must be created. Create a nested folder `plugin_test`:
```
mkdir -p plugin_test/plugin_test
```
To follow Python module structure, `__init__.py` and `setup.py` must be added, and plugin file `test.py` moved to nested folder: 
```
touch plugin_test/plugin_test/__init__.py
touch plugin_test/setup.py
mv test.py plugin_test/plugin_test/
```

Edit `setup.py` to reflect contents of this new plugin: 
```py
from setuptools import setup

setup(
    name='plugin_test',
    version='0.0.1',
    description='Custom bandit plugin to ...',
    url='',
    packages=['plugin_test'],
    author='',
    install_requires=[
        'bandit',
    ],
    entry_points={
        'bandit.plugins': [
            'os_getcwd = plugin_test.test:main_check',
        ],
    }
)
```

Finally, install the plugin using this command:
```
(bvenv)$ python -m pip install ./plugin_test
```

Check if plugin is installed - notice "cli include tests" below which informs user about loaded plugins. Run the tests for `ex3.py`:
```
$ bandit -r ex3.py -t B1337 --format custom
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: B1337
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.13.3
```

In order to avoid installing the plugin again after each change, modify this file instead (your Python version might be different):
```
bvenv/lib/python3.13/site-packages/plugin_test/test.py
```

First step to discover vulnerability is to understand application under analysis. Adjust this plugin to return issue for all function calls thorough the file `ex3.py`

<details> 
  <summary>Q5: How many function calls are present in the file? </summary>
   A5: 17 (see Solutions/q5.py)
</details>

In a complex project, this would return large number of results. In order to limit results to potentially interesting calls, include only those that contain variable as an argument. Run tests against `ex3.py`.

<details> 
  <summary>Q6: How many function with variable arguments are in the file? </summary>
   A6: 8 (see Solutions/q6.py)
</details>

Again, even this result could be very large in a complex codebase. Any potential ideas to further eliminate non-interesting results could either lead to findings, or worse - exclude them. Consider some of the following ways: 
* Exclude any built in functions
* Include only imported names
* Include functions with arguments that come from specific input functions (i.e., to track variable to its source - unfortunately, not possible easily in Bandit, since it is missing taint tracking capabilities)

<details> 
  <summary>Q7: Adding to previous conditions, find only imported variables. What variable names did our plugin find?</summary>
   A7: argv, join
</details>

With list of imported names from modules, next action is to understand how these functions work. Starting with `os.path.join`, primary source of information as official documentation (https://docs.python.org/3/library/os.path.html#os.path.join): 
> If a segment is an absolute path (which on Windows requires both a drive and a root), then all previous segments are ignored and joining continues from the absolute path segment.

It seems that if last provided argument is variable, then attacker might provide path starting with slash (`'/...'`) and the function will ignore all previous path elements, thus allowing function to access arbitrary locations on the filesystem. 

Final step would be then to write complete query to identify the culprit.

<details> 
  <summary>Q8: Considering previous exercises, write a complete plugin to detect call to os.path.join with last positional argument controlled by user.</summary>
   A8: Complete plugin script
</details>