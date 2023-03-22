# qroma-project-generator


### Prompts
>>> Set your project ID
>>> Choose the platform for your project:
     - Arduino CLI (see https://arduino.github.io/arduino-cli to get started)
     - Platform IO (see https://platformio.org/ to get started)
     - I will set up my own projects
>>> Do you want to generate a device-hosted website (Y/N)?
>>> Do you want to generate an Internet based website (Y/N)?
>>> Do you want to generate a smart phone app (Y/N)?


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
