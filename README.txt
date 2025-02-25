This git repo is used as a template for setting up automated unit testing using Github Actions

The trigger for the Github Action is a push or pull request to the main branch. This means that the .yml file that executes the action needs to be in the main branch otherwise Github Actions won't find it. Therefore, the main branch in this repo shows the presence of the .yml file, as well as a generic README, plus a requirements.txt file.

The development branch in this repo is meant as a simple depiction of a development branch. A python function and unittest in this branch can then be merged in to the main branch and the Github action will automatically run the unittests during the pull request.
