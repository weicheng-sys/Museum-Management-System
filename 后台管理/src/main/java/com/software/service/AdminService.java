package com.software.service;

import com.software.entity.Admin;

import java.util.List;

public interface AdminService {
    void update(Admin admin);

    void delete(int id);

    List<Admin> findAll();

    //List<News> findByname(String mname);

    Admin findById(int id);

    void add(Admin admin);

    Admin findByname(String name);

}
