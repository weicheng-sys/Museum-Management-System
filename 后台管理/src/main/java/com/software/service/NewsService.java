package com.software.service;

import com.software.entity.News;

import java.util.List;

public interface NewsService {
    void update(News news);

    void delete(int id);

    List<News> findAll();

    List<News> findBymname(String name);

    News findById(int id);
}
