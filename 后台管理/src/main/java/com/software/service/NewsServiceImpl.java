package com.software.service;

import com.software.dao.NewsDao;
import com.software.entity.News;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional
public class NewsServiceImpl implements NewsService {

    @Autowired
    private NewsDao newsDao;

    @Override
    public void update(News news) {
        newsDao.update(news);
    }

    @Override
    public void delete(int id) {
        newsDao.delete(id);
    }

    @Override
    public List<News> findAll() {
        return newsDao.findAll();
    }

    @Override
    public List<News> findBymname(String mname){return  newsDao.findBymname(mname);}

    @Override
    public News findById(int id) {
        return newsDao.findById(id);
    }


}
