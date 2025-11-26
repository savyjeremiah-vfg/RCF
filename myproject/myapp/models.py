from django.db import models

# ================== ANNOUNCEMENTS ==================
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='announcements/', blank=True, null=True)
    audio = models.FileField(upload_to='announcements/audio/', blank=True, null=True)
    video = models.FileField(upload_to='announcements/video/', blank=True, null=True)

    def __str__(self):
        return self.title

# ================== SERMONS ==================
class Sermon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='sermons/')
    image = models.ImageField(upload_to='sermon_images/', blank=True, null=True)
    audio = models.FileField(upload_to='sermons/audio/', blank=True, null=True)
    video = models.FileField(upload_to='sermons/video/', blank=True, null=True)

    def __str__(self):
        return self.title

# ================== TESTIMONIES ==================
class Testimony(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='testimonies/', blank=True, null=True)
    audio = models.FileField(upload_to='testimonies/audio/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date}"

# New Testimony submissions
class Testimonys(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonies/')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# ================== AUDIO ==================
class Audio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='audio/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

# ================== VIDEO ==================
class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

# ================== UPCOMING EVENTS ==================
class UpcomingEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_date = models.DateTimeField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.title} on {self.event_date.strftime('%Y-%m-%d %H:%M')}"

# ================== IMAGE GALLERY ==================
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
