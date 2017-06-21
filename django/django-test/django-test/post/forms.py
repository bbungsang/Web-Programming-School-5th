from django import forms

from post.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'photo',
            'comment',
        ]

    def check_save(self, **kwargs):
        author = kwargs.get('author', None)
        print(author)

        if not self.instance.pk:
            self.instance.author = author

        return self.instance

