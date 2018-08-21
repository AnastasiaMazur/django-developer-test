from django.shortcuts import render_to_response
from django.template import RequestContext

from rest_framework import viewsets

from roadmap.models import Project
from roadmap.serializers import ProjectSerializer


def dashboard(request):
    return render_to_response('dashboard/dashboard.html', {}, context_instance=RequestContext(request))


class APIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
