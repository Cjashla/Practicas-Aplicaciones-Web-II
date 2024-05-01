
//4. Crear una función que reciba el arreglo del punto anterior y un ID, y proceder a eliminar el elemento del arreglo.

function eliminarElementoPorID(arr: IvehiculosRegistrados[], id: number): IvehiculosRegistrados[] {
    const index = arr.findIndex(item => item.ID_vehiculo === id);
        if (index !== -1) {
            arr.splice(index, 1);
        }
    return arr;
}

//5. Agregar a la función anterior un Callback que le permita acceder por última vez a los
//datos del elemento eliminado y mostrarlo por consola

function eliminarElementoPorID2(arr: IvehiculosRegistrados[], id: number, callback: (elementoEliminado: IvehiculosRegistrados | null) => void): IvehiculosRegistrados[] {
    const index = arr.findIndex(item => item.ID_vehiculo === id);
    let elementoEliminado: IvehiculosRegistrados | null = null;

    if (index !== -1) {
        elementoEliminado = arr.splice(index, 1)[0];
    }

    if (callback) {
        callback(elementoEliminado);
    }

    return arr;
}

