package com.museum.imsub.service;

import com.museum.imsub.entity.NewsId;

import java.util.List;

public interface Newsdlservice {
    List<NewsId> findAll();
    NewsId findByid(int id);
    List<NewsId> findByname(String name);
}
