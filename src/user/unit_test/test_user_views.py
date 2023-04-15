
import pytest
from rest_framework import status
from user.models import CustomUser
from user_fixtures import client, management_user, sale_user, get_tokens_for_user, user_data


@pytest.mark.django_db
def test_get_users(client, management_user):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')
    response = client.get('/users/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_user_with_management_user(client, management_user, user_data):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')
    data = user_data

    response = client.post('/users/', data=data)

    assert response.status_code == status.HTTP_201_CREATED

    user = CustomUser.objects.get(email=data['email'])
    assert user.first_name == data['first_name']
    assert user.last_name == data['last_name']
    assert user.role == data['role']
    assert user.check_password(data['password'])


@pytest.mark.django_db
def test_create_user_with_sale_user(client, sale_user, user_data):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    response = client.post('/users/', data=user_data)

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_update_user_with_management_user(client, management_user, user_data):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = user_data
    response = client.post('/users/', data=data)
    user_id = response.data['id']
    data_update = {
        'last_name': 'La Porta',
    }
    response = client.patch(f'/users/{user_id}/', data=data_update)
    assert response.status_code == status.HTTP_200_OK
    user = CustomUser.objects.get(email=data['email'])
    assert user.last_name == data_update['last_name']


@pytest.mark.django_db
def test_delete_user_with_management_user(client, management_user, user_data):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = user_data
    response = client.post('/users/', data=data)
    user_id = response.data['id']
    response = client.delete(f'/users/{user_id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT

