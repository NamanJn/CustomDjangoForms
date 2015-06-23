import fasta as mc
from django import forms

class FastaField(forms.Field):

     def validate(self, value):

        super(FastaField, self).validate(value)
        if value != "":
            try:
                mc.FastaFile(value, fileName=False)
            except ValueError as e:
                raise forms.ValidationError("Sequence is not in FASTA format!")


class FastaTextField(forms.CharField, FastaField):

    def __init__(self, *args, **kwargs):

        if not kwargs.get('widget'):
            kwargs['widget'] = forms.Textarea
        if not kwargs.get('required'):
            kwargs['required'] = False

        super(FastaTextField, self).__init__(*args, **kwargs)

    def to_python(self, data):
        return data


class FastaFileField(forms.FileField, FastaField):

    def __init__(self, *args, **kwargs):

        if not kwargs.get("required"):
            kwargs['required'] = False
        super(FastaFileField, self).__init__(*args, **kwargs)

    def to_python(self, value):

        super(FastaFileField, self).to_python(value)
        data = ""
        if value:
            data = value.read()
        return data


class FastaForm(forms.Form):

    sequenceS = FastaTextField(label="Enter in FASTA sequence")
    sequenceF = FastaFileField(label="Upload FASTA sequence")

    def clean(self):

        super(FastaForm, self).clean()
        fastaFile = self.cleaned_data.get("sequenceF")
        fastaSequence = self.cleaned_data.get("sequenceS")
        if not fastaFile and not fastaSequence:
            raise forms.ValidationError("Enter a sequence ! Either upload or enter in directly!")
        elif fastaFile and fastaSequence:
            raise forms.ValidationError("Either upload or enter in directly ! Don't do both!")
