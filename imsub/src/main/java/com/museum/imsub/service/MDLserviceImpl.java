package com.museum.imsub.service;

import com.museum.imsub.dao.MDLDAO;
import com.museum.imsub.entity.MDL;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.annotation.Resource;
import java.util.List;
@Service
@Transactional
public class MDLserviceImpl implements MDLservice {
    @Autowired
    @Resource
    private MDLDAO mdldao;
    @Override
    public List<MDL> findAll() {
        return mdldao.findAll();
    }

    @Override
    public MDL findByid(int id) {
        return mdldao.findByid(id);
    }

    @Override
    public void update(MDL mdl) {
        mdldao.update(mdl);
    }

    @Override
    public List<MDL> findBYGrade() {
        return mdldao.findBYGrade();
    }

    @Override
    public List<MDL> findBYGrade1() {
        return mdldao.findBYGrade1();
    }

    @Override
    public List<MDL> findBYGrade2() {
        return mdldao.findBYGrade2();
    }

    @Override
    public List<MDL> findBYGrade3() {
        return mdldao.findBYGrade3();
    }
}
