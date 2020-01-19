package com.kubernetes.app.modelo;

public class NumeroModelo{
  private String numero;

  public NumeroModelo(){

  }

  public String getNumero(){
    return numero;
  }

  public void setNumero(String numero){
    this.numero = numero;
  }

  @Override
  public String toString(){
    return numero;
  }
}
