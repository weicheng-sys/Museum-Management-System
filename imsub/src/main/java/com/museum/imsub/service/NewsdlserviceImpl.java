package com.museum.imsub.service;


import com.museum.imsub.dao.NewsdlDAO;
import com.museum.imsub.entity.NewsId;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.annotation.Resource;
import java.util.List;
@Service
@Transactional
public class NewsdlserviceImpl implements Newsdlservice {
    @Autowired
    @Resource
    private NewsdlDAO newsdlDAO;
    @Override
    public List<NewsId> findAll() {
        return newsdlDAO.findAll();
    }

    @Override
    public NewsId findByid(int id) {
        return newsdlDAO.findByid(id);
    }

    @Override
    public List<NewsId> findByname(String name) {
        return newsdlDAO.findByname(name);
    }
}
