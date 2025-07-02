from django.db import models

class Topic(models.Model):
    """
    A topic the user is learning about.

    Args:
        models (models.Model): class that represents a database table
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class Entry(models.Model):
    """
    Something specific learned about a topic.

    Args:
        models (models.Model): class that represents a database table
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."