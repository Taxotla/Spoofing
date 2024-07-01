# Spoofing
Repositorio ultima tarea ciberseguridad

CREACION DE UN SUPLANTADOR UNICO CON SCAPY.

Los siguientes scripts muestran un breve ejemplo de un ataque de suplantación y su defensa utilizando Scapy. El primero utiliza Scapy para funciones ARP, enviando específicamente paquetes ARP falsos para interceptar el tráfico de red de una IP objetivo y usando la IP del Gateway. Dado que ARP funciona con direcciones MAC, podemos suplantar dispositivos en la misma red.

Para ejecutar el script de ataque, necesitamos permisos de superusuario; por lo tanto, escribe 'sudo' antes del comando del script y luego ingresa la IP objetivo y la IP del Gateway.

Para ejecutar el script de defensa (honeypot), necesitas permisos de red; por lo tanto, usa sudo python3 mas el nombre del archivo

Al detectar suplantación (modificaciones en la tabla ARP), se mostrará un mensaje de registro en la terminal y se creará un archivo .txt en la ubicación del script.



