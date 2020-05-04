package com.software.service;

import com.software.entity.User;

import java.util.List;

public interface UserService {

    void update(User user);

    void delete(int id);

    List<User> findAll();

    List findByname(String mname);

    User findById(int id);

}
