@echo off
echo.
echo  ================================================
echo   STUDENT AI — AWS RDS PostgreSQL
echo   BCA Final Year Project
echo  ================================================
echo.

if not exist ".venv\" (
    echo Creating virtual environment...
    py -m venv .venv
)

call .venv\Scripts\activate.bat

echo Installing packages...
pip install -r requirements.txt -q

echo.
echo IMPORTANT: Make sure your .env file has your RDS details!
echo   DB_HOST=your-rds-endpoint.amazonaws.com
echo   DB_PASS=YourPassword
echo.

echo Starting Flask app...
echo Open browser at: http://localhost:5000
echo.

py app.py
pause
