package com.museum.imsub.dao;

import com.museum.imsub.entity.MDL;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;
@Mapper
@Repository
public interface MDLDAO {
    List<MDL> findAll();
    MDL findByid(int id);
    List<MDL> findBYGrade();
    List<MDL> findBYGrade1();
    List<MDL> findBYGrade2();
    List<MDL> findBYGrade3();
    void update(MDL mdl);
}
