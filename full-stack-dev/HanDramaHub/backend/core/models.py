from django.db import models

STATUSES = [
    ('P', 'Plan'),
    ('W', 'Watching'),
    ('C', 'Completed'),
]

# Create your models here.
class Drama(models.Model):
    #title
    title = models.CharField(max_length=200)
    #year
    year = models.IntegerField()
    #status
    status = models.CharField(choices=STATUSES, default='plan')
    #rating
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    #created_at
    created_at = models.DateTimeField(auto_now_add=True)
    #updated_at
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.title} {self.status}'
 