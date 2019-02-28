from django import forms


class SearchFormCharFieldWidget(forms.Widget):
    input_type = "text"
    template_name = "widgets/search_form_text_field.html"

    def __init__(self, *args, **kwargs):
        print("widget kwargs:", kwargs)
        kwargs["attrs"] = kwargs.get("attrs", {})
        kwargs["attrs"].update(
                **{
                    "class": "form-control mb3 "+kwargs.pop("class", ""),
                    "label": kwargs.pop("label"),
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
            }
        super().__init__(*args, **kwargs)


