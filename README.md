# desafio-modulo8

**Automatización de la creación de un bucket S3 y sincronización de archivos con GitHub Actions**

Este proyecto simplifica la creación de un bucket en Amazon S3 y la sincronización de archivos desde un repositorio de GitHub. Al utilizar GitHub Actions y el SDK de AWS para Python (boto3), se automatiza todo el proceso, desde la creación del bucket hasta la configuración de permisos.

## Cómo usar

1. **Crear un nuevo repositorio:** Forkea este repositorio en tu cuenta de GitHub.
2. **Configurar secretos:**
   * Ve a Settings > Secrets and variables > Actions.
   * Agrega los siguientes secretos con tus credenciales de AWS:
     * `AWS_ACCESS_KEY_ID`
     * `AWS_SECRET_ACCESS_KEY`
     * `S3_BUCKET_NAME`
     * `S3_USER`
     * `S3_USER_ACCESS_KEY_ID`
     * `S3_USER_SECRET_ACCESS_KEY`
     * `AWS_REGION`
3. **Ejecutar el flujo de trabajo:**
   * Haz un commit y push a tu repositorio.
   * El flujo de trabajo se ejecutará automáticamente, creando el bucket (si no existe) y sincronizando los archivos.

## Detalles Técnicos

* **Estructura:**
  * `create_bucket.py`: Crea el bucket y asigna una política de acceso específica al usuario de S3.
  * `workflow.yml`: Define el flujo de trabajo de GitHub Actions.
* **Política de acceso:** La política de acceso permite al usuario de S3 realizar operaciones de subida y descarga en el bucket. Esto garantiza que solo el usuario autorizado pueda acceder a los archivos.
