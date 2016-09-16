abetpujc
========

ABET PUJC


### Para instalar usando virtualenv + python3

Crear el directorio de trabajo:

    mkdir workdir
    cd workdir

Luego crear el ambiente virtual con `pyvenv` y activarlo:

    pyvenv-3.4 venv
    source venv/bin/activate

Para instalar las dependencias requeridas por el proyecto:

    pip3 install -r requirements.txt
    sudo apt-get install wkhtmltopdf
