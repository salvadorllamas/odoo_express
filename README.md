# Instalando Odoo con docker
<p align="center">
  <img src="https://www.arsys.es/blog/file/uploads/2016/06/Qu%C3%A9-aporta-Odoo-a-mi-negocio.jpg" alt="odoo" width="50"/>
  <br><br>
	<img src="https://img.shields.io/badge/version-1.1.2-green.svg?style=for-the-badge">
  <a href="https://www.digitalocean.com/?refcode=9f8258252636&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge">
  <img src="https://img.shields.io/badge/Digital Ocean-$100-green.svg?style=for-the-badge">
  </a>

</p>


Una solución flexible y rápida para implementar multiples instancias de `Odoo` en un servidor. Algunas razónes por las que usted podría usar esta guía.
- Versiones soportados de [**Odoo**][odoo] (`12.0`, `12`, `13.0`, `13`, `14.0`, `14`, `latest`).
- Versiones soportados de [**PostgreSQL**][postgres](`10`, `11`, `12`, `13`, `alpine`, `latest`).
- Configuración optimizada para entorno de desarrollo y producción.
- Integración con **Nginx Proxy Manager**.

## Artítulos relacionados
- [Docker Official Images][odoo]
- [Nginx Proxy Manager][proxy]

## Requerimientos
- [Docker][docker]
- [Docker Compose][docker-compose]


## Detener y reiniciar una instancia de Odoo
Ejecute estas instrucciones en un proyecto de **Odoo**.

**Iniciar**
```bash
docker-compose up -d
```
**Reiniciar**
```bash
docker-compose restart
```
**Detener**
```bash
docker-compose down
```

## Entorno de desarrollo
    El finalizar la ejecución del comando, se creará una estructra similar a ésta.
    ```bash
    ├── controllers
    │   ├── controllers.py
    │   └── __init__.py
    ├── demo
    │   └── demo.xml
    ├── __init__.py
    ├── __manifest__.py
    ├── models
    │   ├── __init__.py
    │   └── models.py
    ├── security
    │   └── ir.model.access.csv
    └── views
        ├── templates.xml
        └── views.xml
    ```


## Dónde se almacenan los Datos

**Nota importante:** Hay varias maneras de guardar los datos usados por las aplicaciones que se ejecutan en contenedores docker. Animamos a los usuarios de las a familiarizarse con las [`opciones disponibles`][volumes].


## Mi web salvador llamas
[web]:http://salvadorllamas.com

