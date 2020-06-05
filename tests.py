from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

from .views import index, getresources, getmeetings
from django.urls import reverse
from django.contrib.auth.models import User


#try:
#    cur.execute("LOCK TABLE mytable IN ACCESS EXCLUSIVE MODE NOWAIT")
#except psycopg2.OperationalError as e:
#    if e.pgcode == psycopg2.errorcodes.LOCK_NOT_AVAILABLE:
#        locked = True
#    else:
#        raise
#


# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        meet=Meeting(meetingtitle="Meeting on Firstview")
        self.assertEqual(str(meet), meet.meetingtitle)
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):
        
    def test_string(self):
        id=MeetingMinutes(meetingid="First Meeting")
        self.assertEqual(str(id), id.meetingid)
    
    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')


class ResourceTest(TestCase):
        
    def test_string(self):
        name=Resource(resourcename="useful link")
        self.assertEqual(str(name),name.resourcename)
    
    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')



class EventTest(TestCase):
        
    def test_string(self):
        title=Event(eventtitle="watch django install video")
        self.assertEqual(str(title), title.eventtitle)
    
    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetResourcesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

class GetMeetings(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)


class MeetingDetailsTest(TestCase):
    def setUp(self):
        meetingdetails=Meeting(meetingtitle='Meeting on Firstview', meetingdata='2020-05-04', meetingtime='23:38:30', meetinglocation='zoom', 
        meetinagenda='1.lecture 2.discussion')
        return meetingdetails
       
    
    def test_string(self):
        meet=self.setup()
        self.assertEqual(str(meet), meet.meetingtitle)
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')
