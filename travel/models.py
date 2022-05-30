from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField('Category')
    img = models.FileField(upload_to="pic/%y/")
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    @classmethod
    def all_images(cls, self):

        return Image.objects.all()

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(category__name__icontains=search_images)
        return images

    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def view_category(cls,cat):
        category = cls.objects.filter(category=cat)
        return category

    # Change the order of added travels beginning with most recent
    class Meta:
        ordering = ('-id',)


class Tag(models.Model):
    name = models.CharField(max_length=155)
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    