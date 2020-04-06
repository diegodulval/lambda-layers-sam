# [WIP] Boilerplate SAM
Project to studies SAM using Layers and Functions.

Below is a brief explanation of what we have in this repo:

```bash
.
├── README.md                  <-- This instructions file
├── events/                    <-- Folder to organize lambda events
├── docker/                    <-- Folder to organize docker files
│   ├── docker-compose.yaml    <-- Docker compose to run DynamoLocal
├── functions/hello            <-- Source code for a Demo lambda function
│   ├── app.py                 <-- Lambda function code
── layers                      <-- Folder to organize lambda layers
│   ├── python                 <-- Folder with custon functions
├── template.yaml              <-- SAM Template

```
## Requirements

* AWS CLI already configured with at least PowerUser permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)
* [Python Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


## Deploy
We need generate the final template using:
```bash
sh generate_template.sh
```
To build template
```bash
sam build --use-container
```
And to deploy application in AWS run the command bellow
```bash
sam deploy --parameter-overrides ENVNAME='PROD'
```
## Setup process

### Building the project

1. Dynamo Local

Start DynamoDB Local by executing the following at the command prompt:
```bash
docker run -p 8000:8000 amazon/dynamodb-local
```
This will run the DynamoDB local in a docker container at port 8000.

At the command prompt, list the tables on DynamoDB Local by executing:
```bash
aws dynamodb list-tables --endpoint-url http://localhost:8000
```

An output such as the one shown below confirms that the DynamoDB local instance has been installed and running:
```bash
{
  "TableNames": []
}
```

At the command prompt, create the PersonTable by executing:
```bash
aws dynamodb create-table --cli-input-json file://json/create_person_table.json --endpoint-url http://localhost:8000
```
**Note:** If you misconfigured your table and need to delete it, you may do so by executing the following command:
        *aws dynamodb delete-table --table-name PersonTable --endpoint-url http://localhost:8000*

2. SAM BUILD

[AWS Lambda requires a flat folder](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) with the application as well as its dependencies. When you make changes to your source code or dependency manifest,
run the following command to build your project local testing and deployment:

```bash
sam build --template sam-template.yaml
```

If your dependencies contain native modules that need to be compiled specifically for the operating system running on AWS Lambda, use this command to build inside a Lambda-like Docker container instead:
```bash
sam build --template sam-template.yaml --use-container
```

By default, this command writes built artifacts to `.aws-sam/build` folder.

### Local development

**Invoking function locally**
```bash
sam local invoke Helo --event /events/event.json --docker-netwok aws-resources
```

## Debug

Check link bellow to undestand how to debug this project in VSCode
* [VSCode Debug - Python](https://github.com/aws/aws-toolkit-vscode/blob/master/docs/debugging-python-lambda-functions.md)

# Appendix

### Python Virtual environment
**In case you're new to this**, python3 comes with `virtualenv` library by default so you can simply run the following:

1. Create a new virtual environment
2. Install dependencies in the new virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```


**NOTE:** You can find more information about Virtual Environment at [Python Official Docs here](https://docs.python.org/3/tutorial/venv.html). Alternatively, you may want to look at [Pipenv](https://github.com/pypa/pipenv) as the new way of setting up development workflows

## Pre commits - Black and Flake8

Execute `pre-commit install` to install git hooks in your .git/ directory.

#### Code Formatter: black
The black code formatter in Python is an opinionated tool that formats your code in the best way possible.

#### Code checker: Flake8
Flake8 is a powerful tool that checks our code’s compliance to PEP8
