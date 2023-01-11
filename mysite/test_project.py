from django.test import TestCase
from proj.models import ID
from proj.views import plswork, mygod

class ModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ID.objects.create(id_passajira='123', nomer_telefona='+12', parol='201331', kolichestvo_mil='15')

    def test_id_passajira_label(self):
        test = ID.objects.get(id=1)
        field_label = test._meta.get_field('id_passajira').verbose_name
        self.assertEquals(field_label, 'id passajira')

    def test_nomer_telefona_label(self):
        test = ID.objects.get(id=1)
        field_label = test._meta.get_field('nomer_telefona').verbose_name
        self.assertEquals(field_label, 'nomer telefona')

    def test_parol_label(self):
        test = ID.objects.get(id=1)
        field_label = test._meta.get_field('parol').verbose_name
        self.assertEquals(field_label, 'parol')

    def test_nomer_telefona_max_length(self):
        test = ID.objects.get(id=1)
        max_length = test._meta.get_field('nomer_telefona').max_length
        self.assertEquals(max_length, 50)

    def test_for_display(self):
        display = plswork("<WSGIRequest: GET '/'>").__str__()
        self.assertEquals(display, "<HttpResponse status_code=200, \"{'ID': <QuerySet [<ID: ID object (1)>]>}\">")

    def test_for_records(self):
        expected_num = mygod()
        self.assertEquals(expected_num, 4)
