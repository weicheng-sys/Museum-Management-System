package com.software.controller;

import com.software.entity.News;
import com.software.service.NewsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;


@RestController
@CrossOrigin
@RequestMapping("museum/news")
public class NewsController {
    @Autowired
    private NewsService newsService;

    @GetMapping("findAll")
    public List<News> findAll(){
        return newsService.findAll();
    }

    @GetMapping("findBymname")
    public List<News> findBymname(String mname){
        return newsService.findBymname(mname);
    }

    @GetMapping("findBynid")
    public News findById(int nid){
        return newsService.findById(nid);
    }

    @GetMapping("delete")
    public HashMap<String, Object> delete(int nid){
        HashMap<String,Object> map=new HashMap<>();
        try{
            newsService.delete(nid);
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
    public HashMap<String, Object> delete(@RequestBody News news){
        HashMap<String,Object> map=new HashMap<>();
        try{
            newsService.update(news);
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
