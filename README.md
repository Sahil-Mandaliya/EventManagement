## Table of Contents

- [Event Management API](#jodo-api)
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

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Jodo API

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

Create env file, activate pyenv and install requirements. This is required to
enable your editor to pull information of the modules being used in order to
show hints.

```sh
cd ~/src/tech/EventManagement
cp env.sample .env          # get a copy of .env file
make pyenv
```

In order to setup using docker, ensure that you have docker and docker-compose
is setup in your system.

#### 2.2. Building Image and Running Service

In order to build the service image and run the service run following command.

```sh
cd ~/src/tech/EventManagement
make precommit
make build # builds the api service image
make createuser   # Create super user
make initialdata # Populates the initial data
make start        # Start the service
```

### 3. Deployment

To deploy new changes, checkout to the branch you want to build and
then run following command-

```sh
make build
make start
```