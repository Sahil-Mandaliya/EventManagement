<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Event Management Service](#event-management-service)
    - [1. Requirements](#1-requirements)
      - [1.1. Docker](#11-docker)
      - [1.2. pyenv](#12-pyenv)
      - [1.3. git](#13-git)
      - [1.4. mysql](#14-mysql)
      - [1.5. Update the ~/.zshrc file (MAC)](#15-update-the-zshrc-file-mac)
    - [2. Development Setup](#2-development-setup)
      - [2.1. Checkout and Env file](#21-checkout-and-env-file)
      - [2.2. Building Image and Running Service](#22-building-image-and-running-service)
    - [3. Deployment](#3-deployment)
    - [4. One time activity](#4-one-time-activity)
    - [5. Swagger](#5-swagger)
      - [5.1. Url](#51-url)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Event Management Service

### 1. Requirements

#### 1.1. Docker

Install docker and docker-compose in your system. If you are using Mac or
Windows you can install "Docker for Mac||Windows".

#### 1.2. pyenv

Make sure you have installed **pyenv** and **pyenv-virtualenv** locally. You can check if it is installed
using `pyenv --version`. If it is not installed use [this link](https://github.com/pyenv/pyenv).
Check pyenv-virtualenv is installed using `pyenv virtualenv --version`,
if not use [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to setup.

#### 1.3. git

Make sure you have **git** installed and the username, email and the ssh keys are configured properly.

#### 1.4. mysql

Install mysql in your system. We need mysql driver files in order to install required python modules. We install requirements.txt locally in order to get the hints in our IDE.
If your on a Mac:
`sh $brew install mysql `

#### 1.5. Update the ~/.zshrc file (MAC)

Add these to ~/.zshrc:

```sh
export PATH="$PYENV_ROOT/bin:$PATH"
export PYENV_ROOT="$HOME/.pyenv"

eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

export LDFLAGS="-L/opt/homebrew/opt/zlib/lib -L/opt/homebrew/opt/zstd/lib"
export CPPFLAGS="-I/opt/homebrew/opt/zlib/include"
export PATH="/opt/homebrew/opt/mysql/bin:$PATH"
```

### 2. Development Setup

#### 2.1. Checkout and Env file

Checkout the code and create env file-

```sh
mkdir -p ~/src/tech
cd ~/src/tech
git clone https://github.com/Sahil-Mandaliya/EventManagement.git
```

Create env file, activate pyenv and install requirements.

```sh
cd ~/src/tech/EventManagement
cp env.sample .env          # get a copy of .env file
make pyenv
pyenv activate event-api-3.9.2
```

In order to setup using docker, ensure that you have docker and docker-compose
is setup in your system.

#### 2.2. Building Image and Running Service

In order to build the service image and run the service run following command.

```sh
cd ~/src/tech/EventManagement
make install # installs requirements
make build # builds the api service image
make start # starts the server
make migration # creates database migrations
make migrate # applies migration to database
make create-superuser USERNAME={} PASSWORD={} EMAIL={} FULL_NAME={} PHONE={} # Creates User With Admin Access

```

### 3. Deployment

To deploy new changes, checkout to the branch you want to build and
then run following command-

```sh
git pull origin master
make build
make start
```


### 4. One time activity

* Create Super User using above mentioned command [Creates One Admin User and Adds Roles ["admin", "user"] in the system]
* Login to current system for super user using Login API - It will returns the Access token [ Valid for 60 minutes ]
* Super User Can Add New Users
* Can Assign roles to users

* Users with role type "admin" can Add new Users, Assign roles, Add / update / delete Events


### 5. Swagger
#### 5.1. Url
```sh
{base_url}/docs - (Base URL is mentioned in the shared postman collection)
To Access the database : {base_url}:8091
```
