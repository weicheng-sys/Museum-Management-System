package com.software.service;

import com.software.dao.VideoDao;
import com.software.entity.Video;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional
public class VideoServiceImpl implements VideoService {

    @Autowired
    private VideoDao videoDao;

    @Override
    public Video findByvid(int vid) {
        return videoDao.findByvid(vid);
    }

    @Override
    public void update(Video video) {
        videoDao.update(video);
    }

    @Override
    public void delete(int vid) {
        videoDao.delete(vid);
    }

    @Override
    public List<Video> findAll_passed() {
        return videoDao.findAll_passed();
    }

    @Override
    public Video findByvname(String vname) {
        return videoDao.findByvname(vname);
    }

    @Override
    public List<Video> findBymname(String mname) {
        return videoDao.findBymname(mname);
    }

    @Override
    public List<Video> findByuname(String uname) {
        return videoDao.findByuname(uname);
    }

    @Override
    public List<Video> findAll_ready() {
        return videoDao.findAll_ready();
    }

    @Override
    public void pass(int vid) {
        videoDao.pass(vid);
    }

    @Override
    public void fail(int vid) {
        videoDao.fail(vid);
    }
}
