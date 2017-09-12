from rest_framework import status
from rest_framework.test import APITestCase
from things.tests.factories import ThingFactory


class ThingsApiTestCase(APITestCase):
    def test_get_things(self):
        response = self.client.get('/api/things/')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals([], response.data)

    def test_create_thing(self):
        data = {'id': 'some-id', 'type': 'RFID', }
        response = self.client.post('/api/things/', data=data)
        self.assertEquals(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEquals(response.data['id'], data['id'], response.data)
        self.assertEquals(response.data['type'], data['type'], response.data)

    def test_cant_create_thing_with_same_id(self):
        data = {'id': 'some-id', 'type': 'RFID', }
        self.client.post('/api/things/', data=data)
        response = self.client.post('/api/things/', data=data)
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code, response.data)

    def test_update_thing(self):
        thing = ThingFactory(id='Testing-Sensor', type='BEACON')
        data = {'type': 'RFID'}
        response = self.client.patch('/api/things/{id}/'.format(id=thing.id), data=data)
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.data)
        self.assertEquals(response.data['type'], 'RFID')

    def test_get_one_thing(self):
        thing = ThingFactory(id='Testing-Sensor', type='BEACON')
        response = self.client.get('/api/things/{id}/'.format(id=thing.id))
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_delete_thing(self):
        thing = ThingFactory(id='Testing-Sensor', type='BEACON')
        response = self.client.delete('/api/things/{id}/'.format(id=thing.id))
        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_create_thing_meta(self):
        thing = ThingFactory()

        data = {
            'key': 'test',
            'value': 'value_test',
        }

        response = self.client.post('/api/things/{}/meta/'.format(thing.id), data=data)
        self.assertEquals(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEquals(response.data['key'], data['key'], response.data)
        self.assertEquals(response.data['value'], data['value'], response.data)
