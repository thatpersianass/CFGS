// let miPersona = {
//     nombre: "Juan",
//     edad: 30,
//     saludo: function(){
//         return this.nombre+" tiene "+this.edad+" años";
//     },

//     sumarEdad: function(){
//         ++this.edad;
//     },
// };

// let persona5 = [miPersona.nombre, miPersona.edad, miPersona.genero];    

// for (let i in persona5) {
//     window.alert(persona5[i]);
// }

// window.alert(miPersona.saludo());

// miPersona.sumarEdad();

// window.alert(miPersona.saludo());

// let a = 7;
// let x=a;
// ++x;

// window.alert(a+""+x);

function persona5(pnombre,pedad,pgenero){
    this.nombre = pnombre;
    this.edad = pedad;
    this.genero = pgenero;
}

let miPersona = new persona5("Angel",27,"hombre")

let a = new persona5("ana",18,"mujer")

window.alert(miPersona.nombre + " " + miPersona.edad + " " + miPersona.genero);
window.alert(a.nombre + " " + a.edad + " " + a.genero);
miPersona.colorPelo="azul";
window.alert(miPersona.nombre + " " + miPersona.edad + " " + miPersona.genero + "" + miPersona.colorPelo);

delete miPersona.colorPelo;

window.alert(miPersona.nombre + " " + miPersona.edad + " " + miPersona.genero + "" + miPersona.colorPelo);