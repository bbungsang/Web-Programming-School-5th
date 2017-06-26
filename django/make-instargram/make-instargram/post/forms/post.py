from django import forms

from post.models import Post


class PostForm(forms.ModelForm):

    comment = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )

    class Meta:
        model = Post
        fields = (
            'photo',
            'comment',
        )

    def save(self, **kwargs):

        commit = kwargs.get('commit', True)
        author = kwargs.pop('author', None)

        if not self.instance.pk:
            self.instance.author = author

        instance = super().save(**kwargs)

        comment_string = self.cleaned_data['comment']

        if commit and instance.my_comment:
            instance.my_comment.content = comment_string
            instance.my_comment.save()
        else:
            Post.objects.create(
                post=instance,
                author=author,
                content=comment_string,
            )
            instance.save()
        return instance