import json
import os
import pytest
import requests
import jsonpath
from conftest import NewUser

baseUrl = "https://gorest.co.in/public/v2"
path = "/graphql"
headers = {"Authorization": f"Bearer {os.environ.get('Token')}"}


@pytest.mark.order(1)
def test_successful_creation_new_user():
    """
    Test on gorest API, create user with a random email.
    """

    createUserMutation = """
    mutation ($name: String!, $gender: String!, $email: String!, $status: String!) {
      createUser(
        input: { name: $name, gender: $gender, email: $email, status: $status }
      ) {
        user {
          id
          name
          gender
          email
          status
        }
      }
    }
    """

    createUserVariables = {
        'name': NewUser.name,
        'email': NewUser.email,
        'gender': NewUser.gender,
        'status': NewUser.status,
    }
    response = requests.post(
        url=baseUrl+path, headers=headers, json={"query": createUserMutation, "variables": createUserVariables})
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    NewUser.id = jsonpath.jsonpath(
        responseJson, '$.data.createUser.user.id')[0]
    assert jsonpath.jsonpath(responseJson, '$.data.createUser.user.name')[
        0] == NewUser.name
    assert jsonpath.jsonpath(responseJson, '$.data.createUser.user.email')[
        0] == NewUser.email


@pytest.mark.order(2)
def test_get_all_users():
    """
    Test on gorest API, we get all users.
    """

    getAllUsersQuery = """
    {
      users {
        nodes {
          id
          name
          email
          gender
          status
        }
      }
    }
    """

    response = requests.post(
        url=baseUrl+path, headers=headers, json={"query": getAllUsersQuery})
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert len(jsonpath.jsonpath(responseJson, '$.data.users.nodes')) > 0


@pytest.mark.order(3)
def test_get_user_details_by_id():
    """
    Test on gorest API, we get user details by id.
    """

    getAllUsersQuery = """
    query ($id: ID!) {
      user(id: $id) {
        id
        name
        email
        gender
        status
      }
    }
    """

    getUserDetailsVariables = {'id': NewUser.id}
    response = requests.post(
        url=baseUrl+path, headers=headers, json={"query": getAllUsersQuery, "variables": getUserDetailsVariables})
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.user.name')[
        0] == NewUser.name
    assert jsonpath.jsonpath(responseJson, '$.data.user.email')[
        0] == NewUser.email


@pytest.mark.order(4)
def test_update_name_of_a_user():
    """
    Test on gorest API, update the user name.
    """
    nameToUpdate = "John Pourdanopoulos"

    updateUserMutation = """
    mutation ($id: Int!, $name: String!) {
      updateUser(input: { id: $id, name: $name }) {
        user {
          id
          name
          gender
          email
          status
        }
      }
    }
    """

    updateUserVariables = {
        'id': NewUser.id,
        'name': nameToUpdate
    }
    response = requests.post(
        url=baseUrl+path, headers=headers, json={"query": updateUserMutation, "variables": updateUserVariables})
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.updateUser.user.name')[
        0] == nameToUpdate
    assert jsonpath.jsonpath(responseJson, '$.data.updateUser.user.email')[
        0] == NewUser.email


@pytest.mark.order(5)
def test_delete_the_user():
    """
    Test on gorest API, delete the user.
    """

    deleteUserMutation = """
    mutation ($id: Int!) {
      deleteUser(input: { id: $id }) {
        user {
          id
          name
          gender
          email
          status
        }
      }
    }
    """

    deleteUserVariables = {'id': NewUser.id}
    response = requests.post(
        url=baseUrl+path, headers=headers, json={"query": deleteUserMutation, "variables": deleteUserVariables})
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.deleteUser.user.id')[
        0] == NewUser.id
    assert jsonpath.jsonpath(responseJson, '$.data.deleteUser.user.email')[
        0] == NewUser.email
