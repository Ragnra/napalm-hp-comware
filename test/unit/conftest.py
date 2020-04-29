"""Test fixtures."""
from builtins import super

import pytest
from napalm.base.test import conftest as parent_conftest

from napalm.base.test.double import BaseTestDouble

from napalm_hp_comware import hp_comware


@pytest.fixture(scope='class')
def set_device_parameters(request):
    """Set up the class."""
    def fin():
        request.cls.device.close()
    request.addfinalizer(fin)

    request.cls.driver = hp_comware.HpComwareDriver
    request.cls.patched_driver = PatchedHPComwareDriver
    request.cls.vendor = 'hp_comware'
    parent_conftest.set_device_parameters(request)


def pytest_generate_tests(metafunc):
    """Generate test cases dynamically."""
    parent_conftest.pytest_generate_tests(metafunc, __file__)


class PatchedHPComwareDriver(hp_comware.HpComwareDriver):
    """Patched Skeleton Driver."""

    def __init__(self, hostname, username, password, timeout=60, optional_args=None):
        """Patched Skeleton Driver constructor."""
        super().__init__(hostname, username, password, timeout, optional_args)

        self.patched_attrs = ['device']
        self.device = FakeHPComwareDevice()


    def disconnect(self):
        pass

    def open(self):
        pass


class FakeHPComwareDevice(BaseTestDouble):
    """Skeleton device test double."""

    def run_commands(self, command_list, encoding='json'):
        """Fake run_commands."""
        result = list()

        for command in command_list:
            filename = '{}.txt'.format(self.sanitize_text(command))
            full_path = self.find_file(filename)

            result.append(self.read_txt_file(full_path))

        return result
    
    def send_command(self, command):
        filename = '{}.txt'.format(self.sanitize_text(command))
        full_path = self.find_file(filename)
        return self.read_txt_file(full_path)


    def send_command_timing(self, command):
        return self.send_command(command)

    def disconnect(self):
        pass