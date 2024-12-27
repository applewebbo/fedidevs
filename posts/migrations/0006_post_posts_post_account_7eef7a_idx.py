# Generated by Django 5.1.3 on 2024-12-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0030_auto_20241201_1217"),
        ("posts", "0005_postsubscription"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["account", "created_at"], name="posts_post_account_7eef7a_idx"),
        ),
    ]
