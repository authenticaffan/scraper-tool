from django.db import models

class Scrape(models.Model):
    website = models.URLField()
    target_element = models.CharField(max_length=255)
    scraped_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scrape of {self.website} - {self.target_element}"

