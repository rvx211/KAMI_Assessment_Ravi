"""This is test cases for the aircraft module"""
import ast
import json

from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from core.exceptions.aircraft import AircraftListEmptyException
from user_api.models import User

# Create your tests here.
class AircraftAPITest(APITestCase):
    """This is the aircraft test class

    Args:
        APITestCase (object): Django REST Framework APITestCase
    """
    def setUp(self) -> None:
        """This is setup function for the aircraft test
        """
        self.aircraft_unit_url = "v1:aircraft-calculation-unit"
        self.aircraft_list_url = "v1:aircraft-calculation-list"
        self.user = User.objects.create_user(
            username="logintest01", email="logintest01@email.com", password="&$P4ssw0rdl01")
        self.token = RefreshToken.for_user(self.user).access_token.__str__()
        self.aircraft_unit_1 = {'aircraft_id': '', 'aircraft_passenger': 100}
        self.aircraft_unit_2 = {'aircraft_id': 2, 'aircraft_passenger': ''}
        self.aircraft_unit_3 = {'aircraft_id': 'a', 'aircraft_passenger': 150}
        self.aircraft_unit_4 = {'aircraft_id': 4, 'aircraft_passenger': 'b'}
        self.aircraft_unit_5 = {'aircraft_id': 5, 'aircraft_passenger': 200}
        self.aircraft_list_1 = json.dumps({'aircraft': []})
        self.aircraft_list_2 = json.dumps({'aircraft': [
            {'aircraft_id': "", 'aircraft_passenger': 100},
            {'aircraft_id': 1, 'aircraft_passenger': 200},
            {'aircraft_id': 2, 'aircraft_passenger': 200},
            {'aircraft_id': 3, 'aircraft_passenger': 200},
            {'aircraft_id': 4, 'aircraft_passenger': 200},
            {'aircraft_id': 5, 'aircraft_passenger': 200},
            {'aircraft_id': 6, 'aircraft_passenger': 200},
            {'aircraft_id': 7, 'aircraft_passenger': 200},
            {'aircraft_id': 8, 'aircraft_passenger': 200},
            {'aircraft_id': 9, 'aircraft_passenger': 200}
        ]})
        self.aircraft_list_3 = json.dumps({'aircraft': [
            {'aircraft_id': 10, 'aircraft_passenger': ""},
            {'aircraft_id': 1, 'aircraft_passenger': 200},
            {'aircraft_id': 2, 'aircraft_passenger': 200},
            {'aircraft_id': 3, 'aircraft_passenger': 200},
            {'aircraft_id': 4, 'aircraft_passenger': 200},
            {'aircraft_id': 5, 'aircraft_passenger': 200},
            {'aircraft_id': 6, 'aircraft_passenger': 200},
            {'aircraft_id': 7, 'aircraft_passenger': 200},
            {'aircraft_id': 8, 'aircraft_passenger': 200},
            {'aircraft_id': 9, 'aircraft_passenger': 200}
        ]})
        self.aircraft_list_4 = json.dumps({'aircraft': [
            {'aircraft_id': 'a', 'aircraft_passenger': 100},
            {'aircraft_id': 1, 'aircraft_passenger': 200},
            {'aircraft_id': 2, 'aircraft_passenger': 200},
            {'aircraft_id': 3, 'aircraft_passenger': 200},
            {'aircraft_id': 4, 'aircraft_passenger': 200},
            {'aircraft_id': 5, 'aircraft_passenger': 200},
            {'aircraft_id': 6, 'aircraft_passenger': 200},
            {'aircraft_id': 7, 'aircraft_passenger': 200},
            {'aircraft_id': 8, 'aircraft_passenger': 200},
            {'aircraft_id': 9, 'aircraft_passenger': 200}
        ]})
        self.aircraft_list_5 = json.dumps({'aircraft': [
            {'aircraft_id': 10, 'aircraft_passenger': 'a'},
            {'aircraft_id': 1, 'aircraft_passenger': 200},
            {'aircraft_id': 2, 'aircraft_passenger': 200},
            {'aircraft_id': 3, 'aircraft_passenger': 200},
            {'aircraft_id': 4, 'aircraft_passenger': 200},
            {'aircraft_id': 5, 'aircraft_passenger': 200},
            {'aircraft_id': 6, 'aircraft_passenger': 200},
            {'aircraft_id': 7, 'aircraft_passenger': 200},
            {'aircraft_id': 8, 'aircraft_passenger': 200},
            {'aircraft_id': 9, 'aircraft_passenger': 200}
        ]})
        self.aircraft_list_6 = json.dumps({'aircraft': [
            {'aircraft_id': 1, 'aircraft_passenger': 200},
            {'aircraft_id': 2, 'aircraft_passenger': 200},
            {'aircraft_id': 3, 'aircraft_passenger': 200},
            {'aircraft_id': 4, 'aircraft_passenger': 200},
            {'aircraft_id': 5, 'aircraft_passenger': 200},
            {'aircraft_id': 6, 'aircraft_passenger': 200},
            {'aircraft_id': 7, 'aircraft_passenger': 200},
            {'aircraft_id': 8, 'aircraft_passenger': 200},
            {'aircraft_id': 9, 'aircraft_passenger': 200},
            {'aircraft_id': 10, 'aircraft_passenger': 200}
        ]})
        self.auth_headers = {'HTTP_AUTHORIZATION': 'Bearer ' + self.token,}

    def test_aircraft_unit_empty_id(self):
        """This is aircraft unit calculation test with empty id
        """
        response = self.client.post(reverse(self.aircraft_unit_url), data=self.aircraft_unit_1, **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['aircraft_id'], ['A valid integer is required.'])

    def test_aircraft_unit_empty_passenger(self):
        """This is aircraft unit calculation test with empty passenger
        """
        response = self.client.post(reverse(self.aircraft_unit_url), data=self.aircraft_unit_2, **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['aircraft_passenger'], ['A valid number is required.'])

    def test_aircraft_unit_invalid_id(self):
        """This is aircraft unit calculation test with invalid id
        """
        response = self.client.post(reverse(self.aircraft_unit_url), data=self.aircraft_unit_3, **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['aircraft_id'], ['A valid integer is required.'])

    def test_aircraft_unit_invalid_passenger(self):
        """This is aircraft unit calculation test with invalid passenger
        """
        response = self.client.post(reverse(self.aircraft_unit_url), data=self.aircraft_unit_4, **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['aircraft_passenger'], ['A valid number is required.'])

    def test_aircraft_unit_valid_data(self):
        """This is aircraft unit calculation test with valid data
        """
        response = self.client.post(reverse(self.aircraft_unit_url), data=self.aircraft_unit_5, **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        fuel_tank_capacity = self.aircraft_unit_5['aircraft_id'] * settings.FUEL_TANK_MULTIPLIER
        basic_fc_per_minute = self.aircraft_unit_5['aircraft_id'] * settings.BASIC_FUEL_MULTIPLIER
        additional_fc_per_minute = self.aircraft_unit_5['aircraft_passenger'] * settings.ADDITIONAL_FUEL_MULTIPLIER
        total_fc_per_minute = basic_fc_per_minute + additional_fc_per_minute
        max_flight_minutes_time = fuel_tank_capacity / total_fc_per_minute
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content['aircraft_total_fuel_consumption_per_minute'], total_fc_per_minute)
        self.assertEqual(content['aircraft_maximum_flight_time_in_minutes'], max_flight_minutes_time)

    def test_aircraft_list_empty(self):
        """This is aircraft list calculation test with empty list
        """
        response = self.client.post(reverse(self.aircraft_list_url), data=self.aircraft_list_1, content_type='application/json', **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['detail'], AircraftListEmptyException().detail)

    def test_aircraft_list_empty_id(self):
        """This is aircraft list calculation test with empty id
        """
        response = self.client.post(reverse(self.aircraft_list_url), data=self.aircraft_list_2, content_type='application/json', **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['aircraft'][0]['aircraft_id'], ['A valid integer is required.'])

    def test_aircraft_list_empty_passenger(self):
        """This is aircraft list calculation test with empty passenger
        """
        response = self.client.post(reverse(self.aircraft_list_url), data=self.aircraft_list_3, content_type='application/json', **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['aircraft'][0]['aircraft_passenger'], ['A valid number is required.'])

    def test_aircraft_list_invalid_id(self):
        """This is aircraft list calculation test with invalid id
        """
        response = self.client.post(reverse(self.aircraft_list_url), data=self.aircraft_list_4, content_type='application/json', **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['aircraft'][0]['aircraft_id'], ['A valid integer is required.'])

    def test_aircraft_unit_invalid_passenger(self):
        """This is aircraft list calculation test with invalid passenger
        """
        response = self.client.post(reverse(self.aircraft_list_url), data=self.aircraft_list_5, content_type='application/json', **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['aircraft'][0]['aircraft_passenger'], ['A valid number is required.'])

    def test_aircraft_unit_valid_data(self):
        """This is aircraft list calculation test with valid list
        """
        response = self.client.post(reverse(self.aircraft_list_url), data=self.aircraft_list_6, content_type='application/json', **self.auth_headers)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for aircraft in content['aircraft']:
            fuel_tank_capacity = aircraft['aircraft_id'] * settings.FUEL_TANK_MULTIPLIER
            basic_fc_per_minute = aircraft['aircraft_id'] * settings.BASIC_FUEL_MULTIPLIER
            additional_fc_per_minute = aircraft['aircraft_passenger'] * settings.ADDITIONAL_FUEL_MULTIPLIER
            total_fc_per_minute = basic_fc_per_minute + additional_fc_per_minute
            max_flight_minutes_time = fuel_tank_capacity / total_fc_per_minute
            self.assertEqual(aircraft['aircraft_total_fuel_consumption_per_minute'], total_fc_per_minute)
            self.assertEqual(aircraft['aircraft_maximum_flight_time_in_minutes'], max_flight_minutes_time)
