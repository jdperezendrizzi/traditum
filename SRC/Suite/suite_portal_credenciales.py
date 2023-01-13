#librerias
import sys
sys.path.append(r"D:\AUTOMATION WEB MEDIFE")
import unittest
import HtmlTestRunner

#ARCHIVOS DONDE SE ENCUENTRAN LOS TEST
from SRC.Test.test_gestion_de_turnos import test_credenciales_002, test_credenciales_003, test_login_001

#INSTANCIA DE LOADER Y SUIT

loader = unittest.TestLoader()
suite = unittest.TestSuite()

#AGREGADO DE TESTS A LA SUITE

suite.addTest(loader.loadTestsFromModule(test_credenciales_001))
suite.addTest(loader.loadTestsFromModule(test_credenciales_002))
suite.addTest(loader.loadTestsFromModule(test_credenciales_003))
# RUNNER Y REPORT HTML

h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Reporte Test credenciales", add_timestamp=False).run(suite)
