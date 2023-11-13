# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```


You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change).

The `.env` needs to be updated with the CONNECTION_STRING and DATABSE_NAME of MongoDB

There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## App Operation

Enter the title of new to-do item in the input field and press the submit button. The list of items at the top of the page should update with the new entry

## App Testing

All tests are under `tests` directory. To run all tests, invoke `pytest` at the root of the project or from `tests` directory:
```bash
poetry run pytest .\todo_app\tests
```

You can also run indivual tests as shown below:
```bash
poetry run pytest -k test_view_model_done_items_property
```

Please refer to [Pytest docs](https://docs.pytest.org/en/7.1.x/how-to/usage.html) for more info.

## Using Docker Containerisation

Build images using:
```
$ docker build --target development --tag todo-app:dev .
$ docker build --target production --tag todo-app:prod .
```

Run containers using:
```
$ docker run --env-file .env --publish 8080:8000 todo-app:prod
$ docker run --env-file .env --publish 8080:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/opt/app/todo_app todo-app:dev
```

#### Running Tests

Build images using:
```
$ docker build --target test --tag todo-app:test .
```

Run container using:
```
$ docker run todo-app:test
```

## Azure

### Build & publish the image

```
$ docker login
$ docker build --target production --tag amtronics/todo-app:prod .
$ docker push amtronics/todo-app:prod
```
The image is uploaded to Docker Hub:
https://hub.docker.com/r/amtronics/todo-app


### Create WebApp

```
$ az login
$ az appservice plan create --resource-group Cohort27_AmiGho_ProjectExercise -n module8_amigho_sp --sku B1 --is-linux
$ az webapp create --resource-group Cohort27_AmiGho_ProjectExercise --plan module8_amigho_sp --name agmod8 --deployment-container-image-name docker.io/amtronics/todo-app:prod
$ az webapp config appsettings set -g Cohort27_AmiGho_ProjectExercise -n agmod8 --settings @azure_app_settings.json
$ curl -dH -X POST "https://\$<deployment_username>:<deployment_password>@<webapp_name>.scm.azurewebsites.net/docker/hook"
```