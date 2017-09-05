from django.test import TestCase
from puppies.models import Puppy

class PuppyTest(TestCase):
    """ Test module for puppy model """

    def setUp(self):
        Puppy.objects.create(
            name="Casper", age=3, breed="bull dog", color="Black"
        )
        Puppy.objects.create(
            name="Muffin", age=1, breed="Gradane", color="Brown"
        )

    def test_puppy_bread(self):
        puppy_casper = Puppy.objects.get(name="Casper")
        puppy_muffin = Puppy.objects.get(name="Muffin")

        self.assertEquals(
            puppy_casper.get_breed(), "Casper belongs to bull dog breed. "
        )
        self.assertEquals(
            puppy_muffin.get_breed(), "Muffin belongs to Gradane breed. "
        )