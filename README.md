# code-analysis
Supporting materials for presentation about fundamentals of security research focusing on static code analysis. 
(in progress)

## Key takeways
* Basic concepts related to vulnerability research
* Software analysis fundamentals 
* Security analysis tools

## Prerequisites 
- [ ] Set up a linux VM to use in exercises,
- [ ] Install [CodeQL inside VSCode](https://docs.github.com/en/code-security/codeql-for-vs-code) and [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli)\*
  - Install VSCode extension from [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-codeql)
  - Download CodeQL CLI binary for your architecture - from https://github.com/github/codeql-cli-binaries/releases/
  - Put `codeql` in your PATH
  - Run `codeql resolve languages` to list supported languages for analysis. (Should include Python)
- [ ] Install [Bandit](https://bandit.readthedocs.io/en/latest/start.html),
  - Install from PIP: `pip install bandit`
  - Run `bandit --version` to get installed version.
- [ ] Install [Nuclei](https://github.com/projectdiscovery/nuclei),
  - Download Nuclei binary for your achitecture - from https://github.com/projectdiscovery/nuclei/releases
  - Put `nuclei` in your PATH
  - Run `nuclei --version` to get installed version. It will install templates on first launch.
- [ ] Download this repo for example vulnerable Python library to follow exercises in tutorial.

\* Optionally you can use [Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) in either VSCode or a browser and issue CodeQL queries online. 
