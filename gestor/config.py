import sys
import csv

DATABASE_PATH = '/Users/juanlu_navarro/Documents/Carrera Juan/programacion/Gestor_Proyect_Clientes/gestor/clientes.csv'

if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv'