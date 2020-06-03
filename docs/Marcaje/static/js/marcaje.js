// function obtenerMarcas(){
//     fetch('/marcaje/')
//     .then(resp => resp.json())
//     .then(data => {
//         console.log(data);
//     })
//     .catch(error => {
//         console.log(error);
//     })
// }

const marcarEntrada = document.querySelector("#btn-entrada");
const marcaSalida = document.querySelector("#btn-salida");

if (marcarEntrada !== null) {
  marcarEntrada.addEventListener("click", function (e) {
    
    this.remove();

    let tipo = "entrada";

    enviarMarca(tipo);
  });
}

if (marcaSalida !== null) {
  marcaSalida.addEventListener("click", function (e) {
    e.preventDefault();

    this.remove();

    let tipo = "salida";

    enviarMarca(tipo);
  });
}

function enviarMarca(tipo) {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  let fd = new FormData();
  fd.append("tipo", tipo);


  fetch("/marcaje/", {
    method: "POST",
    body: fd,
    headers: {
      "X-CSRFToken": csrftoken,
    },
  })
    .then(function (res) {
      return res.json();
    })
    .then((data) => {
      console.log(data);
      if (data.status === 200) {

        let fila = document.getElementById('row-marcas');
        let td = document.createElement('td');
        td.setAttribute('class','text-center');
        td.innerHTML = data.hora;
        fila.appendChild(td);

      } else if (data.status === 300) {
        alert(data.message);
      } else if (data.status === 500) {
        alert(`error de servidor`);
      }
    })
    .catch((data) => {
      alert(data);
    });
};
