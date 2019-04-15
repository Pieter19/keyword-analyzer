import os
from unittest import TestCase

import vcr

from keyword_analyzer.analyzer.impl import parse_url, ValidationError, get_keywords, url_statistics

my_vcr = vcr.VCR(
    cassette_library_dir=os.path.dirname(os.path.realpath(__file__)),
    record_mode='once'
)


class AnalyzerTest(TestCase):
    @vcr.use_cassette('tests/fixtures/pirc_req.yaml')
    def test_correct_url(self):
        result = parse_url('http://pirc.pl')
        self.assertTrue(result)

    def test_url_missing_protocol(self):
        self.assertRaises(ValidationError, parse_url, 'pirc.pl')

    def test_url_random_string(self):
        self.assertRaises(ValidationError, parse_url, 'pasdasdasdl')

    @vcr.use_cassette('tests/fixtures/pirc_req.yaml')
    def test_finding_keywords(self):
        result = parse_url('http://pirc.pl')
        self.assertTrue(len(get_keywords(result)) > 0)

    @vcr.use_cassette('tests/fixtures/pirc_req.yaml')
    def test_keyword_count(self):
        result = url_statistics('http://pirc.pl')
        irc_keyword = next((keyword for keyword in result if keyword['keyword'] == 'irc'), None)
        self.assertEqual(irc_keyword['uses'], 15)
