# QA Take Home Project

## Description

Our customers have a lot of books, and they need to reliably keep track of them using our API. Our engineers built this book-tracking app and submitted to the QA lead. The QA lead will need to test the app, and report the findings back to both engineering and business affairs.

We would like you to create a test suite for this API that contains the following endpoints:

- `GET /books`: Returns a list of books
- `GET /books/{id}`: Returns a book by id
- `POST /books`: Creates a new book
- `PUT /books/{id}`: Updates a book by id
- `DELETE /books/{id}`: Deletes a book by id

## Prerequisites

You'll need `python` and `Docker` installed to run this project.

## Usage

1. Clone the repo:

```bash
git clone https://github.com/Harbour-Enterprises/QATakeHomeProject.git
```

2. Run it locally (_To make it easier, we've added a Makefile with all the commands you'll need to run this project._)

```bash
make
```

## Goal

The objective of this project is to evaluate your testing skills. You'll need to create a test suite for this API.

`Some tools we recommend (but feel free to use any other tool you want):`

- [Locust](https://github.com/locustio/locust) (performance testing tool)
- [Postman](https://www.postman.com/) (an API testing tool)
- [pytest](https://docs.pytest.org/en/6.2.x/) (testing framework for unit and functional tests)

## Deliverables

1. A test suite for this API

   - Test Scripts: Well-documented test scripts that define test scenarios and user behavior.
   - Test Execution Results: Test execution logs and reports.
   - Recommendations: Optimization recommendations based on test results and analysis.

2. A README.md file with instructions on how to run the tests and a brief explanation of the test suite

## Bonus (optional)

- Performance tests for this API

## Rights / Use Requirements

- Do not utilize any third-party managed services/APIs (i.e., do not send data to other companies)

- Written code for this project (other than imported libraries) must be original by you and not provided/subcontracted/owned by another company, contractor, or copied from any undisclosed source

- Optionally, after deliver, feel free to open source the result if you want (e.g., fork this repo to your own GitHub/portfolio)

## Questions

If you have any questions, please reach out to us at [caio@harbourshare.com](mailto:caio@harbourshare.com)
