package com.software.controller;


import com.software.entity.Admin;
import com.software.service.AdminService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;

@RestController
@CrossOrigin
@RequestMapping("admin")
public class AdminController {

    @Autowired
    private AdminService adminService;

    @GetMapping("findAll")
    public List<Admin> findAll(){
        return adminService.findAll();
    }


    @GetMapping("findByid")
    public Admin findById(int uid){
        return adminService.findById(uid);
    }

    @GetMapping("findByname")
    public Admin findByname(String uname){
        return adminService.findByname(uname);
    }

    @GetMapping("delete")
    public HashMap<String, Object> delete(int uid){
        HashMap<String,Object> map=new HashMap<>();
        try{
            adminService.delete(uid);
            map.put("result","success");
            map.put("msg","删除成功");
        }catch (Exception e){
            e.printStackTrace();
            map.put("result","failed");
            map.put("msg","删除失败");
        }
        return map;
    }

    @PostMapping("update")
    public HashMap<String, Object> delete(@RequestBody Admin admin){
        HashMap<String,Object> map=new HashMap<>();
        try{
            adminService.update(admin);
            map.put("result","success");
            map.put("msg","更新成功");
        }catch (Exception e){
            e.printStackTrace();
            map.put("result","failed");
            map.put("msg","更新失败");
        }
        return map;
    }

    @PostMapping("add")
    public HashMap<String,Object> add(@RequestBody Admin admin){
        HashMap<String,Object> map=new HashMap<>();
        try{
            adminService.add(admin);
            map.put("result","success");
            map.put("msg","添加成功");
        }catch (Exception e){
            e.printStackTrace();
            map.put("result","failed");
            map.put("msg","添加失败");
        }
        return map;
    }

}
