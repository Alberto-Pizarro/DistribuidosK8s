package com.kubernetes.app;

import com.kubernetes.app.modelo.NumeroModelo;
import com.kubernetes.app.modelo.PrimosModelo;

import org.springframework.beans.factory.annotation.Value;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@CrossOrigin(origins = "*")
@RestController
public class CalculoController {

  @Value("${kubernetes.python.api.url}")
  private String pythonURL;

  @PostMapping("/calculo")
  public PrimosModelo calculoNumero(@RequestBody NumeroModelo numeroModelo) {

    RestTemplate restTemplate = new RestTemplate();

    return restTemplate.postForEntity(pythonURL + "/primos/calculo", numeroModelo, PrimosModelo.class)
    .getBody();

  }

  @GetMapping("/prueba")
  public void prueba(){

  }
}
