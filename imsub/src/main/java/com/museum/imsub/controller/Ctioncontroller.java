package com.museum.imsub.controller;

import com.museum.imsub.entity.Ction;

import com.museum.imsub.service.Ctionservice;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
@RestController
@CrossOrigin
@RequestMapping("Ction")
public class Ctioncontroller {
    @Autowired
    private Ctionservice ctionservice;
    @GetMapping("findAll")
    public HashMap<String,Object> findAll(){
        HashMap<String,Object> map=new HashMap<>();
        List<Ction> result  = ctionservice.findAll();
        map.put("result",result);

        return map;

    }
    @GetMapping("findOne")
    public Ction findOne(int id){
        return ctionservice.findByid(id);
    }
}
