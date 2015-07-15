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

    pip3 install flask
    pip3 install requests
	pip3 install xlsxwriter
	pip3 install pdfkit
	sudo apt-get install wkhtmltopdf