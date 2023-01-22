"""CREATE PROCEDURE get_data_by_period
    @start_date DATE,
    @end_date DATE
AS
BEGIN
    SELECT * FROM Employee
    WHERE Date BETWEEN @start_date AND @end_date
END"""
from connection_db import Connection


cursor = Connection.cursor()

start_date = '2022-01-01'
end_date = '2022-12-31'

cursor.execute("EXEC get_data_by_period @start_date = ?, @end_date = ?", start_date, end_date)
data = cursor.fetchall
