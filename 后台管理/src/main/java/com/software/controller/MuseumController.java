package com.software.controller;

import com.software.entity.Museum;
import com.software.service.MuseumService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;

@RestController
@CrossOrigin
@RequestMapping("museum")
public class MuseumController {
    @Autowired
    private MuseumService museumService;

    @GetMapping("findAll")
    public List<Museum> findAll(){
        return museumService.findAll();
    }

    @GetMapping("findById")
    public Museum findById(int mid){
        return museumService.findById(String.valueOf(mid));
    }

    @GetMapping("findBymname")
    public List findByname(String mname){
        return museumService.findByname(String.valueOf(mname));
    }

    @GetMapping("delete")
    public HashMap<String, Object> delete(int mid){
        HashMap<String,Object> map=new HashMap<>();
        try{
            museumService.delete(String.valueOf(mid));
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
    public HashMap<String, Object> delete(@RequestBody Museum museum){
        HashMap<String,Object> map=new HashMap<>();
        try{
            museumService.update(museum);
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
