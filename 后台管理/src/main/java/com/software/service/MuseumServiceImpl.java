package com.software.service;

import com.software.dao.MuseumDao;
import com.software.entity.Museum;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional
public class MuseumServiceImpl implements MuseumService {


    @Autowired
    private MuseumDao museumDao;

    @Override
    public void update(Museum museum) {
        museumDao.update(museum);
    }

    @Override
    public void delete(String id) {
        museumDao.delete(id);
    }

    @Override
    public List<Museum> findAll() {
        return museumDao.findAll();
    }

    @Override
    public Museum findById(String id) {
        return museumDao.findById(id);
    }

    @Override
    public List<Museum> findByname(String name){
        return museumDao.findByname(name);
    }
}
