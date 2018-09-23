from django import forms



class NameForm(forms.ModelForm):
    post = forms.CharField()


    class Meta:
        model = get_name
        fields =('get_name',)
