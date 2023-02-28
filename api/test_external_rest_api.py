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


@pytest.mark.order(6)
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
        url=baseUrl+path, headers=headers, params=params)
    responseJson = json.loads(response.text)
    assert response.status_code == 201
    NewUser.id = jsonpath.jsonpath(responseJson, '$.id')[0]
    assert jsonpath.jsonpath(responseJson, '$.name')[0] == NewUser.name
    assert jsonpath.jsonpath(responseJson, '$.email')[0] == NewUser.email


@pytest.mark.order(7)
def test_get_all_users():
    """
    Test on gorest API, we get all users.
    """

    response = requests.get(
        url=baseUrl+path, headers=headers)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert len(responseJson) > 0


@pytest.mark.order(8)
def test_get_user_details_by_id():
    """
    Test on gorest API, we get user details by id.
    """

    response = requests.get(
        url=baseUrl+path+'/'+str(NewUser.id), headers=headers)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.name')[0] == NewUser.name
    assert jsonpath.jsonpath(responseJson, '$.email')[0] == NewUser.email


@pytest.mark.order(9)
def test_update_name_of_a_user():
    """
    Test on gorest API, update the user name.
    """

    nameToUpdate = "John Pourdanopoulos"

    params = {
        'name': nameToUpdate,
    }
    response = requests.put(
        url=baseUrl+path+'/'+str(NewUser.id), headers=headers, params=params)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.name')[0] == nameToUpdate
    assert jsonpath.jsonpath(responseJson, '$.email')[0] == NewUser.email


@pytest.mark.order(10)
def test_delete_the_user():
    """
    Test on gorest API, delete the user.
    """

    response = requests.delete(
        url=baseUrl+path+'/'+str(NewUser.id), headers=headers, )
    assert response.status_code == 204
