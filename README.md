# Materias Guaraní Checker

## Setup

1. Instalar los requirements en entorno virtual y activarlo.
    El código fue desarrollado en Windows.

2. Modificar el cfg json. No se debería tocar el Python.

3. Hay que instalar el webdriver de chrome.


## Al estar funcionando

1. Cuando el python se ejecute, se abrirá una ventana de Chrome con el guaraní ya 
cargado. La contraseña y el usuario se pondrán solos (recordar agregarlos en el json).

2. Apenas se abre la ventana, se cuenta con alrededor de 10 segundos para resolver el
captcha y darle al botón ingresar.

3. Esperar. Se cambiará al link de las materias para inscribirse y ya ahí comienza la magia.

4. Se reiniciará seguidamente esta ventana para ir comprobando. En la consola se verán la
cantidad de comprobaciones que va haciendo. Si se encuentra que se agregaron materias nuevas, 
comenzará a sonar el audio de "alarma.mp3", como si fuera una alarma de Chernobyl. Da gusto.



