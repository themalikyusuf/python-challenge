# python-challenge

This project builds a Docker image, pushes it to DockerHub and Deploys the image to ECS using GitHub Actions. There are a two workflows in this project:

- The first one (Lint and test code on pull request) is triggered when a pull request is opened. It checks the code for syntax and linting errors using Pylint. It then runs Pytest to test the application. Both 'checks' are required before the PR is merged to main branch.

- The second workflow builds the image, pushes to DockerHub and deploys the application to Amazon ECS. This is triggered when there is a push to the master branch. 
