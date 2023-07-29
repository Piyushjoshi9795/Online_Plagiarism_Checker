from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = {'email', 'username', 'first_name', 'last_name', 'i_am', }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = {'email', 'username', 'first_name', 'last_name', 'i_am', }


# class MyCustomLoginForm(LoginForm):
#     def __init__(self, *args, **kwargs):
#         super(MyCustomLoginForm, self).__init__(*args, **kwargs)
#         self.fields["login"].label = ""
#         self.fields["password"].label = ""
#
#     def login(self, *args, **kwargs):
#         # Add your own processing here.
#
#         # You must return the original result.
#         return super(MyCustomLoginForm, self).login(*args, **kwargs)


class MyCustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)

        I_AM = [('', 'I am'),
                ('teacher', 'Teacher'),
                ('student', 'Student')]

        firstname_widget = forms.TextInput(attrs={'type': 'text',
                                                  'placeholder':
                                                      _('First name'), })

        lastname_widget = forms.TextInput(attrs={'type': 'text',
                                                 'placeholder':
                                                     _('Last name'), })

        self.fields['first_name'] = forms.CharField(required=True, label=_(""),
                                                    widget=firstname_widget)
        self.fields['last_name'] = forms.CharField(required=True, label=_(""),
                                                   widget=lastname_widget)
        self.fields['i_am'] = forms.ChoiceField(required=True, label=_(""), choices=I_AM,
                                                widget=forms.Select(attrs={
                                                }))

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.

        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.
        user.i_am = self.cleaned_data['i_am']
        user.save()

        # You must return the original result.
        return user
