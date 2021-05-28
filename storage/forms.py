from django import forms
from django.core import validators


class FormBasic(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # valid email
    verify_email = forms.EmailField(label='enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.ChoiceField(required=False,
                                   widget=forms.HiddenInput,
                                   validators=[
                                       validators.MaxLengthValidator(0)]
                                   )

    # custom valid form
    def clean(self):
        all_clean_date = super().clean()
        email = all_clean_date['email']
        vmail = all_clean_date['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILs MATCH")
