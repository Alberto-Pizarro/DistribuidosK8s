package com.k8.web.modelo;

public class ListaModelo {

    private String lista;
    private float tiempo;

    public ListaModelo() {
    }

    public ListaModelo(String lista, float tiempo) {
        this.lista = lista;
        this.tiempo = tiempo;
    }

    public String getLista() {
        return lista;
    }

    public void setLista(String lista) {
        this.lista = lista;
    }

    public float getTiempo() {
        return tiempo;
    }

    public void setTiempo(float tiempo) {
        this.tiempo = tiempo;
    }

    @Override
    public String toString() {
        return "ListaModelo{" +
                "lista=" + lista + '\'' +
                ", tiempo=" + tiempo +
                '}';
    }
}
