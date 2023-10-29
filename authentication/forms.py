from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from authentication.models import User


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False, *args, **kwargs)
        user.is_admin = False
        user.save()
        return user


class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True, *args, **kwargs):
        user = super().save(commit=False, *args, **kwargs)
        user.is_admin = True
        if commit:
            user.save()
        return user
