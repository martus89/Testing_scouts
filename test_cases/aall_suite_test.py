import unittest
from unittest.loader import makeSuite
from test_cases.adding_players_test import TestAddPlayer
from test_cases.dashboard_test import TestDashboardPage
from test_cases.players_page_test import TestPlayersDashboardPage
from test_cases.reports_per_player_list_test import TestReportsOfPlayerPage
from test_cases.password_remind_page_test import TestPasswordRemindPage
from test_cases.login_to_the_system_test import TestUserLoginPage
from test_cases.edit_player_from_table_test import TestEditPlayerFromTable
from test_cases.edit_match_test import TestEditMatchPage
from test_cases.matches_list_test import TestMatchesListPage

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestDashboardPage))
   test_suite.addTest(makeSuite(TestUserLoginPage))
   test_suite.addTest(makeSuite(TestPlayersDashboardPage))
   test_suite.addTest(makeSuite(TestReportsOfPlayerPage))
   test_suite.addTest(makeSuite(TestPasswordRemindPage))
   test_suite.addTest(makeSuite(TestMatchesListPage))
   test_suite.addTest(makeSuite(TestEditPlayerFromTable))
   test_suite.addTest(makeSuite(TestEditMatchPage))

   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())