from django.test import TestCase
import logging
class LoggingTestCase(TestCase):
    def test_logging(self):
        logger = logging.getLogger(__name__)
        logger.info('This is a test log message.')
        self.assertEqual(1, 1)