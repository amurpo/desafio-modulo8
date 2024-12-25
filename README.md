[![Sync to S3](https://github.com/amurpo/desafio-modulo8/actions/workflows/sync-s3.yml/badge.svg)](https://github.com/amurpo/desafio-modulo8/actions/workflows/sync-s3.yml)

# desafio-modulo8
Creacion de Bucket S3 con GitHub Action

Este proyecto tiene como objetivo crear un bucket en Amazon S3 (si no existe) y sincronizar archivos desde un repositorio de GitHub hacia ese bucket. El código utiliza Python y AWS SDK (boto3) para la creación del bucket y la configuración de la política de acceso.
Archivos principales:

    create_bucket.py: Script Python que crea un bucket S3 y asigna una política de acceso específica a un usuario de S3.
    workflow.yml: Archivo de flujo de trabajo de GitHub Actions que automatiza el proceso de creación del bucket y sincronización de archivos con el bucket S3.

Requisitos

    Una cuenta de AWS con un usuario que tenga permisos de administración para crear y gestionar buckets S3.
    Variables de entorno configuradas para interactuar con AWS, incluyendo el nombre del bucket, el ARN del usuario de S3, y la región de AWS.

Dependencias

    boto3: SDK de AWS para Python.
    pyyaml: Para la carga de configuraciones si es necesario.

Para instalar las dependencias:

pip install boto3 pyyaml

Configuración de GitHub Actions
workflow.yml

Este archivo se encuentra dentro del directorio .github/workflows/ y tiene dos trabajos principales:

    check_and_create:
        Verifica si el bucket S3 ya existe.
        Si no existe, crea el bucket y le asigna una política de acceso que permite a un usuario S3 específico realizar operaciones PutObject y GetObject en el bucket.

    sync_files:
        Sincroniza los archivos del repositorio con el bucket S3, excluyendo ciertos archivos y directorios (como .git, .github, README.md, etc.).

Variables de entorno

Las siguientes variables de entorno deben ser configuradas en los Secretos de GitHub (a través de la configuración de tu repositorio en GitHub):

    AWS_ACCESS_KEY_ID: Clave de acceso del administrador de AWS.
    AWS_SECRET_ACCESS_KEY: Clave secreta del administrador de AWS.
    S3_BUCKET_NAME: Nombre del bucket S3 que será creado o sincronizado.
    S3_USER: ARN del usuario S3 autorizado para interactuar con el bucket.
    S3_USER_ACCESS_KEY_ID: Clave de acceso del usuario S3.
    S3_USER_SECRET_ACCESS_KEY: Clave secreta del usuario S3.
    AWS_REGION: La región de AWS donde el bucket será creado.

Uso

    Configurar los secretos de GitHub: Dirígete a tu repositorio de GitHub, ve a Settings > Secrets and variables > Actions y agrega los siguientes secretos:
        AWS_ACCESS_KEY_ID
        AWS_SECRET_ACCESS_KEY
        S3_BUCKET_NAME
        S3_USER
        S3_USER_ACCESS_KEY_ID
        S3_USER_SECRET_ACCESS_KEY
        AWS_REGION

    Desplegar el flujo de trabajo: Cada vez que se haga un push o un pull request a la rama main, GitHub Actions ejecutará el flujo de trabajo. Primero verificará si el bucket S3 existe, lo creará si es necesario, y luego sincronizará los archivos del repositorio con el bucket.

Scripts
create_bucket.py

Este script crea un bucket en S3 si no existe y asigna una política de acceso al bucket. La política permite que un usuario S3 específico suba y descargue archivos del bucket.
workflow.yml

El flujo de trabajo de GitHub Actions ejecuta los pasos necesarios para crear el bucket y sincronizar archivos desde tu repositorio de GitHub hacia S3.
