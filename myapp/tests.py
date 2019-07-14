# from django.test import TestCase
# from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from myapp.models import Doctor


class DoctorTestCases (APITestCase):
    def SetUp(self):
        self.client = APIClient
        self.url = '/sample/'
        Doctor.objects.create (f_name="Ammar", l_name="Fitwalla", username="ammar12", password="ammmar1234",
                               email="ammmarfitwalla@gmail.com")

    def test_model_Doctor_str(self):
        doctor_str = Doctor.objects.create (f_name="Ammar", l_name="Fitwalla", username="ammar12",
                                            password="ammmar1234", email="ammmarfitwalla@gmail.com")
        print ('test')
        print (doctor_str)
        self.assertEqual (Doctor.__str__ (doctor_str), "ammar12")


'''
    def test_Doctor_listing(self):
        """ Testing """
        response = self.client.get(self.uri, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
'''
