from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader, RequestContext
from person.models import Person, PhoneNumber

from person.forms import PersonForm, PhoneNumberFormSet
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from rest_framework.decorators import list_route, detail_route, permission_classes, authentication_classes
from rest_framework import viewsets, status
import json
# Create your views here.

# GET, POST, PATCH, DELETE CALLs,
# Calls Using View Set.


def get_all_persons(request):
    all_persons = Person.objects.all()
    response = dict()
    person_list=[]
    for person in all_persons:
        person_details = dict()
        person_details['id'] = person.id
        person_details['firstName'] = person.first_name
        person_details['lastName'] = person.last_name
        person_details['company'] = person.company
        person_list.append(person_details)
    response['Person'] = person_list
    return HttpResponse(json.dumps(response), content_type="application/json", status=status.HTTP_200_OK)


def index(request):
    people = Person.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request)
    context.update({'page_name': 'index', 'people': people})
    return HttpResponse(template.render(context))
    # This does the exact same thing, but in one line.
    #return render_to_response("index.html", {'page_name': 'index', 'people': Person.objects.all()}, RequestContext(request))


def add_or_edit(request, id):
    if id is None:
        person = None
        page_name = "add"
    else:
        person = get_object_or_404(Person, id=id)
        page_name = "edit"
    if request.method == "GET":
        form = PersonForm(instance=person)
        phone_forms = PhoneNumberFormSet(instance=person)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        phone_forms = PhoneNumberFormSet(request.POST, instance=person)
        if form.is_valid() and phone_forms.is_valid():
            person = form.save()
            phone_forms = PhoneNumberFormSet(request.POST, instance=person)
            phone_forms.is_valid()
            phone_forms.save()
            return HttpResponseRedirect('/person/%s/' % person.id)
    return render_to_response('add.html', {'page_name': page_name, 'form': form, 'phone_forms': phone_forms, 'person': person}, RequestContext(request))


def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponse("person Object deleted Successfully", content_type="application/json", status=status.HTTP_200_OK)


def detail(request, id):
    person = Person.objects.get(id=id)
    person_details = dict()
    person_details['id'] = person.id
    person_details['firstName'] = person.first_name
    person_details['lastName'] = person.last_name
    person_details['company'] = person.company
    return HttpResponse(json.dumps(person_details), content_type="application/json", status=status.HTTP_200_OK)

# class based view for the demo.


class PersonViewSet(viewsets.ViewSet):

    @list_route(methods=['GET'], permission_classes=[IsAuthenticated])
    def GetAllPersons(self, request):
        allPersons = Person.objects.all()
        response = dict()
        personList=[]
        for person in allPersons:
            personDetails = dict()
            personDetails['id'] = person.id
            personDetails['firstName'] = person.first_name
            personDetails['lastName'] = person.last_name
            personDetails['company'] = person.company
            personList.append(personDetails)
        response['Person'] = personList
        return HttpResponse(json.dumps(response), content_type="application/json", status=status.HTTP_200_OK)

    @list_route(methods=['POST'], permission_classes=[IsAuthenticated])
    def UpdatePersonDetails(self, request):
        person = Person.objects.filter(first_name= request.data['first_name']).first()
        person.company = request.data['company']
        person.title = request.data['title']
        person.email = request.data['email']
        person.save()
        return HttpResponse("Person Object updated successfully", status=status.HTTP_200_OK)

    @list_route(methods=['PUT'], permission_classes=[IsAuthenticated])
    def CreatePersonDetails(self, request):
        person = Person.objects.create(first_name=request.data['first_name'], last_name=request.data['last_name'],
                                       company=request.data['company'], title=request.data['title'], email=request.data['email'],
                                       url=request.data['url'])
        person.save()
        return HttpResponse("Created Person details successfully", status=status.HTTP_200_OK)

    @list_route(methods=['DELETE'], permission_classes=[IsAuthenticated])
    def DeletePersonDetails(self, request):
        person = Person.objects.get(id=request.data['id'])
        person.delete()
        return HttpResponse("Deleted Person details successfully", content_type="application/json", status=status.HTTP_200_OK)