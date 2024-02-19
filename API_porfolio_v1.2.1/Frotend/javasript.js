function crearTarjeta(nombre, edad) {
    const card = document.createElement('div');
    card.classList.add('card');

    const tituloElemento = document.createElement('h2');
    tituloElemento.textContent = "Nombre: "+ nombre;

    const descripcionElemento = document.createElement('p');
    descripcionElemento.textContent = "Edad: "+ edad;

    card.appendChild(tituloElemento);
    card.appendChild(descripcionElemento);

    return card;
  }

  // Función para obtener datos de la API y crear tarjetas
  function obtenerDatosYCrearTarjetas() {
    fetch('http://127.0.0.1:8000/api/v1/programers/')
      .then(response => response.json())
      .then(data => {
        const tarjetasContainer = document.getElementById('tarjetas');
        data.forEach(item => {
          const tarjeta = crearTarjeta(item.fullname, item.age);
          tarjetasContainer.appendChild(tarjeta);
        });
      })
      .catch(error => {
        console.error('Error al obtener datos de la API', error);
      });
  }

  // Llamamos a la función para obtener datos de la API y crear tarjetas
  obtenerDatosYCrearTarjetas();