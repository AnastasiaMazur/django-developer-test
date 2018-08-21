import json

from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory

from roadmap.views import APIViewSet
from roadmap.models import Project, Roadmap, Step


class APITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="BryceYork",
            email="byork@fusionlabs.com.au",
            password="qwerty"
        )
        self.steps = [
            Step.objects.create(name="Step 1", explanation="Do some things"),
            Step.objects.create(name="Step 2", explanation="Do some other things"),
            Step.objects.create(name="Step 3", explanation="Get some help to do this thing"),
            Step.objects.create(name="Step 4", explanation="Celebrate!")
        ]
        for step in self.steps:
            step.save()

        self.roadmap = Roadmap.objects.create(name="Sample Roadmap 1")
        self.roadmap.publications.add(*self.steps)

        self.project = Project.objects.create(
            name="Example Project A",
            description="This is a sample project",
            owner=self.user,
            roadmap=self.roadmap
        )

    def test_view_set(self):
        request = APIRequestFactory().get("")
        api_view = APIViewSet.as_view({"get": "list"})
        response = api_view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.rendered_content)[0]

        self.assertEqual(data["name"], self.project.name)
        self.assertEqual(data["description"], self.project.description)
        self.assertEqual(data["owner"], {"username": self.user.username, "email": self.user.email})
        self.assertEqual(data["roadmap"]["name"], self.roadmap.name)
        for i in range(len(self.steps)):
            self.assertEqual(data["roadmap"]["steps"][i]["name"], self.steps[i].name)
            self.assertEqual(data["roadmap"]["steps"][i]["explanation"], self.steps[i].explanation)
