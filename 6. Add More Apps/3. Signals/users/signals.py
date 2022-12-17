from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User  # importing default django user model


# sender: is sender fo signal, instance: onj of model that has trigger this signal, created: true, false value for
# wheater the model data is newly added to database or not (wheather it is update or new record creation)
# def profileUpdated(sender, instance, created, **kwargs):
#     print('Profile Saved!')
#     print('Instance:', instance)
#     print('Created:', created)

# Using Decorator: We annotate on top of function (@Receiver)
# @receiver(post_save, sender=Profile)  #Decorator for signal
# def deleteUser(sender, instance, **kwargs):
#     print('Deleting user...')

# signals
# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)


def profileUpdated(sender, instance, created, **kwargs):
    print('Profile Signal is Triggered!!')
    if created:
        user = instance
        profile = Profile.objects.create(user=user, username=user.name, email=user.email, first_name=user.name)


def deleteUser(sender, instance, **kwargs):
    print('User Signal is Triggered!!')
    user = instance.user
    user.delete()


post_save.connect(profileUpdated, sender=User)
post_delete.connect(deleteUser, sender=Profile)  # If Profile is deleted, it will automatically delete User
