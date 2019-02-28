from django import forms

from widgets import SearchFormCharFieldWidget, QualifiedSearchFormCharFieldWidget

SCRIPT_CHOICES = (
        ('hieroglyphic', 'Hieroglyphic/Hieratic'),
        ('demotic', 'Demotic'),
        ('coptic', 'Coptic')
)


class SearchFormCharField(forms.CharField):

    def __init__(self, *args, **kwargs):
        print("field kwargs:", kwargs)
        if "qualifier" in kwargs:
            widget = QualifiedSearchFormCharFieldWidget(
                    qualifier=kwargs.pop("qualifier"),
                    choices=kwargs.pop("choices", {}),
                    label=kwargs.get("label")
            )
        else:
            widget = SearchFormCharFieldWidget(label=kwargs.get("label"))
        kwargs.setdefault("widget", widget)
        super().__init__(*args, **kwargs)
        print(self)


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



