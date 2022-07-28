package misiontic2022.co.edu.unal.decardenass;

public class ComputadoresMesa extends Computadores {
    // Atributos
    private final static Integer ALMACENAMIENTO_BASE = 50;
    private Integer almacenamiento;

    // Constructores
    public ComputadoresMesa() {
        this.precioBase = PRECIO_BASE;
        this.peso = PESO_BASE;
        this.consumoW = CONSUMO_W;
        this.almacenamiento = ALMACENAMIENTO_BASE;
    }

    public ComputadoresMesa(Double precioBase, Integer peso) {
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = CONSUMO_W;
        this.almacenamiento = ALMACENAMIENTO_BASE;
    }

    public ComputadoresMesa(Double precioBase, Integer peso, char consumoW, Integer almacenamiento) {
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = consumoW;
        this.almacenamiento = almacenamiento;
    }

    // Métodos
    public Double calcularPrecio() {
        Double adicion = super.calcularPrecio();
        if (almacenamiento > 100) {
            adicion += 50;
        }

        return adicion;
    }

    public Integer getAlmacenamiento() {
        return almacenamiento;
    }

}
