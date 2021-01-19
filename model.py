class Job(models.Model):
    attendant = models.ForeignKey(Attendant, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    company_logo = models.URLField(max_length=500, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    deadline = models.DateField(null=True)
    requirements = models.JSONField(null=True)

    def __str__(self):
        return self.title