
//Ejecucion del punto 4
const idAEliminar = 2; 
const nuevoArreglo = eliminarElementoPorID(Parquear.VehiculosRegistrados, idAEliminar);
console.log(nuevoArreglo);


//Ejecucion del punto 5
const idAEliminar2 = 2; 
const nuevoArreglo2 = eliminarElementoPorID2(Parquear.VehiculosRegistrados, idAEliminar2, elementoEliminado => {
    if (elementoEliminado) {
        console.log("Elemento eliminado:");
        console.log(elementoEliminado);
    } else {
        console.log("No se encontró ningún elemento con el ID proporcionado.");
    }
});
console.log(nuevoArreglo2);
