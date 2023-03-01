import json
import os
import secrets
import pytest
import requests
import jsonpath
from conftest import NewUser

randomEmail = f"{secrets.token_hex(8)}@mail.com"
baseUrl = "https://gorest.co.in/public/v2"
path = "/users"
headers = {"Authorization": f"Bearer {os.environ.get('API_TOKEN')}"}


@pytest.mark.serial
def test_successful_creation_new_user():
    """
    Test on gorest API, create user with a random email.
    """

    NewUser.email = randomEmail
    params = {
        'name': NewUser.name,
        'email': NewUser.email,
        'gender': NewUser.gender,
        'status': NewUser.status,
    }
    response = requests.post(
        url=f"{baseUrl}{path}", headers=headers, params=params)
    responseJson = json.loads(response.text)
    assert response.status_code == 201
    NewUser.id = jsonpath.jsonpath(responseJson, '$.id')[0]
    assert jsonpath.jsonpath(responseJson, '$.name')[0] == NewUser.name
    assert jsonpath.jsonpath(responseJson, '$.email')[0] == NewUser.email


@pytest.mark.serial
def test_get_all_users():
    """
    Test on gorest API, get all users.
    """

    response = requests.get(
        url=f"{baseUrl}{path}", headers=headers)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert len(responseJson) > 0


@pytest.mark.serial
def test_get_user_details_by_id():
    """
    Test on gorest API, get user details by id.
    """

    response = requests.get(
        url=f"{baseUrl}{path}/{NewUser.id}", headers=headers)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.name')[0] == NewUser.name
    assert jsonpath.jsonpath(responseJson, '$.email')[0] == NewUser.email


@pytest.mark.serial
def test_update_name_of_a_user():
    """
    Test on gorest API, update the user name.
    """

    nameToUpdate = "John Pourdanopoulos"

    params = {
        'name': nameToUpdate,
    }
    response = requests.put(
        url=f"{baseUrl}{path}/{NewUser.id}", headers=headers, params=params)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.name')[0] == nameToUpdate
    assert jsonpath.jsonpath(responseJson, '$.email')[0] == NewUser.email


@pytest.mark.serial
def test_delete_the_user():
    """
    Test on gorest API, delete the user.
    """

    response = requests.delete(
        url=f"{baseUrl}{path}/{NewUser.id}", headers=headers, )
    assert response.status_code == 204
