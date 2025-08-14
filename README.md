# code-analysis
Supporting materials for presentation about fundamentals of security research focusing on static code analysis. 
(in progress)

## Key takeways
* Basic concepts related to vulnerability research
* Software analysis fundamentals 
* Security analysis tools

## Prerequisites 
- [ ] Set up a linux VM to use in exercises,
- [ ] Set up virtual environment
```
$ cd ~/Documents
$ python3 -m venv bandit-venv
$ source bandit-venv/bin/activate
```
- [ ] Install [Bandit](https://bandit.readthedocs.io/en/latest/start.html),
  - Install from PIP: `pip install bandit`
  - Run `bandit --version` to get installed version.
- [ ] Download this repo for example vulnerable Python library to follow exercises in tutorial.

## Exercises
This section contains interactive examples and exercises to be run during the session.

### Create AST of Hello World script


\* Optionally you can use [Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) in either VSCode or a browser and issue CodeQL queries online. 
