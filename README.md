Ma0 y Leidy Backend

Otro proyectico personal alojado en github.

Inicialmente este es el código del backend que soporta la página https://ma0yleidy.com. Por ahora
esta página es exclusivamente para la invitación de nuestra boda, pero puede evolucionar o puede
simplemente morir como cualquiera de los otros 100 proyectos que tengo alojados en mi github 😅.

Esto es mas para mi que para el lector, entonces

Conectarse al servidor:

keypair: ma0yleidykeypair
host: ec2-34-207-90-63.compute-1.amazonaws.com

Actualizar código

```bash
cd projects/back.ma0yleidy.com
git pull
#sudo nginx -t
#sudo systemctl restart nginx

sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```


Correr migrationes:

```bash
env $(cat /etc/gunicorn/back.ma0yleidy.com.conf| xargs) python ./manage.py migrate
```