package com.software.entity;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;
import lombok.experimental.Accessors;

@Data
@AllArgsConstructor
@NoArgsConstructor
@ToString
@Accessors(chain = true)
public class Video {
    int vid;
    int uid;
    int mid;
    String vname;
    String vaddr;
    String vinfo;
    int status;

}
