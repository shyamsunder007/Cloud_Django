from django.db.models.signals import post_save

def auto_compress_file_on_post_save(sender, instance, **kargs):
instance.upload_file.compress()

post_save.connect(auto_compress_file_on_post_save, sender=MyContent) 