package com.museum.imsub.controller;

import com.museum.imsub.entity.Ction;
import com.museum.imsub.entity.NewsId;
import com.museum.imsub.service.Newsdlservice;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;

@RestController
@CrossOrigin
@RequestMapping("News")
public class Newsdlcontroller {
    @Autowired
    private Newsdlservice newsdlservice;
    @GetMapping("findAll")
    public HashMap<String,Object>findAll(){
        HashMap<String,Object> map=new HashMap<>();
        List<NewsId> result  = newsdlservice.findAll();
        map.put("result",result);
        return map;
    }
    @GetMapping("findByid")
    public NewsId findByid(int id){
        return newsdlservice.findByid(id);
    }
    @GetMapping("findByname")
    public List<NewsId> findByname(String name){
        return newsdlservice.findByname(name);

    }

}
