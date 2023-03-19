import pytest
import pandas as pd
import self as self

from pages.search_page import SearchPage
from tests.base_test import BaseTest
from tests.read_from import tools


class TestCSV(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = SearchPage(self.driver, self.wait)
        self.page.go_to_search_page()

    @pytest.mark.parametrize("service", tools.getData(self))
    def test_extract_all_search_service(self, load_pages, service):
        search_input = service

        self.page.search_on_home_page(search_input)
        service_name = self.page.get_service_search_results_title(search_input)
        number = str(len(service_name))
        print("\n""\n" "Total Results Found : " "\n""\n" + "\n".join(number))

        print("\n""\n" "Service Names are: " "\n""\n" + "\n".join(service_name))

        xs = search_input
        s = ''.join(xs)

        dict = {'Search Keyword': s, 'Service Name': service_name}
        df = pd.DataFrame(dict)
        df.to_csv(s)

    @pytest.mark.parametrize("service", tools.getData(self))
    def test_extract_only_first_ten_search_service(self, load_pages, service):
        search_input = service
        k = 10

        self.page.search_on_home_page(search_input)
        service_name = self.page.get_service_search_results_title(search_input)
        first_ten = len(service_name)
        for i in range(0, first_ten - k):
            service_name.pop()

        print("\n""\n" "Service Names are: " "\n""\n" + "\n".join(service_name))

        xs = search_input
        s = ''.join(xs)

        dict = {'Search Keyword': s, 'Service Name': service_name}
        df = pd.DataFrame(dict)
        df.to_csv(s+".csv")
