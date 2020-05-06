package com.museum.imsub.dao;

import com.museum.imsub.entity.Ction;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;
@Mapper
@Repository
public interface CtionDAO {
    List<Ction> findAll();

   Ction findByid(int id);
}
