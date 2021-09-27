from pages.models import CommentModel

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['date_added','blog']