package com.museum.imsub.service;

import com.museum.imsub.dao.CtionDAO;
import com.museum.imsub.entity.Ction;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.annotation.Resource;
import java.util.List;

@Service
@Transactional
public class CtionserviceImpl implements Ctionservice {

    @Autowired
    @Resource
    private CtionDAO ctionDAO;

    @Override
    public List<Ction> findAll() {
        return ctionDAO.findAll();
    }

    @Override
    public Ction findByid(int id) {
        return ctionDAO.findByid(id);
    }
}
