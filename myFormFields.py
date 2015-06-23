from django import forms
from django.core.validators import RegexValidator

class PositiveIntegerField(forms.IntegerField):
    def __init__(self, *args, **kwargs):

        minimumvalue = kwargs.pop('min_value', 0)
        maximumvalue = kwargs.pop("max_value", None)
        if not kwargs.get('widget'):
            kwargs['widget'] = forms.NumberInput(attrs={"required":"required"})

        super(PositiveIntegerField, self).__init__(max_value=maximumvalue, min_value=minimumvalue, *args, **kwargs)

class OptionalPositiveIntegerField(PositiveIntegerField):
    def __init__(self, *args, **kwargs):

        if not kwargs.get('widget'):
            kwargs['widget'] = forms.NumberInput(attrs={})
        super(OptionalPositiveIntegerField, self).__init__( required=False, *args, **kwargs)

class OptionalPercentField(OptionalPositiveIntegerField):
    def __init__(self, *args, **kwargs):
        super(OptionalPercentField, self).__init__(max_value=100, *args, **kwargs)
