from django.shortcuts import render

from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django import forms
from django.core.mail import send_mail

class HomeView(TemplateView):

    template_name = "home.html"

class AboutView(TemplateView):

    template_name = "about.html"

class ContactForm(forms.Form):

    nom = forms.CharField(max_length=100, label="Nom")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")

class ContactView(FormView):

    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):

        send_mail(
        	
            subject=f"Nouveau message de {form.cleaned_data['nom']}",
            message=form.cleaned_data["message"],
            from_email=form.cleaned_data["email"],
            recipient_list=["contact@exemple.com"],
        )
        return super().form_valid(form)

