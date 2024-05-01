
//1. Definir un objeto por cada entidad asignada (3 entidades).
const vehiculo:Ivehiculo={
    ID:1,
    Descripcion:`KIA Picanto`,
    Placa:`ABC1234`,
    Color:`Gris`
}

const EspacioParqueo:Iespacioparqueo ={
    ID:1,
    DescripcionParqueo:`Parroquia Leonidas Proaño`
}

const Parquear:Iparquear={
    ID:1,
    ID_vehiculo:1,
    ID_parqueo:1,
    FechayhoraEntrada:`14-02-2023 -- 15:00`,
    FechayhoraSalida:`14-02-2023 -- 22:00`,
//3. Crear un arreglo de objetos basándose en la entidad transaccional con por lo menos 3 elementos.
    VehiculosRegistrados:[
        {ID_vehiculo:1,Placa:`ABC1234`,DescripcionParqueo:`Parroquia Leonidas Proaño`},
        {ID_vehiculo:2,Placa:`DEF1234`,DescripcionParqueo:`Barrio Las cumbres`},
        {ID_vehiculo:3,Placa:`GHI1234`,DescripcionParqueo:`Parroquia San Jose`}
    ]
}

