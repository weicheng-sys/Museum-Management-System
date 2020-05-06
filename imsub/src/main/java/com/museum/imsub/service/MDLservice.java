package com.museum.imsub.service;

import com.museum.imsub.entity.MDL;

import java.util.List;

public interface MDLservice {
    List<MDL> findAll();
    MDL findByid(int id);
    void update(MDL mdl);
    List<MDL> findBYGrade();
    List<MDL> findBYGrade1();
    List<MDL> findBYGrade2();
    List<MDL> findBYGrade3();
}
