from django import forms

CHOICES = (
    ('+', '+'),
    ('-', '-'),
    ('*', '*'),
    ('/', '/')
)


class MathsForm(forms.Form):
    amount = forms.IntegerField(min_value=1, max_value=50)
    minValue = forms.IntegerField(min_value=0, max_value=100)
    maxValue = forms.IntegerField(min_value=1, max_value=100)
    operations = forms.MultipleChoiceField(
        choices=CHOICES,
        label="...",
        required=True,
        widget=forms.CheckboxSelectMultiple())



