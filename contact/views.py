from django.http import HttpResponseRedirect
from django.shortcuts import render
from contact.forms import ContactForm
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})

    contact = Contact.objects.create(**form.cleaned_data)
    
    _send_mail(
        'contact/contact_email.txt',
        {'contact': contact},
        'Novo contato.',
        settings.DEFAULT_FROM_EMAIL,
        form.cleaned_data['email'])

    messages.success(request, 'Contato realizado com sucesso!')
    return HttpResponseRedirect('/contact/')



def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})



def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])
