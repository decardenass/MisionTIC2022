package misiontic2022.co.edu.unal.decardenass;

public class ComputadoresPortatiles extends Computadores {
    // Atributos
    private final static Integer PULGADAS_BASE = 20;
    private Integer pulgadas;
    private boolean camaraITG;

    // Constructores
    public ComputadoresPortatiles() {
        this.precioBase = PRECIO_BASE;
        this.peso = PESO_BASE;
        this.consumoW = CONSUMO_W;
        this.pulgadas = PULGADAS_BASE;
        this.camaraITG = false;
    }

    // Constructor
    public ComputadoresPortatiles(Double precioBase, Integer peso) {
        // this.peso = peso;
        // this.precioBase = precioBase;
        super(precioBase, peso);
        this.consumoW = CONSUMO_W;
        this.pulgadas = PULGADAS_BASE;
        this.camaraITG = false;
    }

    public ComputadoresPortatiles(Double precioBase, Integer peso, char consumoW, Integer pulgadas, boolean camaraITG) {
        // this.peso = peso;
        // this.precioBase = precioBase;
        super(precioBase, peso, consumoW);
        this.pulgadas = pulgadas;
        this.camaraITG = camaraITG;
    }

    // Métodos
    public Double calcularPrecio() {
        Double adicion = super.calcularPrecio();
        if (pulgadas > 40) {
            adicion += precioBase * (30.0 / 100.0);
        }

        if (camaraITG) {
            adicion += 50;
        }

        return adicion;
    }

    public Integer getPulgadas() {
        return pulgadas;
    }

    public boolean isCamaraITG() {
        return camaraITG;
    }

}
