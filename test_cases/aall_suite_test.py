import unittest
from unittest.loader import makeSuite


from test_cases.adding_players_test import TestAddPlayer
from test_cases.dashboard_test import TestDashboardPage
from test_cases.login_to_the_system_test import TestUserLoginPage
from test_cases.players_page_test import TestPlayersDashboardPage

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestDashboardPage))
   test_suite.addTest(makeSuite(TestUserLoginPage))
   test_suite.addTest(makeSuite(TestPlayersDashboardPage))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())