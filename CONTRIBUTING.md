# Contributing

## How to participate

1. Assign yourself to an open git issue
    - To suggest a new feature or bugfix:
      - Check it does not already exist first! If it doesn't then:
      - Open github issue
      - Label it accordingly
      - Discuss with project members on discord or through github
2. Create a branch with `<issue-number>-<branch-descriptor>` naming scheme [*(see article)*](https://deepsource.io/blog/git-branch-naming-conventions/)
3. Work on assigned issue
    - Try not to go outside the scope of the git issue
      - discuss with project members if you end up having to implement new features outside of the original scope
4. Sync branch with dev
5. Create remote branch and push to that branch
6. Start the [pull request process](#pull-request=process)

## Git workflow: Issue branch workflow

- Branches are created from issues/ tasks
- Branches have the same name of its issue id#
- One Branch per issue and one issue per branch
- see [article](https://medium.com/flexisaf/git-workflow-for-your-project-3d9dbdc5f8e2)

## Coding Style

*The coding style was inspired by [The Hitchhikers Guide to Python](https://docs.python-guide.org/writing/style/)*

- General Concepts
  - Explicit Code - The most straighforward way of coding is prefered.

        -Bad

        def make_complex(*args):
            x, y = args
            return dict(**locals())

        -Good

        def make_complex(x, y):
            return {'x': x, 'y': y}

  - One Statement per line - While there are some areas where compound statements are allowed it is good practice to only have one statement per line.

        -Bad

            print('one'); print('two')
            if x == 1: print('one')
            if <complex comparison> and <other complex comparison>:# do something

        -Good

            print('one')
            print('two')

            if x == 1:
            print('one')

            cond1 = <complex comparison>
            cond2 = <other complex comparison>
            if cond1 and cond2:
            # do something

  - Do your best to try and keep you code concise and clean so it is readable to everyone. For more detailed examples or if you are unsure about something please refer to the documentation linked above or reach out to one of us.

## Development Environment Setup

### Instuctions for Windows in VS Code

- Create virtual environment
  - `python -m venv .venv`
- Add path to python interpreter from new virtual environment to IDE
  - Open command palette: `CTRL-SHIFT-P`
  - Type and select `Python: Select Interpreter` option
  - Select `python.exe` file inside the `venv` folder
  - Close terminal and relaunch
  - Verify `venv` is activated by seeing `(.venv)` prompt in terminal
- Install project dependencies
  - `pip install -r requirements.txt`
- Setup pre-commit hook
  - `pre-commit install`

### Instructions for Linux/ MacOS in VS Code

- Check to see if python is installed
  - Open a new terminal if one is not already present
  - Enter in terminal `python3 --version`
  - If that dosn't work try `python --version`
  - If you have python 2, or are missing python you will need to download and follow instructions from [Python.org](https://www.python.org/downloads/)

- Create a virtual enviroment
  - Create directory with `mkdir myproject`
  - Change into that directory or folder name `cd myproject`
  - Create virtual environment using `python3 -m venv venv`
  - Activate the enviroment with `.venv/bin/activate`

### Using Git to make a pull request

- Instructions on [Sachinsf.com](https://www.sachinsf.com/how-to-push-the-code-from-vs-code-to-github/)
  - Make sure you have git installed on your PC, and that all the files you are pushing are in one folder before you push any changes

### Running app

This app can be run by typing `python3 main.py` or `python main.py` in your terminal.  Since Tkinter is included with the basic Python installation, no additional libraries or frameworks are required to be downloaded via the Python package installer (pip).
  
### Resources

- Currently, this project uses Tkinter for its GUI.  This decision was made due to the popularity of Tkinter, the large amount of available resources, and the fact that Tkinter comes installed with a standard Python installation.  In the future, this project may apply Tkinter themes or design modules to createa  more modern design look.  There are myriad resources for using Tkinter available online:
  - [Official Tkinter Documentation](https://docs.python.org/3/library/tk.html)
  - [TK Docs Guide](https://tkdocs.com/)
  - [Real Python Guide to Tkinter](https://realpython.com/python-gui-tkinter/)
  - [Tkinter 8.5 Reference](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html)
  - [Tkinter Theme Example](https://github.com/rdbende/Sun-Valley-ttk-theme)
  - [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer)

## Testing

*todo...*

## Pull Request Process

1. Create branch with correct naming scheme (see [section](#how-to-participate))
2. Ensure code is working properly and passed all tests (see [section](#testing))
3. Open PR (against dev branch)
4. Code review must be completed by running the code and tests, and ensuring code meets our coding standards (see [section](#coding-style))
    - *review is not necessary if PR is related to documentation or project maintenance*
5. Upon approving PR:
    - Close the github issue that the PR for
    - Delete PR branch
    - Merge PR into `dev` branch (*just merge PR to main if its related to documenation or project maintenance*)

## Deployment

*todo...*

## Code of Conduct

*See [Contributors Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/code_of_conduct.txt)*

## Join us

We are discussing this project on [discord](https://discord.com/). Please contact andromedamoon-stack or PatrickBruso by DM on Github for details on our server.
