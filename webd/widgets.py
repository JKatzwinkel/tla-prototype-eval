from django import forms

import store

class SearchFormCharFieldWidget(forms.Widget):
    input_type = "text"
    template_name = "widgets/search_form_text_field.html"

    def __init__(self, *args, **kwargs):
        kwargs["attrs"] = kwargs.get("attrs", {})
        kwargs["attrs"].update(
            **{
                "divclass": kwargs.get('attrs').get('divclass') or "col-sm-10",
                "class": kwargs.get('attrs').get('class') or "form-control mb3",
                "label": kwargs.pop("label"),
                "required": kwargs.pop("required", False),
            }
        )
        super().__init__(*args, **kwargs)


class QualifiedSearchFormCharFieldWidget(SearchFormCharFieldWidget):
    template_name = "widgets/qualified_search_form_text_field.html"

    def __init__(self, qualifier="attribute", choices={}, *args, **kwargs):
        kwargs["attrs"] = {
                "qualifier": {
                    "name": qualifier,
                    "choices": {
                        key: {
                            "label": v.get("label"),
                            "checked": v.get("checked"),
                            }
                        for key, v in choices.items()
                    },
                },
                "required": kwargs.pop("required", False),
            }
        super().__init__(*args, **kwargs)


class SearchMetadataFieldWidget(forms.MultiWidget):
    def __init__(self):
        widgets = (
                SearchFormCharFieldWidget(
                    label="Passport",
                    attrs={
                        "class":"form-control col-sm-10",
                        "divclass": "col-sm-5",
                    },
                ),
                forms.Select(
                    choices = [
                        (
                            choice, choice
                        ) for choice in list(
                            filter(
                                lambda predicate: predicate.startswith('passport') and predicate.endswith('id'),
                                store.get_mappings('text')
                            )
                        )
                    ],
                    attrs={"class": "form-control col-sm-4"},
                ),
        )
        super().__init__(widgets)

    def decompress(self, value):
        if value:
            return value.lsplit(" ", 1)
        return ["", ""]

    def format_output(self, rendered_widgets):
        return "{} {}".format(*rendered_widgets)
