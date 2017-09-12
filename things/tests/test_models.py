from django.test import TestCase
from things.tests.factories import ThingFactory, ThingMetaFactory


class ThingTestCase(TestCase):

    def test_model_factory(self):
        thing = ThingFactory()
        meta = ThingMetaFactory(thing=thing)
        meta_two = ThingMetaFactory(key='Wow', value='Son', thing=thing)

        self.assertEqual(thing.id, 'some-sensor')
        self.assertEqual(thing.alias, 'something')
        self.assertEqual(thing.type, 'BEACON')
        self.assertEqual(thing.active, True)
        self.assertEqual(meta.key, 'Test')
        self.assertEqual(meta.value, 'Data')
        self.assertEqual(meta_two.key, 'Wow')
        self.assertEqual(meta_two.value, 'Son')
