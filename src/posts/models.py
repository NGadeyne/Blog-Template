from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

User = get_user_model()


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = HTMLField()
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        super().save(*args, **kwargs)
        
    def author_or_default(self):
        if self.author:
            return self.author.username
        return "L'auteur mystère"   
