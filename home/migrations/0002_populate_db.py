from django.db import migrations

def populate_initial_db(apps, *args):
    LevelClear = apps.get_model('home', 'LevelClear')
    for i in ["expression", "gallery", "mail", "memes"]:
        levelclear_obj = LevelClear.objects.create(name=i, cleared=False)
        levelclear_obj.save()

class Migration(migrations.Migration):
    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_initial_db),
    ]