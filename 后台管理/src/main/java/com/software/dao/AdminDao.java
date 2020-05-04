package com.software.dao;


import com.software.entity.Admin;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
@Repository
public interface AdminDao {

    void update(Admin admin);

    void delete(int id);

    List<Admin> findAll();

    //List<News> findByname(String mname);

    Admin findById(int id);

    void add(Admin admin);

    Admin findByname(String name);

}
