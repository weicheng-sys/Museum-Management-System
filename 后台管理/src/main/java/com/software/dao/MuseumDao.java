package com.software.dao;

import com.software.entity.Museum;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
@Repository
public interface MuseumDao {

    void update(Museum museum);

    void delete(String id);

    List<Museum> findAll();

    Museum findById(String id);

    List<Museum> findByname(String name);

}
