from django import forms

SCRIPT_CHOICES = (
        ('hieroglyphic', 'Hieroglyphic/Hieratic'),
        ('demotic', 'Demotic'),
        ('coptic', 'Coptic')
)


class DictSearchForm(forms.Form):
    script = forms.CheckboxSelectMultiple(
        choices=SCRIPT_CHOICES,
    )
    transcription = forms.CharField(
        label="Transcription",
        widget=forms.TextInput,
        max_length=128,
        required=False,
    )


class TextWordSearchForm(forms.Form):
    textname = forms.CharField(
        label="Text Name",
        required=False,
    )
    hieroglyphs = forms.CharField(
        label="Hieroglyphs",
        required=False,
    )
    lemma = forms.CharField(
        label="Lemmatized as",
        required=False,
    )

