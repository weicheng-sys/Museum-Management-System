package com.software.dao;


import com.software.entity.News;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
@Repository
public interface NewsDao {
    void update(News news);

    void delete(int nid);

    List<News> findAll();

    List<News> findBymname(String mname);

    News findById(int nid);

}
