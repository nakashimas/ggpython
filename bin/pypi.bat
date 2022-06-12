cd %~dp0/../
call python setup.py bdist_wheel
call python setup.py sdist
@REM call python -m twine upload --repository pypi dist/*
set /p IN="Enter to End"