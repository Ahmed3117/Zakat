### data types :
* numeric , decimal :
```sql
SELECT CAST(123 AS DECIMAL(5,2)) -- 123.00 
SELECT CAST(12345.12 AS NUMERIC(10,5)) -- 12345.12000
```
* real , float :
```sql
SELECT CAST( PI() AS FLOAT) -- 3.14159265358979 
SELECT CAST( PI() AS REAL) -- 3.141593
```
* integer :
	bigint
	int
	smallint
	tinyint
* money , smallmoney
* VARCHAR , CHAR :
```sql
SELECT CAST('ABC' AS CHAR(10)) -- 'ABC        '  هيحجز الاماكن كلها حتى لو مش هتستخدم
SELECT CAST('ABC' AS VARCHAR(10)) -- 'ABC' 
SELECT CAST('ABCDEFGHIJKLMNOPQRSTUVWXYZ' AS CHAR(10)) -- 'ABCDEFGHIJ'
```
