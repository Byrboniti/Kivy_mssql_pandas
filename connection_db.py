import pyodbc

Connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'
                            'SERVER=.;'
                            'DATABASE=Testdb;'
                            'Trusted_Connection=Yes')