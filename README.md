
<h1 align="center">Behave BDD Test Examples 🚀🔬</h1>



<!-- Badges -->
<p align="center">
<a href="https://github.com/tooniez/behave-bdd-python/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/tooniez/behave-bdd-python"></a>
<a href="https://github.com/tooniez/behave-bdd-python/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/tooniez/behave-bdd-python"></a>
<a href="https://github.com/tooniez/behave-bdd-python/stargazers"><img alt="Github Stars" src="https://img.shields.io/github/stars/tooniez/behave-bdd-python"></a>
<a href="https://github.com/tooniez/behave-bdd-python/blob/master/LICENSE"><img alt="MIT" src="https://img.shields.io/github/license/tooniez/behave-bdd-python"></a>
<img src="https://img.shields.io/badge/behave-1.2.0-blue" alt="Behave 1.2.0" />
<img src="https://img.shields.io/badge/selenium-4.0.0-blue" alt="Selenium 4.0.0" />
<!-- <a href="https://github.com/tooniez/behave-bdd-python/"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a> -->


<h2 align="center">Elevate Your BDD with Behave!</h2>

</p>

## Contents

1. [Introduction](#intro)
    - [Packages Used](#packages)
    - [Features](#features)
    - [Steps Implemented](#steps)
    - [Uilities](#utilities)
3. [Join the Community!](#section03)
4. [License](#section04)



<a id='intro'></a>

## Introduction

This repository serves as a reference for working on BDD Behave and Selenium integration, ensuring clarity on the existing features and their implementations.

<a id='packages'></a>

### 📦 Packages Used
- **behave**: A behavior-driven development (BDD) framework written in Python.
- **selenium**: A tool for automating web applications for testing purposes.
- **requests**: A HTTP library to handle requests and responses.

<a id='features'></a>

### 🔍 Types of Features

1. **Unit Tests**: 
   - Scenarios for creating mock objects and using utility functions.

2. **API Tests**: 
   - Scenarios for testing reponse code using Requests library.
   
2. **E2E Tests**: 
   - Scenarios for opening the Google webpage and performing searches.

<a id='steps'></a>

### 🧪 Steps Implemented

- **Given Steps**: 
  - Creating mock objects.
  - Makes a HTTP requests
  - Opening the Google webpage.
  
- **When Steps**: 
  - Calling the mock object.
  - Response is returned.
  - Searching for a query on Google.
  
- **Then Steps**: 
  - Validating the expected results from the mock object.
  - Checking response code is valid.
  - Checking if the search results contain the queried term.

<a id='utilities'></a>

### Utilities

- **Logging**:
  - Sets default log format.

<a id='started'></a>

## Getting Started

Run `make all` to install dependencies and run the tests. See the provided `Makefile` for other run commands.

<a id='section03'></a>

## Join the Community!

Got ideas? We'd love your input! Check out our [Contributing Guidelines](.github/CONTRIBUTING.md) and dive in. Don't forget to drop a ⭐️ if you like what you see!

<a id='section04'></a>

## License

Copyright © 2024 [tooniez](https://github.com/tooniez). <br />
This project is [MIT](https://github.com/tooniez/appium-framework/blob/main/LICENSE) licensed.
