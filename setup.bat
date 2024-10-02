@echo off

:: Exibe uma mensagem de início
echo Criando o ambiente virtual...

:: Criação do ambiente virtual
python -m venv venv

:: Verifica se o ambiente virtual foi criado com sucesso
if exist venv (
    echo Ambiente virtual criado com sucesso!
) else (
    echo Falha ao criar o ambiente virtual.
    exit /b 1
)

:: Ativa o ambiente virtual
echo Ativando o ambiente virtual...
call venv\Scripts\activate

:: Verifica se o ambiente virtual foi ativado
if errorlevel 1 (
    echo Falha ao ativar o ambiente virtual.
    exit /b 1
)

:: Instala as dependências do requirements.txt
echo Instalando dependências...
pip install -r requirements.txt

:: Verifica se as dependências foram instaladas com sucesso
if errorlevel 1 (
    echo Falha ao instalar as dependências.
    exit /b 1
)

:: Executa a aplicação
echo Iniciando a aplicação...
start /b python app.py

:: Aguarda 2 segundos para garantir que a aplicação tenha tempo para iniciar
timeout /t 2 /nobreak >nul

:: Abre o navegador na URL da aplicação
start http://127.0.0.1:5000

:: Exibe uma mensagem de sucesso
echo Setup concluído! Ambiente virtual ativado, dependências instaladas, aplicação iniciada e navegador aberto.

pause
