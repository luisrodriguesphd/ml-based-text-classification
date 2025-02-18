set repo_name=ml-based-text-classification


:: Creating virtual environment
call :CreateVirutalEnvironment

:: Install requirements
call :SetupEnvironment


:: Functions

:CreateVirutalEnvironment
:: Create a virtual env
call py -m venv env
:: Activate the virtual env
call .\env\Scripts\activate

:SetupEnvironment
:: Install pip using ensurepip
py -m ensurepip --upgrade
:: Update pip
py -m pip install --upgrade pip
:: Install requirements
pip install -r src\requirements.txt
:: Install the currenct project
pip install -e src\.

