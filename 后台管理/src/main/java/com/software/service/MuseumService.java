package com.software.service;

import com.software.entity.Museum;

import java.util.List;

public interface MuseumService {

    void update(Museum museum);

    void delete(String id);

    List<Museum> findAll();

    Museum findById(String id);

    List<Museum> findByname(String name);

}
