package com.example.springbootdeviceapp;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DeviceService {
    private final RestTemplate restTemplate;

    public DeviceService(RestTemplateBuilder restTemplateBuilder) {
        this.restTemplate = restTemplateBuilder.build();
    }

    public Device predictPrice(Device device) {
        String url = "http://localhost:5000/predict"; 
        HttpEntity<Device> request = new HttpEntity<>(device);
        try {
            ResponseEntity<Device> response = restTemplate.postForEntity(url, request, Device.class);
            return response.getBody();
        } catch (HttpClientErrorException | HttpServerErrorException e) {
            // Handle HTTP errors here
            System.out.println("HTTP Error: " + e.getStatusCode() + " - " + e.getStatusText());
        } catch (RestClientException e) {
            // Handle other RestClientException errors here
            System.out.println("Error: " + e.getMessage());
        }
        return null;
    }
}

}
