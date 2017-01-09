from __future__ import print_function
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User, Travel, JoinedTrip

import datetime


def travel(request):
    if 'logged_user' not in request.session:
        messages.error(request, "You are not allowed to see that")
        return redirect('/')

    user = User.objects.get(id=request.session['logged_user'])
    print (user.name)

    travelplans = Travel.objects.all()
    userplans = Travel.objects.filter(planner=user)

    context = {
        'travelplans': travelplans,
        'userplans': travelplans,
        'user': user
    }

    return render(request, 'travel/index.html', context)


def tripInfo(request, tripID):
    if 'logged_user' not in request.session:
        messages.error(request, "You are not allowed to see that")
        return redirect('/')
    currenttrip = Travel.objects.get(id=tripID)
    joins = JoinedTrip.objects.filter(trip=currenttrip)
    print(joins)
    context = {
        'trip': currenttrip,
        'joins': joins,
    }
    return render(request, "travel/tripinfo.html", context)


def createTravelForm(request):
    if 'logged_user' not in request.session:
        messages.error(request, "You are not allowed to see that")
        return redirect('/')
    return render(request, 'travel/tripcreate.html')


def createTravel(request):
    if 'logged_user' not in request.session:
        messages.error(request, "You are not allowed to see that")
        return redirect('/')

    starttime = datetime.datetime.now()
    endtime = datetime.datetime.now()

    user = User.objects.get(id=request.session['logged_user'])

    destination = request.POST["destination"]
    description = request.POST["description"]
    Travel.objects.create(destination=destination, description=description, planner=user, datestart=starttime,
                          dateend=endtime)
    return redirect(reverse('travels:travel'))


def deleteTravel(request, tripID):
    if 'logged_user' not in request.session:
        messages.error(request, "You are not allowed to see that")
        return redirect('/')
    tobedeleted = Travel.objects.get(id=tripID)
    tobedeleted.delete()
    return redirect(reverse('travels:travel'))


def joinTravel(request, tripID):
    if 'logged_user' not in request.session:
        messages.error(request, "You are not allowed to see that")
        return redirect('/')

    user = User.objects.get(id=request.session['logged_user'])
    trip = Travel.objects.get(id=tripID)
    join = JoinedTrip.objects.create(trip=trip, user=user)
    messages.success(request, "You successfully joined the trip")
    return redirect('{}/info'.format(tripID))

