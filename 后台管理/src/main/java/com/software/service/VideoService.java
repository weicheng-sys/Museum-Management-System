package com.software.service;

import com.software.entity.Video;

import java.util.List;

public interface VideoService {
    //通用
    Video findByvid(int vid);

    /**
     视频页面
     */
    void update(Video video);

    void delete(int vid);

    List<Video> findAll_passed();

    Video findByvname(String vname);

    List<Video> findBymname(String mname);

    List<Video> findByuname(String uname);

    /**
     * 审核页面
     */
    List<Video> findAll_ready();

    //通过
    void pass(int vid);

    //不通过
    void fail(int vid);
}
