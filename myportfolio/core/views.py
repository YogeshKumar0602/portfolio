from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import TechSkill, Project
from django.contrib import messages

def home(request):
    skills = TechSkill.objects.all()
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['email']

            full_message = f"Message from {name} <{sender_email}>:\n\n{message}"

            try:
                # Send to your inbox
                send_mail(
                    subject,
                    full_message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )

                # Send auto-reply to user
                thank_you_subject = "Thank you for contacting me!"
                thank_you_message = f"""
                Hi {name},

                Thanks for reaching out!

                I've received your message and will get back to you shortly.

                — Yogesh Kumar M
                """

                send_mail(
                    thank_you_subject,
                    thank_you_message,
                    settings.EMAIL_HOST_USER,
                    [sender_email],
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully ✅")

            except Exception as e:
                messages.error(request, "Sorry, there was an error sending your message ❌")

    return render(request, 'index.html', {
        'skills': skills,
        'projects': projects,
        'form': form
    })
