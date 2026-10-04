@echo off
pytest -s -v -m "regressions" --html=./Reports/nopcommercem.html testCases/ --browser edge 
REM pytest -s -v -m "sanity" --html=./Reports/nopcommercem.html testCases/ --browser edge 




::pytest -s -v -m "regressions" --html=./Reports/nopcommercem.html testCases/ --browser firefox
REM pytest -s -v -m "sanity" --html=./Reports/nopcommercem.html testCases/ --browser firefox 