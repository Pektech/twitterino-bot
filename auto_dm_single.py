import tweepy
from config import *

get_user = api.followers("rvfuturoayerhoy")
print(get_user[0].screen_name,get_user[0].name)

#message = "Hola {0}, ya conoces nuestra revista? Somos una revista que le interesa promover la lectura y a escritores que no han tenido la oportunidad de publicar sus obras, actualmente el primer numero de este anyo de la revista \"El futuro del ayer, hoy\" se encuentra disponible en Amazon por un costo minimo y de forma gratuita en Google Books, mas abajo te entregamos las ligas para que puedas obtener tu numero. Agradecemos tambien cualquier apoyo, tanto mandando esta informacion a escritores en busca de publicar su primera obra, lectores en busca de nuevos textos o simplemente con un like o retweet a nuestras convocatorias y textos en nuestra cuenta @rvfuturoayerhoy. Saludos, Comite Editorial \"El futuro del ayer, hoy\" #lee #escribe #comparte\nAmazon Digital: https://www.amazon.es/dp/B07F3HHSS5\nAmazon Fisico: https://www.amazon.es/dp/1983300993\nGoogle Books: https://bit.ly/2N5M9VE"
#x = api.send_direct_message("vicosurge",text=message.format("Vicente Munoz"))
#print(x)