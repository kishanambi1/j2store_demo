@ECHO OFF
REM pytest -m "sanity" Test_Cases/ -rA --html=./Reports/report.html

REM pytest -m "regression" Test_Cases/ -rA --html=./Reports/report.html

pytest -m "sanity or regression" Test_Cases/ -rA --html=./Reports/report.html

REM pytest -m "sanity and regression" Test_Cases/ -rA --html=./Reports/report.html


pause