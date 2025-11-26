from django.contrib import admin
from .models import Announcement, Sermon, Testimony, Audio, Video, UpcomingEvent,Image

# Register all models
admin.site.register(Announcement)
admin.site.register(Sermon)
admin.site.register(Testimony)
admin.site.register(Audio)
admin.site.register(Video)
admin.site.register(UpcomingEvent)
admin.site.register(Image)
