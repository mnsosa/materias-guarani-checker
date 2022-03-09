import json
import time
import vlc

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def ver_lista_materias(driver):
    success = False
    while not success:
        try:
            driver.get("https://autogestion.guarani.unc.edu.ar/cursada")
            success = True
        except Exception as e:
            print(e)
 
def esperar_materias_nuevas():
    # cfg data from json file
    cfg_file = open('cfg.json') 
    cfg = json.load(cfg_file)
    cfg_file.close()

    # SETUP
    driver_path = cfg["driver_path"]

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

    # Acceder a la aplicación web
    driver.get("https://autogestion.guarani.unc.edu.ar/")

    print("\n", "*"*50)
    print("HACER CAPTCHA Y APRETAR INGRESAR. LUEGO ESPERAR. SE TIENEN 10 SEGUNDOS PARA ESTO.")
    print("*"*50, "\n")

    usuario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='usuario']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    usuario.send_keys(cfg["user"])
    password.send_keys(cfg["password"])

    # Resolver CAPTCHA Y TOCAR INGRESAR
    time.sleep(14)

    ver_lista_materias(driver)

    materias_nuevas = False

    materias_full_xpath = "/html/body/div[6]/div[2]/div[1]/div/div[3]/ul"

    success = False
    while not success:
        try:
            lista_materias = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, 
                                materias_full_xpath))).text.split()
            cant_materias = len(lista_materias)
            success = True
        except Exception as e:
            print("Intentando primera lectura nuevamente...\n")
            print("ERROR:\n")
            print(e, "\n")

    print("\n", "*"*50)
    print(lista_materias)
    print("*"*50, "\n")

    count = 0
    while not materias_nuevas:
        try:        
            lista_materias_2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, 
                                materias_full_xpath))).text.split()
            cant_materias_2 = len(lista_materias_2)
            print(f"Comprobando materias nuevas... [{count}]")
            count += 1
        except Exception as e:
            print("No se pudo checkear lista nueva por esta vez.")
            print(e, "\n")

        # Si no coinciden la cantidad de palabras entonces hay materias nuevas
        if cant_materias != cant_materias_2:
            materias_nuevas = True
            print("\n", "*"*50)
            print(lista_materias)
            print("*"*50, "\n")

        time.sleep(2)                
        ver_lista_materias(driver)

    
    p = vlc.MediaPlayer(r"\alarma.mp3")
    p.play()
    time.sleep(200)


if __name__ == '__main__':
    esperar_materias_nuevas()

