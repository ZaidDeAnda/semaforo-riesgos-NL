<!-- Improved compatibility of Regresar arriba link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://www.nl.gob.mx/igualdadeinclusion">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8WbL6qqsS_z-BJv6k68nJOZK6_IeMVy8-QfrYnm8Njz_A2xWAcqv6dwrZUzb6a9ce8so&usqp=CAU" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Semáforo de riesgos 🚦</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del proyecto</a>
      <ul>
        <li><a href="#alimentos">Alimentos</a></li>
        <li><a href="#desempleo">Desempleo</a></li>
        <li><a href="#noticias">Noticias</a></li>
        <li><a href="#transporte">Transporte</a></li>
      </ul>
    </li>
    <li>
      <a href="#iniciando">Iniciando</a>
      <ul>
        <li><a href="#prerequisitos">Prerequisitos</a></li>
        <li><a href="#instalacion">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#todo">TODO</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

![Frontpage](https://i.imgur.com/jn1F09J.png)

Este proyecto busca ofrecer visualizaciones de datos de importancia para la secretaria de igualdad e inclusión. Cuenta con 4 áreas:
* Alimentos
* Desempleo
* Noticias
* Transporte

Cada una de éstas áreas incluye tanto visualizaciones en la página de streamlit, como scrappers de obtención de datos mediante scripts de consola.

### Alimento

Esta página busca calcular y visualizar la tendencia de inflación entre grupos de alimentos entre 2 periodos de tiempo (1 año por default), mediante gráficas que permiten apreciar cuáles alimentos han sufrido incrementos más grandes, el histórico de la inflación promedia y el top de alimentos que más han sufrido incrementos. También permite una comparación de estos datos entre Ciudad de México y Monterrey

#### Scrapper

Su scrapper obtiene datos de la página de la inegi. Puedes ejecutarlo usando

```bash
./ruta/al/repositorio/semaforo-riesgos-nl/alimentos/scripts/run_scrapper.sh
```

o

```bat
c:/ruta/al/repositorio/semaforo-riesgos-nl/alimentos/scripts/run_scrapper.bat
```

Estos scripts solo llaman al archivo `scrapper.py` (y mover/eliminar algunos archivos), pero debido a que el servidor windows actual no puede ejectuar archivos de windows nativamente, se utiliza el `.bat`.

Este scrapper siempre obtendrá los datos más recientes disponibles, y su correspondiente del año pasado (por ejemplo, de enero de 2024 y de enero de 2023)

### Desempleo

Esta página busca calcular y visualizar la tendencia de desempleo entre varios sectores poblacionales de un trimestre de un año establecido, mediante gráficas que permiten apreciar cuáles sectores de educación sufren de más desempleo, cuáles sectores de edad, porcentaje de desocupación por estado y global, y también una descomposición de salarios

#### Scrapper

Su scrapper obtiene datos de la página de la inegi. Puedes ejecutarlo usando

```bash
./ruta/al/repositorio/semaforo-riesgos-nl/desempleo/scripts/run_scrapper.sh
```

o

```bat
c:/ruta/al/repositorio/semaforo-riesgos-nl/desempleo/scripts/run_scrapper.bat
```

Estos scripts son un poco más complejos que el anterior, puesto que además de llamar a `scrapper.py`, también llaman a `preprocess.py` y `process.py` para el procesado de los datos (y mover/eliminar algunos archivos).

Este scrapper está fijado a un semestre de un año en específico (actualemente, al 4to trimestre de 2022).

### Transporte

Esta página busca calcular y visualizar la tendencia de inflación entre grupos de transporte entre 2 periodos de tiempo (1 año por default), mediante gráficas que permiten apreciar cuáles medios de transporte han sufrido incrementos más grandes, también permititiendo una comparación de estos datos entre Ciudad de México y Monterrey

#### Scrapper

Su scrapper obtiene datos de la página de la inegi. Puedes ejecutarlo usando

```bash
./ruta/al/repositorio/semaforo-riesgos-nl/transporte/scripts/run_scrapper.sh
```

o

```bat
c:/ruta/al/repositorio/semaforo-riesgos-nl/transporte/scripts/run_scrapper.bat
```

Estos scripts solo llaman al archivo `scrapper.py` (y mover/eliminar algunos archivos), pero debido a que el servidor windows actual no puede ejectuar archivos de windows nativamente, se utiliza el `.bat`.

Este scrapper siempre obtendrá los datos más recientes disponibles, y su correspondiente del año pasado (por ejemplo, de enero de 2024 y de enero de 2023)

### Noticias

Esta página busca visualizar las noticias más relevantes de tópicos escogidos que sean de interés (por ejemplo, "Nuevo León", "Samuel García", etc)

#### Scrapper

Su scrapper obtiene datos de la página de la inegi. Puedes ejecutarlo usando

```bash
./ruta/al/repositorio/semaforo-riesgos-nl/noticias/scripts/run_scrapper.sh
```

o

```bat
c:/ruta/al/repositorio/semaforo-riesgos-nl/noticias/scripts/run_scrapper.bat
```

Estos scripts son un poco más complejos que el anterior, puesto que funcionan con una "base de datos". Es decir, primero se inicializa una base de datos de noticias, en los scripts

```bash
./ruta/al/repositorio/semaforo-riesgos-nl/noticias/scripts/init_scrapper.sh
```

o

```bat
c:/ruta/al/repositorio/semaforo-riesgos-nl/noticias/scripts/init_scrapper.bat
```

Que tienen hard-codeado un set de semanas para las cuales buscaran noticias. Una vez inicializado, cada semana se ejecutan los `run_scrapper` normales, que solo añaden las noticias de la última semana a esta base de datos.

<p align="right">(<a href="#readme-top">regresar arriba</a>)</p>


<!-- GETTING STARTED -->
## Iniciando

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
Para poder ejecutar el proyecto en tu local, sigue estos pasos:

### Prerequisitos

* Python
* Powershell/bash
* Chromedriver (debe estar en la carpeta del repo)

### Instalación

Creamos un entorno virtual de python
```bash
python -m venv venv
```

Entramos al entorno virtual.
Para windows:
```bash
source venv/Scripts/activate
```

Para mac/linux:
```bash
source venv/bin/activate
```

Luego instalamos los requisitos

```bash
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">Regresar arriba</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Para levantar la página de streamlit, ejecuta:

```bash
streamlit run app.py
```


<p align="right">(<a href="#readme-top">Regresar arriba</a>)</p>



<!-- ROADMAP -->
## TODO

- [ ] Automatizar scrapper de noticias
- [ ] Centralizar todos los utils para que pueda ser refactorizado
- [ ] Refactorizar los scrappers para poder ejecutarlos de mejor manera (por ejemplo, que sea más fácil cambiar las fechas)

<p align="right">(<a href="#readme-top">Regresar arriba</a>)</p>


<!-- CONTACT -->
## Contacto

Zaid De Anda - zaidy.deanda@gmail.com

Project Link: [https://github.com/ZaidDeAnda/semaforo-riesgos-nl](https://github.com/ZaidDeAnda/semaforo-riesgos-nl)

<p align="right">(<a href="#readme-top">Regresar arriba</a>)</p>
