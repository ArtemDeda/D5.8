from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Category(models.Model):
    NEWS = 'NEWS'
    ARTICLE = 'ARTICLE'
    CATEGORY_CHOICES = [(NEWS, 'Новость'), (ARTICLE, 'Статья'),]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=NEWS, unique=True)

    def __str__(self):
        return self.get_name_display()


class News(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='Новость')
    content = models.TextField()
    date_published = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.user.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posttype')
    create_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        if self.rating != 0:
            self.rating -= 1
            self.save()

    def preview(self):
        return self.text[0:123] + "..."


class PostCategory(models.Model):
    post_through = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.SmallIntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        if self.comment_rating != 0:
            self.comment_rating -= 1
            self.save()
