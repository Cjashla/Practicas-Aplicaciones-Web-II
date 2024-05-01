
//2. Definir una interfaz por cada objeto y asignarla como tipo de objeto.
interface Ivehiculo{
    ID:number,
    Descripcion:string,
    Placa:string,
    Color:string
}
interface Iespacioparqueo{
    ID:number,
    DescripcionParqueo:string
}
interface Iparquear{
    ID:number,
    ID_vehiculo:number,
    ID_parqueo:number,
    FechayhoraEntrada:string,
    FechayhoraSalida:string,
    VehiculosRegistrados:IvehiculosRegistrados[]
}
interface IvehiculosRegistrados{
    ID_vehiculo:number,
    Placa:string,
    DescripcionParqueo:string
}

  
  
