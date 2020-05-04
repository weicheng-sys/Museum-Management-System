package com.software.service;

import com.software.dao.AdminDao;
import com.software.entity.Admin;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;


@Service
@Transactional
public class AdminServiceImpl implements AdminService {

    @Autowired
    private AdminDao adminDao;

    @Override
    public void update(Admin admin) {
        adminDao.update(admin);
    }

    @Override
    public void delete(int id) {
        adminDao.delete(id);
    }

    @Override
    public List<Admin> findAll() {
        return adminDao.findAll();
    }

    @Override
    public Admin findById(int id) {
        return adminDao.findById(id);
    }

    @Override
    public void add(Admin admin) {
        adminDao.add(admin);
    }

    @Override
    public Admin findByname(String name) {
        return adminDao.findByname(name);
    }
}
