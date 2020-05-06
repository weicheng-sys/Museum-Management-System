package com.museum.imsub.dao;

import com.museum.imsub.entity.NewsId;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;
@Mapper
@Repository
public interface NewsdlDAO {
    List<NewsId> findAll();

    NewsId findByid(int id);
    List<NewsId> findByname(String name);
}
