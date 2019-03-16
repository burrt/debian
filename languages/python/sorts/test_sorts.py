import pytest
import random
from sorts import Sorter

Sorter = Sorter()
correct_sorted_positive_numbers = list(range(0, 30))

class TestBoundaries:
    common_test_data = [
        ([]),
        ([None]),
    ]

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_bubble_sort_with(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.bubble_sort(sorted_numbers)

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_insertion_sort(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.insertion_sort(sorted_numbers)

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_selection_sort(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.selection_sort(sorted_numbers)

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_merge_sort(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.merge_sort(sorted_numbers)

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_quick_sort_hoare_partition(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.quick_sort(sorted_numbers, 0, len(sorted_numbers)-1, "quick_h")

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_quick_sort_lomuto_partition(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.quick_sort(sorted_numbers, 0, len(sorted_numbers)-1, "quick_l")

        assert sorted_numbers == sorted(sorted_numbers)


class TestValidNumbers:
    common_test_data = [
        (sorted((range(-100, 100)), key = lambda x: random.random())),
        (list(reversed((range(-100, 30))))),
        ([random.uniform(-100, 100) for _ in range(0, 100)]),
        ([1] * 200),
        ([1])
    ]

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_bubble_sort_with(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.bubble_sort(sorted_numbers)

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_insertion_sort(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.insertion_sort(sorted_numbers)

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_selection_sort(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.selection_sort(sorted_numbers)

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_merge_sort(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.merge_sort(sorted_numbers)

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_quick_sort_hoare_partition(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.quick_sort(sorted_numbers, 0, len(sorted_numbers)-1, "quick_h")

        assert sorted_numbers == sorted(sorted_numbers)

    @pytest.mark.parametrize("testdata", common_test_data)
    def test_quick_sort_lomuto_partition(self, testdata):
        sorted_numbers = list(testdata)
        Sorter.quick_sort(sorted_numbers, 0, len(sorted_numbers)-1, "quick_l")

        assert sorted_numbers == sorted(sorted_numbers)
