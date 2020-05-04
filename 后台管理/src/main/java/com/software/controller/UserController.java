package com.software.controller;


import com.software.entity.News;
import com.software.entity.User;
import com.software.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;

@RestController
@CrossOrigin
@RequestMapping("user")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("findAll")
    public List<User> findAll(){
        return userService.findAll();
    }


    @GetMapping("findByid")
    public User findById(int uid){
        return userService.findById(uid);
    }

    @GetMapping("findByname")
    public List findByname(String uname){return  userService.findByname(uname);}

    @GetMapping("delete")
    public HashMap<String, Object> delete(int uid){
        HashMap<String,Object> map=new HashMap<>();
        try{
            userService.delete(uid);
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
    public HashMap<String, Object> delete(@RequestBody User user){
        HashMap<String,Object> map=new HashMap<>();
        try{
            userService.update(user);
            map.put("result","success");
            map.put("msg","更新成功");
        }catch (Exception e){
            e.printStackTrace();
            map.put("result","failed");
            map.put("msg","更新失败");
        }
        return map;
    }
}
