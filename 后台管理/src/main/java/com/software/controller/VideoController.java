package com.software.controller;


import com.software.entity.Video;
import com.software.service.VideoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;

@RestController
@CrossOrigin
@RequestMapping("video")
public class VideoController {

    @Autowired
    private VideoService videoService;

    //通用
    @GetMapping("findByvid")
    public Video findByvid(int vid){
        return  videoService.findByvid(vid);
    }

    /**
     视频页面
     */
    @PostMapping("update")
    public HashMap<String,Object> update(@RequestBody Video video){
        HashMap<String,Object> map=new HashMap<>();
        try{
            videoService.update(video);
            map.put("result","success");
            map.put("msg","更新成功");
        }catch (Exception e){
            e.printStackTrace();
            map.put("result","failed");
            map.put("msg","更新失败");
        }
        return map;
    }

    @GetMapping("delete")
    public HashMap<String,Object> delete(int vid){
        HashMap<String,Object> map=new HashMap<>();
        try{
            videoService.delete(vid);
            map.put("result","success");
            map.put("msg","删除成功");
        }catch (Exception e){
            e.printStackTrace();
            map.put("result","failed");
            map.put("msg","删除失败");
        }
        return map;
    }

    @GetMapping("findAll_passed")
    public List<Video> findAll_passed(){
        return videoService.findAll_passed();
    }

    @GetMapping("findByvname")
     public Video findByvname(String vname){
        return videoService.findByvname(vname);
     }

     @GetMapping("findBymname")
     public List<Video> findBymname(String mname){
        return videoService.findBymname(mname);
     }

     @GetMapping("findByuname")
    public List<Video> findByuname(String uname){
        return videoService.findByuname(uname);
    }

    /**
     * 审核页面
     */
    @GetMapping("findAll_ready")
    public List<Video> findAll_ready(){
        return videoService.findAll_ready();
    }

    //通过
    @GetMapping("pass")
    public HashMap<String,Object> pass(int vid){
        HashMap<String,Object> map=new HashMap<>();
        try{
            videoService.pass(vid);
            map.put("result","success");
            map.put("msg","操作成功");
        }catch (Exception e){
            e.printStackTrace();
            map.put("result","failed");
            map.put("msg","操作失败");
        }
        return map;
    }

    //不通过
    @GetMapping("fail")
    public HashMap<String,Object> fail(int vid){
        HashMap<String,Object> map=new HashMap<>();
        try{
            videoService.fail(vid);
            map.put("result","success");
            map.put("msg","操作成功");
        }catch (Exception e){
            e.printStackTrace();
            map.put("result","failed");
            map.put("msg","操作失败");
        }
        return map;
    }

}
