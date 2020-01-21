package com.k8.web;

import com.k8.web.modelo.PrimoModelo;
import com.k8.web.modelo.ListaModelo;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@CrossOrigin(origins = "*")
@RestController
public class PrimoControlador {

    @Value("${k8.python.api.url}")
    private String apiURL;

    @PostMapping("/criba")
    public ListaModelo obtenerLista(@RequestBody PrimoModelo primoModelo) {
        RestTemplate restTemplate = new RestTemplate();

        return restTemplate.postForEntity(apiURL + "/calculo/criba",
                primoModelo, ListaModelo.class)
                .getBody();
    }

    @GetMapping("/prueba")
    public void prueba() {
    }
}
