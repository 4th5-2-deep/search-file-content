from django.db import models


class Document(models.Model):
    description = models.TextField(blank=True)
    markdown = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def markdown_content(self):
        return self.markdown.read().decode('utf-8')

    @classmethod
    def search_in_markdown(cls, query):
        documents = cls.objects.all()
        pk_list = [ document.pk for document in documents if query in document.markdown_content ]
        return cls.objects.filter(pk__in=pk_list)
