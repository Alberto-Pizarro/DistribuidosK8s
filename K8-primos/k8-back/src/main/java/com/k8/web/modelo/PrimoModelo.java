package com.k8.web.modelo;


public class PrimoModelo {
    private String lista;

    public PrimoModelo() {
    }

    public String getLista() {
        return lista;
    }

    public void setLista(String lista) {
        this.lista = lista;
    }

    @Override
    public String toString() {
        return lista;
    }
}
