# Write the test cases.
# There are 3 things (the functions that do not start with the word test and those that do):
# These are: (i) Positive assert, (ii) Negative assert and (iii) Test Cases

import sender_stand_request

# General Functions
def possitive_assert (code):
    assert code == 201

def negative_assert (code):
    assert code == 400

# Testing Checklist #1
def test_number_of_character_1 ():
    response_test_number_of_character_1 = sender_stand_request.create_personal_kit("a")
    possitive_assert(response_test_number_of_character_1.status_code)
    assert response_test_number_of_character_1.json()["name"] == "a"

# Testing Checklist #2
def test_number_of_character_511 ():
    long_name = "a" * 511
    response_test_number_of_character_511 = sender_stand_request.create_personal_kit(long_name)
    possitive_assert(response_test_number_of_character_511.status_code)
    assert response_test_number_of_character_511.json()["name"] == long_name

# Testing Checklist #3
def test_number_of_character_0 ():
    response_test_number_of_character_0 = sender_stand_request.create_personal_kit("")
    negative_assert(response_test_number_of_character_0.status_code)
    assert response_test_number_of_character_0.json()["name"] == ""

# Testing Checklist #4
def test_number_of_character_512 ():
    long_name_2 = "a" * 512
    response_test_number_of_character_512 = sender_stand_request.create_personal_kit(long_name_2)
    negative_assert(response_test_number_of_character_512.status_code)
    assert response_test_number_of_character_512.json()["name"] == long_name_2

# Testing Checklist #5
def test_special_character_allowed ():
    response_test_special_character_allowed = sender_stand_request.create_personal_kit("%")
    possitive_assert(response_test_special_character_allowed.status_code)
    assert response_test_special_character_allowed.json()["name"] == "%"

# Testing Checklist #6
def test_spaces_allowed ():
    response_test_spaces_allowed = sender_stand_request.create_personal_kit("a Aa")
    possitive_assert(response_test_spaces_allowed.status_code)
    assert response_test_spaces_allowed.json()["name"] == "a Aa"

# Testing Checklist #7
def test_number_allowed ():
    response_test_number_allowed = sender_stand_request.create_personal_kit("123")
    possitive_assert(response_test_number_allowed.status_code)
    assert response_test_number_allowed.json()["name"] == "123"

# Testing Checklist #8
def test_request_without_params ():
    response_test_request_without_params = sender_stand_request.create_personal_kit()
    negative_assert(response_test_request_without_params.status_code)
    assert response_test_request_without_params.json()["name"]

# Testing Checklist #9
def diferent_param ():
    response_diferent_param = sender_stand_request.create_personal_kit(123)
    negative_assert(response_diferent_param.status_code)
    assert response_diferent_param.json()["name"] == 123
