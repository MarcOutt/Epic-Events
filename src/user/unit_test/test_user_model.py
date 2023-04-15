import pytest
from user.models import CustomUser
from user_fixtures import user_data, superuser_data


@pytest.mark.django_db
def test_create_user(user_data):
    user = CustomUser.objects.create_user(**user_data)
    assert user.email == 'p.laroche@example.com'
    assert user.first_name == 'Paul'
    assert user.last_name == 'Laroche'
    assert user.role == 'sale'
    assert user.check_password('test_password')


@pytest.mark.django_db
def test_create_superuser(superuser_data):
    superuser = CustomUser.objects.create_superuser(**superuser_data)
    assert superuser.email == 'r.lapierre@example.com'
    assert superuser.first_name == 'Robert'
    assert superuser.last_name == 'Lapierre'
    assert superuser.role == 'management'
    assert superuser.check_password('test_password')
    assert superuser.is_staff == True
    assert superuser.is_admin == True
