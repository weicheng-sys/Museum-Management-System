package com.museum.imsub.entity;
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

public class NewsId {
    private int nid;
    private String title;
    private String content;
    private String publisher;
    private String ntime;
    private String nimg;
    private String mname;
    private String evaluation;
    private String source;
}
