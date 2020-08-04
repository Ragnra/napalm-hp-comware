"""Tests for getters."""

from napalm.base.test.getters import BaseTestGetters, wrap_test_cases


import pytest


@pytest.mark.usefixtures("set_device_parameters")
class TestGetter(BaseTestGetters):
    """Test get_* methods."""


    @wrap_test_cases
    def test_get_iproute_table(self, test_case):
        """test get_ip_route_table()"""

        get_iproute_table = self.device.get_iproute_table()
        assert len(get_iproute_table) > 0

        return get_iproute_table