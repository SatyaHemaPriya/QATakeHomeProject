# Sample Project

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

- A performance test suite for this API
- A README.md file with instructions on how to run the tests and a brief explanation of the test suite

## Bonus (optional)

- A Dockerfile to run the tests
- A CI/CD pipeline to run the tests
- A report to visualize the results

## Questions

If you have any questions, please reach out to us at [caio@harbourshare.com](mailto:caio@harbourshare.com)
