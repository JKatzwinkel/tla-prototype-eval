from django import forms
from django.forms.fields import MultiValueField
from django.core.validators import RegexValidator


from widgets import SearchFormCharFieldWidget, QualifiedSearchFormCharFieldWidget, SearchMetadataFieldWidget

import store

SCRIPT_CHOICES = (
        ('hieroglyphic', 'Hieroglyphic/Hieratic'),
        ('demotic', 'Demotic'),
        ('coptic', 'Coptic')
)



class SearchMetadataField(MultiValueField):
    widget = SearchMetadataFieldWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.ChoiceField(
                label="predicate",
            ),
            SearchFormCharField(
                label="identifier",
            )
        )
        super().__init__(fields, **kwargs)

    def compress(self, data_list):
        if data_list:
            return "{} {}".format(*data_list)


class SearchFormCharField(forms.CharField):

    def __init__(self, *args, **kwargs):
        if "qualifier" in kwargs:
            widget = QualifiedSearchFormCharFieldWidget(
                    qualifier=kwargs.pop("qualifier"),
                    choices=kwargs.pop("choices", {}),
                    label=kwargs.get("label")
            )
        else:
            widget = SearchFormCharFieldWidget(
                label=kwargs.get("label"),
                required=kwargs.get("required", False),
            )
        kwargs.setdefault("widget", widget)
        super().__init__(*args, **kwargs)


class DictSearchForm(forms.Form):
    script = forms.MultipleChoiceField(
        choices=SCRIPT_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
    )
    transcription = SearchFormCharField(
        label="Transcription",
        max_length=128,
        required=False,
    )
    translation = SearchFormCharField(
        label="Translation",
        max_length=128,
        required=False,
    )


class TextWordSearchForm(forms.Form):
    textname = SearchFormCharField(
        label="Text Name",
        required=False,
    )
    hieroglyphs = SearchFormCharField(
        label="Hieroglyphs",
        required=False,
    )
    lemma = SearchFormCharField(
        label="Lemmatized as",
        required=False,
    )
    translation = SearchFormCharField(
        label="Translation",
        qualifier="trans_lang",
        choices={
            "en": {
                "label": "English",
                "checked": False,
                },
            "de": {
                "label": "German",
                "checked": True,
            },
        },
        required=False,
    )
    passport = SearchMetadataField(
        required=False
    )




