# qroma-project-generator

### Download
Compiled Windows executables are available in [/downloads](/downloads)

### To Run qroma-project-generator locally
* `git clone https://github.com/qromatech/qroma-project-generator`
* `git submodule init`
* `git submodule update`
* to make git changes for qroma-project-template
  * `cd qroma-project-template`
  * `git checkout main`
  * `cd ..`
* `poetry install`
* `poetry run python src/qroma-cli.py new :my-qroma-project`
* `poetry run python src/qroma-cli.py protobuf :my-qroma-project`
* `poetry run python src/qroma-cli.py build :my-qroma-project`


### Create/Run a New Project
#### Pre-conditions
* Docker installed
* VS Code with PlatformIO plugin
* node/npm installed

#### Steps to Develop a New Project Locally
* `qroma new :$PROJECT-ID`
* `qroma build :$PROJECT-ID`
* `qroma pb edit :pumpkin-2023`
* `qroma firmware edit :pumpkin-2023`
* `qroma site edit :$PROJECT-ID`
* `npm run start`

#### Steps to Deploy to Github Pages
These steps assume you have already created an empty repository named `$PROJECT-ID` for your project. See https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository.

Next, run the steps below from your project's root directory.
* `git init`
* `git checkout -b main`
* `git add *`
* `git commit -m "New qroma project commit"`
* `git remote add origin https://github.com/OWNER/$PROJECT-ID`
* `git push origin main`

This project is ready to deploy the project's Docusaurus site to public Github pages with your declared Protocol Buffer types and using your compiled firmware artifacts. See Docusaurus docs at https://docusaurus.io/docs/deployment#triggering-deployment-with-github-actions
* see build ran - `https://github.com/OWNER/$PROJECT-ID/actions`
* Github - project - settings - pages - https://github.com/OWNER/$PROJECT-ID/settings/pages
  * select `gh-pages` to be source branch
* Site is available at http://OWNER.github.io/$PROJECT-ID


### Dev Notes
#### To build command line executable [Windows]
* From root directory, run `package-qroma-project-generator.bat`
* Alternatively, run command `poetry run python -m PyInstaller src/qroma-cli.py`

#### To run tests that emulate a product demo to create, build, and run a new project
* (still needs a little tweaking, probably about making sure the right directories are on the Python path) `poetry run python -m pytest tests/src/end_to_end/project_demo_tests.py` 


#### Editing py-qroma
`poetry add -e C:\Users\ajb\Projects\qromatech\py-qroma`


#### Prompts
```
>>> Set your project ID
>>> Choose the platform for your project:
     - Arduino CLI (see https://arduino.github.io/arduino-cli to get started)
     - Platform IO (see https://platformio.org/ to get started)
     - I will set up my own projects
>>> Do you want to generate a device-hosted website (Y/N)?
>>> Do you want to generate an Internet based website (Y/N)?
>>> Do you want to generate a smart phone app (Y/N)?
```
