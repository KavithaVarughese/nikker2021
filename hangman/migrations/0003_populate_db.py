from django.db import migrations

def populate_initial_db(apps, *args):
    Phrase = apps.get_model('hangman', 'Phrase')
    for i in ["Settu laifu", "Come to amazon", "Sleep is overrated", "Gaus sed aakallee"]:
        phrase = Phrase.objects.create(phrase=i.upper(), success=False, wrong_tries=0)
        phrase.save()

class Migration(migrations.Migration):
    dependencies = [
        ('hangman', '0002_auto_20210110_1653'),
    ]

    operations = [
        migrations.RunPython(populate_initial_db),
    ]