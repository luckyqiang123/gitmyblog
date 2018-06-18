from django.db import models

class Notice(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return u'%s' % (self.content)
 
    class Meta:
        ordering=['-create_time']