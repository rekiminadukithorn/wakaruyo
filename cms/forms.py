<<<<<<< HEAD
<<<<<<< HEAD
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
=======
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
=======
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb

UserModel = get_user_model()


<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['username'].widget.attrs['class'] = 'input'
       self.fields['password'].widget.attrs['class'] = 'input'

<<<<<<< HEAD
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
=======
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
=======
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'twitter')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
<<<<<<< HEAD
<<<<<<< HEAD
            field.widget.attrs['class'] = 'input'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['username'].widget.attrs['class'] = 'input'
       self.fields['password'].widget.attrs['class'] = 'input'


#UserUpdateFormをパクった
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('todo',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
=======
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
=======
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
            field.widget.attrs['class'] = 'input'