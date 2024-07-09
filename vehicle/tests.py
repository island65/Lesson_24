from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Car


class VehicleTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_car(self):
        """Тестирование создания машины"""
        data = {
            'title': 'Test car',
            'description': "Test"
        }

        response = self.client.post(
            '/cars/',
            data=data,
        )
        print(response.json())
        # self.assertEqual(response.status_code, 201)
        # self.assertEqual(response.json()['title'], 'Test car')
        # self.client.post(
        #     '/cars/',
        #     data=data,
        # )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
    {'id': 1, 'milage': [], 'title': 'Test car', 'description': 'Test', 'owner': None}
        )

        self.assertTrue(
            Car.objects.all().exists()
        )

    def test_list_car(self):
        """Тестирование получения списка машин"""

        Car.objects.create(
            title='List Test',
            description="List Test"
        )
        response = self.client.get(
            '/cars/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
        [{'id':2, 'milage': [], 'title': 'List Test', 'description': 'List Test', 'owner': None}]
        )
