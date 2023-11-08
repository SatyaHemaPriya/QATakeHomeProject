import requests
import pytest


ENDPOINT = "http://localhost:9090"
VALID_BOOKS = [("testTitle", "testAuthor"), ("testTitle1", "testAuthor1"), ("testTitle2", "testAuthor2")]
INVALID_BOOKS = [("&%&%&", "testAuthor"), ("testTitle1", "&%&&%&%"), ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", "testAuthor2"), ("title", "***********************************************************")]

def test_cannot_call_invalid_endpoint():
    """
    test_cannot_call_invalid_endpoint calls invalid endpoint and expects 404 status code
    """ 
    response = requests.get(ENDPOINT + "/api/boks")
    assert response.status_code == 404

# VALIDTING CREATE BOOKS
@pytest.mark.parametrize("title,author", VALID_BOOKS)
def test_can_create_a_book_valid_inputs(title, author):
    """
    test_can_create_a_book_valid_inputs: for each input this test
        1. creates the book
        2. gets the create books based on ID returned in the response.
        3. asserst if the getResponse does not match with created book contents

    :param title: title used for creating the book
    :param author: author used for creating the book
    """ 
    payload = get_new_book_payload(title, author)
    
    #create book
    create_book_response = create_book(payload)
    assert create_book_response.status_code == 200

    data = create_book_response.json()
    book_id = data["unique_id"]
    
    #get book based on above book Id
    get_book_response = get_book(book_id)
    assert get_book_response.status_code == 200
    get_response_data = get_book_response.json()
    assert get_response_data["title"] == payload["title"]
    assert get_response_data["author"] == payload["author"]

@pytest.mark.parametrize("title,author", INVALID_BOOKS)
def test_can_create_a_book_invalid_inputs(title, author):
    """
    test_can_create_a_book_invalid_inputs: for each invalid input
        1. Creates a book.
        2. Asserts on status code 400 expecting client side error response from service.

    :param title: title used for creating the book
    :param author: author used for creating the book
    """ 
    payload = get_new_book_payload(title, author)
    create_book_response = create_book(payload)
    assert create_book_response.status_code == 400

# VALIDATING THE UPDATION
@pytest.mark.parametrize("title,author", VALID_BOOKS)
def test_can_update_valid_books(title, author):
    """
     test_can_update_valid_books: for each input this test
        1. creates the book
        2. updates the book based on ID returned in the response.
        3. Gets the book based on above ID
        4. asserst if the getResponse does not match with created book contents

    :param title: title used for creating the book
    :param author: author used for creating the book
    """ 
    # create a book
    payload = get_new_book_payload("DUMMY_TITLE", "DUMMY_AUTHOR")
    create_book_response =  create_book(payload)
    book_id = create_book_response.json()["unique_id"]
    
    # update a book
    updated_payload = get_new_book_payload(title, author)
    update_book_response = update_book(book_id, updated_payload)
    
    # get the book and validate
    get_book_response = get_book(book_id)
    assert get_book_response.status_code == 200
    get_response_data = get_book_response.json()
    assert get_response_data["title"] == updated_payload["title"]
    assert get_response_data["author"] == updated_payload["author"]

@pytest.mark.parametrize("title,author", INVALID_BOOKS)
def test_can_update_Invalid_books(title, author):
    """
    test_can_update_Invalid_books: for each invalid input
        1. Creates a book with valid input
        2. Update the same book with invalid payload.
        3. Asserts on status code 400 expecting client side error response from service.

    :param title: title used for creating the book
    :param author: author used for creating the book
    """ 

    # create a book
    payload = get_new_book_payload("DUMMY_TITLE", "DUMMY_AUTHOR")
    create_book_response =  create_book(payload)
    book_id = create_book_response.json()["unique_id"]
    
    # update a book
    updated_payload = get_new_book_payload(title, author)
    update_book_response = update_book(book_id, updated_payload)
    assert update_book_response.status_code == 400


@pytest.mark.parametrize("title,author", VALID_BOOKS)
def test_can_list_books(title, author):
    """
    test_can_list_books: for each input
        1. List books
        2. Capture book and create new book
        3. List books
        4. Compares latest count with previous count

    :param title: title used for creating the book
    :param author: author used for creating the book
    """ 
    #list books
    list_books_response_before = list_books()
    data = list_books_response_before.json()
    #capture count
    initial_count = len(data)
    payload = get_new_book_payload(title, author)
    #create book
    create_book(payload)
    #list books
    list_books_response_after = list_books()
    data_after = list_books_response_after.json()
    #assert on counts
    assert initial_count+1 == len(data_after)

@pytest.mark.parametrize("title,author", VALID_BOOKS)
def test_delete_books(title, author):
    """
    test_delete_books: for each input
        1. creates a book
        2. deletes the book
        3. Gets the book
        4. expects 404

    :param title: title used for creating the book
    :param author: author used for creating the book
    """ 
    payload = get_new_book_payload(title, author)

    #create book
    create_book_response = create_book(payload)
    data = create_book_response.json()
    book_id = data["unique_id"]
    
    #delete book
    delete_books(book_id)

    get_book_response = get_book(book_id)
    assert get_book_response.status_code == 404

def create_book(payload):
    """
    create_book Makes a post call to create book with given payload.

    :param payload: payload for the book
    :return: CreateBookResponse
    """ 
    return requests.post(ENDPOINT + "/api/books",json=payload)

def list_books():
    """
    list_books Makes a get call to get list of books

    :return: ListBookResponse
    """ 
    return requests.get(ENDPOINT + "/api/books")

def update_book(book_id, payload):
    """
    update_book Makes a put call to update a book

    :param book_id: Id fo the book to update
    :param payload: payload to update with.
    :return: UpdateBooksResponse
    """ 
    # `PUT /api/books/{id}`: Updates a book by id
    return requests.put(ENDPOINT + f"/api/books/{book_id}",json=payload)

def get_book(book_id):
    """
    get_book Makes get call to fetch a book with given Id.

    :param book_id: Id of the book to fetch.
    :return: GetBookResponse.
    """ 
    return requests.get(ENDPOINT + f"/api/books/{book_id}")

def delete_books(book_id):
    """
    delete_books Makes a delete call to delete the books with given Id.

    :param book_id: Id of the book to delete
    :return: DeleteBookResponse.
    """ 
    return requests.delete(ENDPOINT + f"/api/books/{book_id}")
             
def get_new_book_payload(title, author):
    """
    get_new_book_payload Helper function to create payload with given title and author

    :param title: title of the book
    :param author: Author of the book
    :return: Json payload for the book
    """ 
    return {
        "title": title,
        "author": author,
    }
