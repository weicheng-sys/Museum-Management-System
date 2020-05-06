package com.museum.imsub.service;

import com.museum.imsub.entity.Ction;

import java.util.List;

public interface Ctionservice {

    List<Ction> findAll();

    Ction findByid(int id);
}
