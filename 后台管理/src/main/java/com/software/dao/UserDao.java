package com.software.dao;

import com.software.entity.User;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;
import java.util.List;

@Mapper
@Repository
public interface UserDao {

    void update(User user);

    void delete(int id);

    List<User> findAll();

    List findByname(String mname);

    User findById(int id);

}
