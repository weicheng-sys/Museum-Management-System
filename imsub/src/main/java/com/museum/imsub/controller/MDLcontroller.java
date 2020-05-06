package com.museum.imsub.controller;

import com.museum.imsub.entity.MDL;
import com.museum.imsub.service.MDLservice;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
@RestController
@CrossOrigin
@RequestMapping("MDL")
public class MDLcontroller {
    @Autowired
    private MDLservice mdLservice;
    @GetMapping("findAll")
    public HashMap<String,Object> findAll(){
        HashMap<String,Object> map=new HashMap<>();
        List<MDL> result  = mdLservice.findAll();
        map.put("result",result);

        return map;
    }
    @GetMapping("findByid")
    public MDL findByid(int id){
        return mdLservice.findByid(id);
    }
    @PostMapping("update")
    public HashMap<String,Object> update(@RequestBody MDL mdl){
        HashMap<String,Object> map = new HashMap<>();
            mdLservice.update(mdl);
            map.put("ok","ok");
        return map;
    }
    @GetMapping("findBYGrade")
    public HashMap<String,Object> findBYGrade(){
        HashMap<String,Object> map=new HashMap<>();
        List<MDL> result  = mdLservice.findBYGrade();
        map.put("result",result);

        return map;
    }
    @GetMapping("findBYGrade1")
    public HashMap<String,Object> findBYGrade1(){
        HashMap<String,Object> map=new HashMap<>();
        List<MDL> result  = mdLservice.findBYGrade1();
        map.put("result",result);

        return map;
    }
    @GetMapping("findBYGrade2")
    public HashMap<String,Object> findBYGrade2(){
        HashMap<String,Object> map=new HashMap<>();
        List<MDL> result  = mdLservice.findBYGrade2();
        map.put("result",result);

        return map;
    }
    @GetMapping("findBYGrade3")
    public HashMap<String,Object> findBYGrade3(){
        HashMap<String,Object> map=new HashMap<>();
        List<MDL> result  = mdLservice.findBYGrade3();
        map.put("result",result);

        return map;
    }

}
