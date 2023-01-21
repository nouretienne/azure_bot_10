from helpers.luis_helper import LuisHelper # the class where the code should be tested
from flight_booking_recognizer import FlightBookingRecognizer
import unittest # This is the test framework
from config import DefaultConfig




class Test_Testdst_city(unittest.TestCase):

    def setUp(self):
        self.luis_recognizer = FlightBookingRecognizer(DefaultConfig)

    async def test_dst_city_valid(self):
        input_text = 'I would like to go from Paris to London'
        a , result = await LuisHelper.execute_luis_query(self.luis_recognizer,input_text)
        self.assertEqual(result.__dict__['dst_city'],'London')

    async def test_dst_city_missing(self):
        input_text = 'I would like to go on vacation from Paris'
        _, result = await LuisHelper.execute_luis_query(self.luis_recognizer,input_text)
        self.assertEqual(result.__dict__['dst_city'], None)
    
