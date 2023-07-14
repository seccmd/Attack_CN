@echo off

setlocal EnableDelayedExpansion

:: setup a local development environment by creating a virtual environment
:: resoring packages and making sure modules under src path are discoverable to unit tests
if not exist .env (
    echo Creating virtual environment at .env
    python -m venv .env
)

:: we use cmd /k so that the restore and other commands will run inside the scope of the venv terminal
:: in addition && is used so that commands will run only if previous call succeeded (errorlevel neq 0)
echo Activating virtual environment
if "%1"=="" (
    cmd /k ".env\Scripts\activate.bat && pip install mkdocs-material==8.5.3 && mkdocs build && mkdocs serve"
) else (
    echo bad arg "%1" && exit /b 1
)
echo Setup complete

set EX=!errorlevel!
if "%EX%" neq "0" (
    echo Failed to initialize
    popd
    exit /b %EX%
)

exit /b 0