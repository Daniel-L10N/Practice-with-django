const textos = [" 👋welcomes you to our REST API 🌐", " do not hesitate to contact us 🤗", " we 👨 ‍💻 will always be waiting for you 🤵 🤝 🧑"]; // Agrega los nuevos mensajes que quieras mostrar
let contador = 0;

function typeWriter(texto, i) {
    if (i < texto.length) {
        document.getElementById('texto-cambiante').textContent = texto.substring(0, i + 1);
        setTimeout(() => {
            typeWriter(texto, i + 1);
        }, 100); // Velocidad de escritura
    } else {
        setTimeout(() => {
            deleteAndChangeText();
        }, 1500); // Tiempo antes de borrar y cambiar el texto
    }
}

function deleteAndChangeText() {
    let textoActual = document.getElementById('texto-cambiante').textContent;
    if (textoActual.length > 0) {
        document.getElementById('texto-cambiante').textContent = textoActual.substring(0, textoActual.length - 1);
        setTimeout(() => {
            deleteAndChangeText();
        }, 50); // Velocidad de borrado
    } else {
        contador = (contador + 1) % textos.length;
        typeWriter(textos[contador], 0);
    }
}

typeWriter(textos[contador], 0);