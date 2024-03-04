from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Completar las siguientes variables
LEGAJO = 47773
PASSWORD = ""
MATERIA = ""  # No es necesario que sea el nombre completo, puede ser un nombre parcial
POS = 1  # posicion de la opcion de la comision de arriba par abajo (arrancando en 1). Si una comision se queda sin cupos puede pasar cualquier cosa
# ----------------------------------------------------------------------------------------------------

def main():
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")  # for Chrome >= 109
        driver = webdriver.Chrome(options=chrome_options)
        while True:
            driver.get("https://alumnos.frro.utn.edu.ar/menuAlumno.asp")

            if "login" in driver.current_url:
                print("Pantalla login")
                driver.find_element(By.NAME, "legajo").send_keys(LEGAJO)
                driver.find_element(By.NAME, "password").send_keys(PASSWORD)
                driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

            if "menuAlumno" in driver.current_url:
                print("Pantalla menu alumno")
                driver.find_element(
                    By.XPATH,
                    f"// *[contains(text(), 'Inscripción a cursado')]",
                ).click()

            if "materiasCursado" in driver.current_url:
                print("Pantalla lista cursado")
                driver.save_screenshot("estado.png")
                index = 0
                lines = driver.find_elements(By.CSS_SELECTOR, ".textoTabla")
                for line in lines:
                    if MATERIA in line.text:
                        break
                    index += 1
                anchors = driver.find_elements(By.CSS_SELECTOR, "a")
                print(str(index) + " " + lines[index].text + " encontrado")
                anchors[index].click()

            if "cursosCursado" in driver.current_url:
                print("Pantalla comisiones")
                driver.find_element(By.CSS_SELECTOR, f"[value='{POS}']").click()
                driver.save_screenshot(MATERIA + "-comision.png")

                driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
                print("Creo que te anotaste")
                driver.save_screenshot(MATERIA + "-certificado.png")
                exit()

    finally:
        driver.quit() if driver != None else "¯|_(ツ)_/¯"


if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as err:
            print(err)
