import sys
import time
import ssl
import json
import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from pathlib import Path

# Validar nombre de perfil recibido
if len(sys.argv) < 2:
    print("Debés pasar el nombre del perfil de Facebook como argumento.")
    sys.exit(1)

name = sys.argv[1]

# Configuración de Selenium
ssl._create_default_https_context = ssl._create_unverified_context
current_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(current_dir, 'driver', 'chromedriver.exe')
service = Service(driver_path)

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=service, options=options)

# Abrir página de login y esperar inicio manual
driver.get("https://www.facebook.com/login/")
print("Abrí el navegador, iniciá sesión manualmente en Facebook.")
print("Esperando 60 segundos para que completes el login...")
time.sleep(60)  # Espera 60 segundos (podés ajustar el tiempo)
print("Continuando con el scraping...")

# A partir de acá continuás el scraping normalmente
# Ejemplo: ir al perfil de usuario
perfil_url = f"https://www.facebook.com/{name}"
driver.get(perfil_url)
time.sleep(5)


# Buscar el muro
try:
    muro = driver.find_element(By.XPATH, '//div[@role="main"]/div[4]/div[2]/div/div[2]/div[2]')
except Exception as e:
    print("No se encontró el div 'muro':", e)
    driver.quit()
    sys.exit(1)

# Función para normalizar números tipo "8,6 mil"
def normalizar_numero(texto):
    if texto is None:
        return None
    texto = texto.lower().replace(" ", " ").strip()
    match = re.match(r"([\d.,]+)\s*(mil|k)?", texto)
    if not match:
        return None
    numero_str, sufijo = match.groups()
    numero_str = numero_str.replace(',', '.')
    try:
        numero = float(numero_str)
        if sufijo in ['mil', 'k']:
            numero *= 1000
        return int(numero)
    except:
        return None

# Scraping de publicaciones
data = []
publicaciones_extraidas = 0
intentos_maximos = 10

while publicaciones_extraidas < 10 and intentos_maximos > 0:
    publicaciones = muro.find_elements(By.XPATH, './div')

    if publicaciones_extraidas >= len(publicaciones):
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", publicaciones[-1])
        time.sleep(2)
        intentos_maximos -= 1
        continue

    pub = publicaciones[publicaciones_extraidas]
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", pub)
    time.sleep(2)

    try:
        cuerpo = pub.find_element(By.XPATH, './/div[@data-ad-rendering-role="story_message"]')
        texto_cuerpo = cuerpo.text
        emojis_imgs = cuerpo.find_elements(By.XPATH, './/img[@alt]')
        emojis = ''.join([img.get_attribute('alt') for img in emojis_imgs if img.get_attribute('alt')])
        texto_cuerpo += f" {emojis}".strip()
    except Exception:
        texto_cuerpo = "esta publicacion no tiene descripcion"

    fotos = []
    post_id = None
    post_url = None
    reacciones = None
    comentarios = None

    try:
        spans = pub.find_elements(By.XPATH, './/span[contains(@class, "html-span")]')
        for s in spans:
            texto = s.text.strip().lower()
            match = re.search(r'([\d.,]+)\s*(mil|k)?', texto)
            numero_limpio = match.group(0).strip() if match else None

            if "reacci" in texto and not reacciones:
                reacciones = numero_limpio
            elif "comentario" in texto and not comentarios:
                comentarios = numero_limpio
    except Exception as e:
        print("Error extrayendo métricas:", e)

    enlaces = pub.find_elements(By.XPATH, './/a[contains(@href, "/photo/") or contains(@href, "/posts/") or contains(@href, "/videos/")]')
    for enlace in enlaces:
        href = enlace.get_attribute('href')
        if not href:
            continue

        try:
            img = enlace.find_element(By.TAG_NAME, 'img')
            src = img.get_attribute('src')
            if src:
                fotos.append(src)
        except:
            pass

        if 'set=pcb.' in href:
            partes = href.split('set=pcb.')
            if len(partes) > 1:
                posible_id = partes[1].split('&')[0]
                if posible_id.isdigit():
                    post_id = posible_id
                    post_url = f'https://www.facebook.com/{post_id}'
        elif '/posts/' in href:
            match = re.search(r'/posts/([\w:]+)', href)
            if match:
                post_id = match.group(1)
                post_url = href.split('?')[0]
        elif '/videos/' in href:
            match = re.search(r'/videos/(\d+)', href)
            if match:
                post_id = match.group(1)
                post_url = href.split('?')[0]

    data.append({
        "numero": publicaciones_extraidas + 1,
        "texto_cuerpo": texto_cuerpo,
        "fotos": fotos,
        "post_id": post_id,
        "post_url": post_url,
        "reacciones": normalizar_numero(reacciones),
        "comentarios": normalizar_numero(comentarios),
    })

    publicaciones_extraidas += 1
    print(f"Publicación #{publicaciones_extraidas} extraída")

# Guardar en JSON dentro de core/static/core/
output_path = os.path.join(os.path.dirname(__file__), 'static', 'core', 'publicaciones.json')
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Publicaciones guardadas en publicaciones.json")
driver.quit()
