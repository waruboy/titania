from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

class ExampleForm(forms.Form):

    nama = forms.CharField(
        label = "Nama Anda",
        max_length = 80,
        required = True,
    )

    email = forms.EmailField(
        label = "Email Anda",
        max_length = 80,
        required = True,
    )

    pesanan = forms.CharField(
        label = "Pesanan Anda.",
        required = False,
        widget = forms.Textarea,
    )

    komentar = forms.CharField(
        label = "Komentar tambahan untuk kami.",
        required = False,
        widget = forms.Textarea,
    )
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "id-exampleForm"
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Kirimkan pesanan'))
        super(ExampleForm,self).__init__(*args, **kwargs)