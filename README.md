# code-analysis
Supporting materials for presentation about fundamentals of security research focusing on static code analysis. 
(in progress)

## Key takeways
* Basic concepts related to vulnerability research
* Software analysis fundamentals 
* Security analysis tools

## Prerequisites 
- [ ] Set up a linux VM to use in exercises
- [ ] Set up virtual environment
```
$ cd ~/Documents
$ python3 -m venv bandit-venv
$ source bandit-venv/bin/activate
```
- [ ] Install [Bandit](https://bandit.readthedocs.io/en/latest/start.html),
  - Install from PIP: `pip install bandit`
  - Install from PIPL `pip install astpretty`
  - Run `bandit --version` to note installed version
- [ ] Download this repo for example vulnerable Python library to follow exercises in tutorial

## Exercises
This section contains interactive examples and exercises to be run during the session.

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
   A2: Call -> print -> len
</details>
