package com.kubernetes.app.modelo;

public class PrimosModelo{
  private String primos;
  private float tiempo;

  public PrimosModelo(){

  }

  public PrimosModelo(String primos, float tiempo){
    this.primos = primos;
    this.tiempo = tiempo;
  }

  public String getPrimos(){
    return primos;
  }

  public float getTiempo(){
    return tiempo;
  }

  public void setPrimos(String primos){
    this.primos = primos;
  }

  public void setTiempo(float tiempo){
    this.tiempo = tiempo;
  }

  @Override
  public String toString(){
    return "PrimosModelo{" +
            "primos='" + primos + '\'' +
            ", tiempo=" + tiempo +
            '}';
  }
}
