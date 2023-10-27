# QA Take Home Project

## Description

This a pre-built FastAPI Sample App that should be used as base for your Performance Testing project.

It is a simple API for `books` and it has the following endpoints:

- `GET /books`: Returns a list of books
- `GET /books/{id}`: Returns a book by id
- `POST /books`: Creates a new book
- `PUT /books/{id}`: Updates a book by id
- `DELETE /books/{id}`: Deletes a book by id

## Prerequisites

You'll need `python` and `Docker` to run this project.

## Usage

1. Clone the repo:

```bash
git clone https://github.com/Harbour-Enterprises/SampleProject.git
```

2. Run it locally (_To make it easier, we've added a Makefile with all the commands you'll need to run this project._)

```bash
make
```

## Goal

The objective of this project is to evaluate your performance testing skills. You'll need to create a performance test suite for this API.

Should be included in the test suite:

- A test to validate the response time of each endpoint
- A test to validate the throughput of each endpoint
- A test to validate the error rate of each endpoint

Please also consider the following configuration for the test:

- 100 concurrent users (spawn rate of 10 users per second)
- 1 minute test duration

_We recommend using [Locust](https://github.com/locustio/locust) (an open source load testing tool) but not required._

## Deliverables

1. A performance test suite for this API

   - Locust Test Scripts: Well-documented Locust test scripts that define test scenarios and user behavior.
   - Test Execution Results: Test execution logs and reports, including performance metrics and analysis.
   - Recommendations: Performance optimization recommendations based on test results and analysis.

2. A README.md file with instructions on how to run the tests and a brief explanation of the test suite

## Bonus (optional)

- Include different User credentials (one with access to all endpoints and one with access only to the `GET /books` endpoint)

## Rights / Use Requirements

- Do not utilize any third-party managed services/APIs (i.e., do not send data to other companies)

- Written code for this project (other than imported libraries) must be original by you and not provided/subcontracted/owned by another company, contractor, or copied from any undisclosed source

- Optionally, after deliver, feel free to open source the result if you want (e.g., fork this repo to your own GitHub/portfolio)

## Questions

If you have any questions, please reach out to us at [caio@harbourshare.com](mailto:caio@harbourshare.com)
